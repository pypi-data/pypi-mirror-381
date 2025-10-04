# 🌟 ModXPy — The Python Module Universe at Your Fingertips 🌟

Welcome to ModXPy, the ultimate playground for Python’s modules.  
With ModXPy you can instantly import, explore, and experiment with the entire Python standard library — plus any installed third-party modules — all from one simple interface.



##### UPDATE 1.8.1---

###### Updated vcompat() to print

###### a neater looking table instead of list.

###### Fix multiple bugs of vcompat(), including

###### f-string bugs, printing bugs, etc.---



## 🚀 Installation

Install directly from PyPI:
pip install modxpy

In Python, import as import modx (not modxpy)



# Functions:



🔹 import\_all()

Imports about every standard library module at once.

🔹 import\_random(n)

Imports n random modules from the standard library.

🔹 import\_letter(letter)

Imports all standard library modules whose names start with the given letter.

🔹 import\_external()

Attempts to import every third-party module you currently have installed.

🔹 import\_screen()

Imports every module that uses a screen/GUI (like pygame or turtle).

🔹 list\_importall()

Returns a list of modules that would be imported by import\_all().

🔹 modules\_loaded()

Shows how many modules you currently have downloaded on your device.

🔹 imported()

Lists the modules imported since ModX loaded (user + ModX), including dependencies.

🔹 modx\_imported()

Lists the modules that were ONLY imported by ModX, NOT including user imports
and dependencies.

🔹 import\_letter(letter)

Import every standard library module from the ModX 'modules' list
whose name starts with the given letter (case-insensitive).

🔹 search\_modules(keyword)

Search for modules whose names contain the keyword.

🔹 info(module\_name)

Shows basic info about typed module: file path, built-in status, docstring.

🔹 is\_imported(module)

Checks if module is currently imported into Python Shell (Not Pythonlib)

🔹 dependencies()

Shows what other modules a specific module depends on without importing it.

🔹 vcompat(module\_name, python\_version)

Checks if a module is compatible with a python version, if a version was given.

🔹 modfunctions(module)

Show how many and what functions a module has without importing it.



# Example Code:





import modx  # import ModX module



Import almost every standard library module at once

modx.import\_all()

Output: (Imports 200+ standard library modules silently)

Bulk import completed!



Show all modules imported after ModX loaded (user + ModX)

modx.imported()

Output:

Modules imported after ModX load (user, ModX and dependencies):

\- \_collections\_abc

\- \_weakrefset

\- abc

\- collections

\- codecs

\- copyreg

\- encodings

\- encodings.aliases

\- encodings.utf\_8

\- enum

\- io

\- keyword

\- linecache

\- os

\- random

\- re

\- sys

\- turtle

\- zipfile

Total modules imported after ModX load: 19



Show only modules imported via ModX functions

modx.modx\_imported()

Output:

Modules imported via ModX:

\- collections

\- json

\- math

\- random

\- re

\- turtle

\- zipfile

Total modules imported via ModX: 7



Import 5 random modules from ModX list

modx.import\_random(5)

Output: \['turtle', 'json', 'zipfile', 'math', 're']

These 5 modules were randomly selected and imported



Import all modules starting with letter 't'

modx.import\_letter('t')

Output: \['tabnanny', 'tarfile', 'tempfile', 'test', 'textview', 'textwrap', 'threading', 'timeit', 'tkinter', 'token', 'tokenize', 'tomllib', 'tooltip', 'trace', 'traceback', 'tracemalloc', 'tree', 'turtle', 'turtledemo', 'types', 'typing']

All standard library modules starting with 't' were imported



Import all installed third-party modules (if any)

modx.import\_external()

Output: (Imports numpy, pandas, requests, etc. if installed silently)

Third-party modules imported if available



Import common screen/GUI/game modules if available

modx.import\_screen()

Output: (Imports pygame, tkinter, turtle, etc. if available silently)

GUI modules imported if available



Get the list of modules import\_all() would import

modx.list\_importall()

Output: \['collections', 'sys', 'asyncio', 'concurrent', 'ctypes', 'dbm', 'email', 'encodings', 'ensurepip', 'html', ...] (250+ modules)

Complete list of all modules ModX can import



Get list of standard library modules NOT yet imported

modx.nonimported()

Output: \['abc', 'argparse', 'ast', 'base64', 'bdb', 'bisect', 'bz2', 'calendar', 'cmd', 'codecs', ...] (xxx modules)

Standard library modules that haven't been imported yet



Search for modules containing the keyword 'json'

modx.search\_modules('json')

Output: \['json']

Found modules containing 'json' in their names



Show information about a specific module

modx.info('random')

Output:

Module: random

Path: /usr/lib/python3.11/random.py

Docstring:

Random variable generators.

Shows file path and docstring for the random module



\#Check if random is imported
is\_imported("random")
#Output: True



\#Check all dependencies of module random
dependencies("random")
#Output: Dependencies found:
\_collections\_abc
\_random
\_sha2
argparse
bisect
hashlib
itertools
math
operator
os
statistics
time
warnings



Show if pygame is compatible with Python 2.0

modx.vcompat("pygame", 2.0)
#Output: Compatibility Report for: pygame
Target Python Version: 2.0
Warnings Found: 2

1. UNAVAILABLE: match - Added in 3.10
2. SYNTAX: f-strings require Python 3.6+



Show ModX built-in help screen

modx.modxhelp()

Output:

ModX — The Python Module Universe

=================================



Functions:

----------



import\_all()

Import almost every standard library module at once.

Example: modx.import\_all()



import\_external()

Import all installed third-party modules.

Example: modx.import\_external()



... (full help text continues)



# 💡 Why Use ModX?



Explore the Python standard library in seconds

Stress-test your environment by bulk importing modules

See hidden dependencies that load behind the scenes

Experiment with random imports for fun or testing

Discover new modules you didn’t know existed



ModXPy turns Python’s module system into a playground —
perfect for learning, testing, or just satisfying your curiosity.
Install it today with pip install modxpy, import it with import modx,
and start discovering how many modules Python already has waiting for you!

