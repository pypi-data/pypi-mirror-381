import sys
import logging

from collections import defaultdict
from pathlib import Path
from shlex import join as shlex_join
from shutil import which
from subprocess import Popen, DEVNULL, PIPE
from textwrap import indent
from typing import Union, Iterable, Tuple, Any, AnyStr, Hashable, Optional

from .log import log_verbosity


AnyStrOrPath = Union[AnyStr,Path]


class VersionedDict:
	'''A dict that can have multiple versions with different contents. Accessing
	d[version] will return the value of the dict for the given version. Adding
	a {key: value} for a range of versions can be done through the .add()
	method.
	'''
	__slots__ = ('_versions', '_cache')

	def __init__(self, iterable: Optional[Iterable[Tuple[Hashable,Hashable,Hashable,Any]]]=None):
		'''Instantiate a VersionedDict given initial version ranges and relative
		key-value pairs, or an empty VersionedDict if iterable is not given.

		The given iterable= is an iterable of tuples where each tuple is of the
		form (vstart, vend, key, val), i.e., the same parameters taken by the
		.add() method.
		'''
		self._cache    = {}
		self._versions = defaultdict(dict)

		if iterable is not None:
			for vstart, vend, key, val in iterable:
				self._versions[vstart, vend][key] = val

	def __getitem__(self, version: Hashable) -> dict:
		'''Get the dict corresponding to the given version.
		'''
		if version not in self._cache:
			self._cache[version] = self._getversion(version)
		return self._cache[version]

	def _getversion(self, version: Hashable) -> dict:
		'''Create and return the dict corresponding to the given version.
		'''
		res = {}
		for (vstart, vend), dct in self._versions.items():
			if vstart <= version < vend:
				res.update(dct)
		return res

	def add(self, vstart: Hashable, vend: Hashable, key: Hashable, value: Any):
		'''Add a {key: value} mapping for all versions of this VersionedDict
		between vstart (included) and vend (not included).
		'''
		self._versions[vstart, vend][key] = value

		# Invalidate cache for any version in [vstart, vend)
		for v in self._cache:
			if vstart <= v < vend:
				del self._cache[v]


class VersionedList:
	'''A list that can have multiple versions with different contents. Accessing
	lst[version] will return the value of the list for the given version. Adding
	values for a range of versions can be done through the .add() method.
	'''
	__slots__ = ('_versions', '_cache')

	def __init__(self, iterable: Optional[Iterable[Tuple[Hashable,Hashable,Iterable[Any]]]]=None):
		'''Instantiate a VersionedList given initial version ranges and relative
		values, or an empty VersionedList if iterable is not given.

		The given iterable= is an iterable of tuples where each tuple is of the
		form (vstart, vend, iterable_of_values), i.e., the same parameters taken
		by the .add() method.
		'''
		self._cache    = {}
		self._versions = defaultdict(list)

		if iterable is not None:
			for vstart, vend, values in iterable:
				self._versions[vstart, vend].extend(values)

	def __getitem__(self, version: Hashable) -> list:
		'''Get the list corresponding to the given version.
		'''
		if version not in self._cache:
			self._cache[version] = self._getversion(version)
		return self._cache[version]

	def _getversion(self, version: Hashable) -> list:
		'''Create and return the list corresponding to the given version.
		'''
		res = []
		for (vstart, vend), lst in self._versions.items():
			if vstart <= version < vend:
				res.extend(lst)
		return res

	def add(self, vstart: Hashable, vend: Hashable, values: Iterable[Any]):
		'''Add all the values from values to for all versions of this
		VersionedList between vstart (included) and vend (not included).
		'''
		self._versions[vstart, vend].extend(values)

		# Invalidate cache for any version in [vstart, vend)
		for v in self._cache:
			if vstart <= v < vend:
				del self._cache[v]


def maybe_rel(path: Path, root: Path) -> Path:
	'''Calculate and return a the given path relative to root. If path is not
	relative to root, it is returned as is.
	'''
	return path.relative_to(root) if root is not None and path.is_relative_to(root) else path

def anyprefix(s: str, *pxs: str) -> bool:
	'''Determine whether the given string as any of the given prefixes.
	'''
	return any(s.startswith(px) for px in pxs)

def anysuffix(s: str, *sxs: str) -> bool:
	'''Determine whether the given string as any of the given suffixes.
	'''
	return any(s.endswith(sx) for sx in sxs)

def noprefix(s: str, *pxs: str) -> str:
	'''Find the first matching prefix in s among pxs and return a new string
	without it. If s does not have any of the given prefixes, it is returned as
	is.
	'''
	for px in pxs:
		if s.startswith(px):
			return s[len(px):]
	return s

def nosuffix(s: str, *sxs: str) -> str:
	'''Find the first matching suffix in s among sxs and return a new string
	without it. If s does not have any of the given suffixes, it is returned as
	is.
	'''
	for sx in sxs:
		if s.endswith(sx):
			return s[:-len(sx)]
	return s

