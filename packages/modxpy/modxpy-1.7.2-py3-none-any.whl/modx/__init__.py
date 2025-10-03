'''modx.py: A module whose functions have to do with other modules.
For example: importall(), a function used to import every single module
in Python that is supported on most devices without printing an
error message, does not print out dialog nor pop up a link when
imported, and not required to be downloaded
separately with Python (such as Pygame, downloaded in Terminal).

Modules ios_support, pty, this, sre_compile, sre_parse,
sre_constants, tty, idle and antigravity are left out of import_all().
Reason: ios_support not supporting computers,
pty and tty importing a nonexistent module (termios),
sre_compile, sre_constants and sre_parse printing warnings,
this printing out "The Zen of Python" poem, idle
opening up Python Shell window, and
antigravity popping out a web browser link
(There are more modules left out but the full list is way too long).

Permission to use this module is granted to anyone wanting to use it,
under the following conditions: 1.) Any copies of this module must be clearly
marked as so. 2.) The original of this module must not be misrepresented;
you cannot claim this module is yours.'''

#Notes: for imported(), module idlelib will not show up as it is pre-imported
#as soon as this module is run, leading to problems and bugs, thus idlelib
#is not shown in imported().

#for vcompat(), module modx will not work as vcompat
#checks the content of a module for version-specified content. As vcompat
#has a list of a lot of version-specified content, the check shows it and
#prints the whole list as potential problems.

#vcompat() checks for most issues for 2.0-3.12 and not all. If every one
#were to be included, the rules alone would be about 1500 lines and the rest
#would be 200 lines-ish. Most of the major problems are included in vcompat().
#Only less, very rare problems are left out.

#Created by: Austin Wang. Created at: September 19, 2025. Version: 1.7.2

import sys, importlib, pkgutil, random, builtins, ast, importlib.util, os, tokenize, io
from pathlib import Path
from packaging import version

# Record baseline modules at time of ModX load
_initial_modules = set(sys.modules.keys())

# Capture original import
_original_import = builtins.__import__

# Track modules imported manually by user after ModX loaded
_user_imports = set()

def _tracking_import(name, globals=None, locals=None, fromlist=(), level=0):
    """Internal function. Not designed for public use."""
    mod = _original_import(name, globals, locals, fromlist, level)
    top_name = name.partition('.')[0]
    if not top_name.startswith('idlelib'):
        _user_imports.add(top_name)
    return mod

# Install hook
builtins.__import__ = _tracking_import

# Track modules imported by ModX (ONLY directly requested ones)
_imported_by_modx = set()

# -------------------------
# Master Module List
# -------------------------
modules = [
        'collections', 'sys', 'asyncio', 'concurrent', 'ctypes', 'dbm', 'email',
        'encodings', 'ensurepip', 'html', 'http', 'idlelib', 'importlib', 'json', 'logging',
        'multiprocessing', 'pathlib', 'pydoc_data', 're', 'sqlite3',
        'sysconfig', 'test', 'tkinter', 'tomllib', 'turtledemo', 'unittest', 'urllib',
        'venv', 'wsgiref', 'xml', 'xmlrpc', 'zipfile', 'zoneinfo',
        '_pyrepl', '_collections_abc', '_colorize',
        '_compat_pickle', '_compression', '_markupbase', '_opcode_metadata',
        '_py_abc', '_pydatetime', '_pydecimal', '_pyio', '_pylong', '_sitebuiltins', '_strptime',
        '_threading_local', '_weakrefset', 'abc', 'argparse', 'ast', 'base64', 'bdb',
        'bisect', 'bz2', 'calendar', 'cmd', 'codecs', 'codeop', 'colorsys', 'compileall', 'configparser',
        'contextlib', 'contextvars', 'copy', 'copyreg', 'cProfile', 'csv', 'dataclasses', 'datetime',
        'decimal', 'difflib', 'dis', 'doctest', 'enum', 'filecmp', 'fileinput', 'fnmatch', 'fractions',
        'ftplib', 'functools', 'genericpath', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib',
        'gzip', 'hashlib', 'heapq', 'hmac', 'imaplib', 'inspect', 'io', 'ipaddress', 'keyword', 'linecache',
        'locale', 'lzma', 'math', 'mailbox', 'mimetypes', 'modulefinder', 'netrc',
        'opcode', 'optparse', 'os', 'pdb', 'pickle', 'pickletools', 'pkgutil',
        'platform', 'plistlib', 'poplib', 'pprint', 'profile', 'pstats', 'py_compile',
        'pyclbr', 'pydoc', 'queue', 'quopri', 'random', 'reprlib', 'runpy', 'sched', 'secrets',
        'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtplib', 'socket', 'socketserver',
        'ssl', 'stat', 'statistics', 'string', 'stringprep',
        'struct', 'subprocess', 'symtable', 'tabnanny', 'tarfile', 'tempfile', 'textwrap',
        'threading', 'timeit', 'token', 'tokenize', 'trace', 'traceback', 'tracemalloc', 'turtle',
        'types', 'typing', 'uuid', 'warnings', 'wave', 'weakref', 'webbrowser', 'zipapp', 'zipimport',
        '__future__', '__hello__', '__phello__', "atexit", "mmap",
        'autocomplete','autocomplete_w','autoexpand','browser','build',
        'calltip','calltip_w','codecontext','colorizer',
        'config','config_key','configdialog','debugger','debugger_r',
        'debugobj','debugobj_r','delegator','direct','dynoption','editor',
        'filelist','format','grep','help','help_about','history','hyperparser',
        'id','idle_test','iomenu','keyring','mainmenu','more_itertools',
        'multicall','outwin','parenmatch','pathbrowser','percolator','pyparse',
        'pyshell','query','redirector','replace','rpc','run',
        'runscript','screeninfo','scrolledlist','search','searchbase','searchengine',
        'sidebar','squeezer','stackviewer','statusbar','textview','tooltip',
        'tree','undo','util','window','zoomheight','zzdummy', 'builtins', 'itertools',
        'operator', 'collections.abc', 'errno', 'msvcrt', 'array', 'marshal',
        'rlcompleter', 'urllib.request', 'urllib.response', 'urllib.parse', 'urllib.error', 
        'urllib.robotparser', 'http.client', 'http.server',
        'xml.etree.ElementTree', 'xml.parsers.expat',
        '_thread', '_weakref', '_collections', '_ast', '_bisect',
        '_heapq', '_io', '_functools', '_operator', '_signal', '_socket', '_ssl',
        '_stat', '_struct', '_datetime', '_random', '_hashlib', '_md5', '_sha1',
        '_blake2', '_pickle', '_json', '_zoneinfo', '_opcode', 'cmath', 'numbers',
        '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr',
        '_codecs_tw', '_interpchannels', '_interpqueues', '_interpreters',
        '_multibytecodec', '_sha2', '_sha3', '_suggestions', 'faulthandler', 'xxsubtype'
        ]
from .reporting import *
from .info import *
from .help import *
from .import import *