def do_popen(cmd: Union[AnyStr,Iterable[AnyStr]], cwd: Union[AnyStr,Path], **kwargs) -> Popen:
	'''Conveniency wrapper around subprocess.Popen, which gracefully handles
	FileNotFoundError and NotADirectoryError providing useful logging to the
	user.
	'''
	try:
		return Popen(cmd, cwd=cwd, **kwargs)
	except FileNotFoundError:
		# We can also get here if the passed cwd= is invalid, so differentiate
		# between the two. Yes this is racy... see if I care.
		if cwd.exists():
			cmd = cmd.split()[0] if isinstance(cmd, str) else cmd[0]
			logging.critical('Command not found: %s', cmd)
		else:
			logging.critical('Directory does not exist: %s', cwd)
	except NotADirectoryError:
		logging.critical('Path is not a directory: %s', cwd)

	return None

def command_argv_to_string(cmd: Union[AnyStrOrPath,Iterable[AnyStrOrPath]]) -> str:
	'''Convert the given command, which can be str, bytes, Path, or an iterable
	containing any of those, to a shlex-escaped string.
	'''
	if isinstance(cmd, Path):
		return str(cmd)
	elif isinstance(cmd, bytes):
		return cmd.decode()
	elif isinstance(cmd, str):
		return cmd

	parts = []
	for part in cmd:
		if isinstance(part, Path):
			parts.append(str(part))
		elif isinstance(part, bytes):
			parts.append(part.decode())
		else:
			parts.append(part)

	return shlex_join(parts)

def run_command(cmd: Union[AnyStrOrPath,Iterable[AnyStrOrPath]],
		cwd: Optional[AnyStrOrPath]=None, stdin: Optional[AnyStr]=None,
		console_output: bool=False) -> int:
	'''Run the given command (cmd), optionally under the given working directory
	(cwd), optionally passing the given data to standard input (stdin), and
	optionally enabling console output. The returned value is the exit code of
	the command.
	'''
	if log_verbosity() >= 3:
		logging.debug('Running command: %s', command_argv_to_string(cmd))

	if console_output:
		stdout, stderr = sys.stdout, sys.stderr
	else:
		stdout = stderr = DEVNULL

	child = do_popen(cmd, cwd=cwd, shell=isinstance(cmd, str), stdout=stdout, stderr=stderr)
	if child is None:
		return 127

	child.communicate(stdin)
	return child.returncode

def ensure_command(cmd: Union[AnyStrOrPath,Iterable[AnyStrOrPath]],
		cwd: Optional[AnyStrOrPath]=None, stdin: Optional[AnyStr]=None,
		capture_stdout: bool=True, console_output: bool=False) -> AnyStr:
	'''Run the given command (cmd), optionally under the given working directory
	(cwd), optionally passing the given data to standard input (stdin),
	capturing and returning its standard output (if capture_stdout=True) and
	optionally enabling console output (if console_output=True).

	If the given command is not found or exits with a non-zero exit code, the
	standard error produced by the command is loggged and the caller is
	terminated by means of sys.exit().
	'''
	# console_output implies not capture_stdout
	assert not console_output or not capture_stdout

	if log_verbosity() >= 3:
		logging.debug('Running command: %s', command_argv_to_string(cmd))

	if console_output:
		stdout, stderr = sys.stdout, sys.stderr
	else:
		stdout = PIPE if capture_stdout else DEVNULL
		stderr = PIPE

	child = do_popen(cmd, cwd=cwd, shell=isinstance(cmd, str), stdout=stdout, stderr=stderr, text=True)
	if child is None:
		sys.exit(127)

	out, err = child.communicate(stdin)

	if child.returncode != 0:
		if stderr == PIPE:
			err = ('\n' + indent(err, '\t')) if err.strip() else ' (no stderr output)'
		else:
			err = ''

		logging.critical('Command returned %d: %s%s', child.returncode, cmd, err)
		sys.exit(1)

	return out

def command_available(name: AnyStr) -> bool:
	'''Wrapper for shutil.which to determine whether a command is available or
	not (i.e., whether it is under the current PATH paths) given its name.
	'''
	return which(name) is not None

def gcc_version(gcc_cmd: AnyStr) -> str:
	'''Run GCC to get its version and return it as a string. Execution will be
	aborted if the given GCC command is not found.
	'''
	return ensure_command((gcc_cmd, '--version')).splitlines()[0].strip()

def git_checkout(repo_dir: Union[AnyStr,Path], ref: AnyStr):
	'''Run git checkout inside repo_dir to check out to the given ref. Execution
	will be aborted if git is not found or errors out.
	'''
	ensure_command(('git', 'checkout', ref), cwd=repo_dir, capture_stdout=False)

def format_duration(s: float) -> str:
	'''Convert a duration in seconds to a human readable string specifying
	hours, minutes and seconds.
	'''
	s = round(s)
	h = s // 3600
	s %= 3600
	m = s // 60
	s %= 60

	if h > 0:
		return f'{h}h {m:02d}m {s:02d}s'
	if m > 0:
		return f'{m}m {s:02d}s'
	return f'{s}s'
