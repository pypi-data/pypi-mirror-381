def dependencies(module_name):
    """Show what other modules a specific module depends on without importing it."""
    import re
    import ast
    
    dependencies = set()
    
    print(f"Dependency analysis for: {module_name}")
    print("=" * 40)
    
    try:
        # Find the module spec without importing
        spec = importlib.util.find_spec(module_name)
        if not spec:
            print(f"Module '{module_name}' not found")
            return
        
        if spec.origin and spec.origin.endswith('.py'):
            print(f"File: {spec.origin}")
            
            try:
                with open(spec.origin, 'r', encoding='utf-8') as f:
                    source_code = f.read()
                
                # Parse with AST for accurate import detection
                try:
                    tree = ast.parse(source_code)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                dependencies.add(alias.name.split('.')[0])
                        elif isinstance(node, ast.ImportFrom):
                            if node.module:  # from x import y
                                dependencies.add(node.module.split('.')[0])
                except SyntaxError:
                    # Fallback to regex for compiled modules or syntax issues
                    imports = re.findall(r'^(?:import|from)\s+([\w\.]+)', source_code, re.MULTILINE)
                    for imp in imports:
                        dependencies.add(imp.split('.')[0])
                        
            except (UnicodeDecodeError, FileNotFoundError, IOError):
                print("   (Source not readable)")
        
        elif spec.origin:
            print(f"File: {spec.origin} (compiled module)")
        else:
            print("   (Built-in module)")
        
        # Filter out common built-ins and self
        dependencies.discard(module_name.split('.')[0])
        dependencies.discard('__future__')
        dependencies.discard('builtins')
        
        # Show results
        if dependencies:
            print("Dependencies found:")
            for dep in sorted(dependencies):
                # Check if dependency would be importable
                dep_spec = importlib.util.find_spec(dep)
                status = "[AVAILABLE]" if dep_spec else "[NOT FOUND]"
                print(f"   {dep}")
        else:
            print("No external dependencies found")
            
    except Exception as e:
        print(f"Error analyzing module: {e}")

def search_modules(keyword):
    """Search for modules whose names contain the keyword."""
    keyword = keyword.lower()
    return [m for m in modules if keyword in m.lower()]

def info(module_name):
    """Show basic info about a module: file path, built-in status, docstring."""
    import inspect
    try:
        mod = sys.modules[module_name] if module_name in sys.modules else importlib.import_module(module_name)
    except ImportError:
        print(f"Module '{module_name}' not found.")
        return
    path = getattr(mod, '__file__', '(built-in)')
    doc = (inspect.getdoc(mod) or '').splitlines()[0:3]
    print(f"Module: {module_name}")
    print(f"Path: {path}")
    print("Docstring:")
    for line in doc:
        print(line)

def is_imported(module_name: str):
    """
    Check if a module is imported in the caller's globals.
    True  -> currently imported in shell globals
    False -> exists but not imported yet
    'Module X doesn't exist.' -> if module does not exist
    """
    import importlib.util, inspect
    frame = inspect.currentframe().f_back
    caller_globals = frame.f_globals
    if module_name in caller_globals:
        return True
    spec = importlib.util.find_spec(module_name)
    if spec:
        return False
    return f"Module {module_name} doesn't exist."

def vcompat(module_name, python_version=None):
    """
    Checks if a module is compatible with a python version, if
a version was given. If not given, returns any potential problems
for Pythons versions 2.0 through 3.12. Any typed Python version higher
than 3.12 works as 3.12 in the function.
    """
    COMPAT_RULES = {
        # === Python 2.0-2.7 Features ===
        "print": {"removed_in": "3.0", "note": "Python 2 print statement not valid in Python 3+"},
        "print>>": {"removed_in": "3.0", "note": "Python 2 print chevron syntax removed"},
        "xrange": {"removed_in": "3.0", "note": "Use range() in Python 3"},
        "raw_input": {"removed_in": "3.0", "note": "Use input() in Python 3"},
        "unicode": {"removed_in": "3.0", "note": "Use str in Python 3"},
        "long": {"removed_in": "3.0", "note": "long type merged into int"},
        "basestring": {"removed_in": "3.0", "note": "basestring removed, use str"},
        "apply": {"removed_in": "3.0", "note": "apply() removed, call function directly"},
        "execfile": {"removed_in": "3.0", "note": "execfile() removed, use exec()"},
        "reload": {"removed_in": "3.0", "note": "reload() moved to importlib"},
        "coerce": {"removed_in": "3.0", "note": "coerce() removed"},
        "file": {"removed_in": "3.0", "note": "file type removed, use open()"},
        
        # Python 2.2+ (generators)
        "generators": {"added_in": "2.2", "note": "Generators and yield added"},
        
        # Python 2.3+ (new features)
        "enumerate": {"added_in": "2.3", "note": "enumerate() function added"},
        "boolean": {"added_in": "2.3", "note": "bool type added"},
        
        # Python 2.4+ (decorators, generator expressions)
        "decorators": {"added_in": "2.4", "note": "Function decorators @ added"},
        "generator_expressions": {"added_in": "2.4", "note": "Generator expressions added"},
        
        # Python 2.5+ (with statement, conditional expressions)
        "with_statement": {"added_in": "2.5", "note": "with statement added"},
        "conditional_expressions": {"added_in": "2.5", "note": "x if condition else y syntax added"},
        
        # Python 2.6+ (format strings, class decorators)
        "str.format": {"added_in": "2.6", "note": "str.format() method added"},
        "class_decorators": {"added_in": "2.6", "note": "Class decorators added"},
        
        # Python 2.7+ (dictionary comprehensions, set literals)
        "dict_comprehensions": {"added_in": "2.7", "note": "Dictionary comprehensions added"},
        "set_literals": {"added_in": "2.7", "note": "Set literals {1,2,3} added"},
        
        # === Python 3.0+ Breaking Changes ===
        "exec": {"changed_in": "3.0", "note": "exec is a function, not a statement"},
        "print_function": {"changed_in": "3.0", "note": "print is a function, not a statement"},
        
        # Module renames (Python 3.0)
        "ConfigParser": {"removed_in": "3.0", "note": "Renamed to configparser"},
        "cPickle": {"removed_in": "3.0", "note": "Renamed to pickle"},
        "StringIO": {"removed_in": "3.0", "note": "Use io.StringIO"},
        "Queue": {"removed_in": "3.0", "note": "Renamed to queue"},
        "SocketServer": {"removed_in": "3.0", "note": "Renamed to socketserver"},
        "Tkinter": {"removed_in": "3.0", "note": "Renamed to tkinter"},
        "urllib2": {"removed_in": "3.0", "note": "Renamed to urllib"},
        
        # Python 3.1+ features
        "importlib": {"added_in": "3.1", "note": "importlib module added"},
        "ordered_dict": {"added_in": "3.1", "note": "collections.OrderedDict added"},
        
        # Python 3.2+ features
        "concurrent.futures": {"added_in": "3.2", "note": "concurrent.futures module added"},
        "argparse": {"added_in": "3.2", "note": "argparse added to stdlib"},
        
        # Python 3.3+ features
        "yield from": {"added_in": "3.3", "note": "yield from syntax added"},
        "venv": {"added_in": "3.3", "note": "venv module added"},
        "faulthandler": {"added_in": "3.3", "note": "faulthandler module added"},
        "ipaddress": {"added_in": "3.3", "note": "ipaddress module added"},
        
        # Python 3.4+ features
        "asyncio": {"added_in": "3.4", "note": "asyncio module added"},
        "enum": {"added_in": "3.4", "note": "enum module added"},
        "pathlib": {"added_in": "3.4", "note": "pathlib module added"},
        
        # Python 3.5+ features
        "async": {"changed_in": "3.5", "note": "'async' became a reserved keyword"},
        "await": {"changed_in": "3.5", "note": "'await' became a reserved keyword"},
        "typing": {"added_in": "3.5", "note": "typing module added"},
        "@ operator": {"added_in": "3.5", "note": "Matrix multiplication operator @ added"},
        
        # Python 3.6+ features
        "fstrings": {"added_in": "3.6", "note": "f-string syntax added"},
        "secrets": {"added_in": "3.6", "note": "secrets module added"},
        "underscore_literals": {"added_in": "3.6", "note": "1_000_000 numeric literal syntax"},
        
        # Python 3.7+ features
        "async/await": {"changed_in": "3.7", "note": "async/await became proper keywords"},
        "dataclasses": {"added_in": "3.7", "note": "dataclasses module added"},
        "contextvars": {"added_in": "3.7", "note": "contextvars module added"},
        
        # Python 3.8+ features
        "walrus": {"added_in": "3.8", "note": "Walrus operator := added"},
        "positional_only": {"added_in": "3.8", "note": "Positional-only parameters / added"},
        "fstring=": {"added_in": "3.8", "note": "f-string = debugging syntax added"},
        
        # Python 3.9+ features
        "dict_union": {"added_in": "3.9", "note": "Dict union | operator added"},
        "str_removeprefix": {"added_in": "3.9", "note": "str.removeprefix/removesuffix added"},
        "zoneinfo": {"added_in": "3.9", "note": "zoneinfo module added"},
        
        # Python 3.10+ features
        "match": {"added_in": "3.10", "note": "Structural pattern matching added"},
        "union_operator": {"added_in": "3.10", "note": "X | Y union type syntax added"},
        
        # Python 3.11+ features
        "exception_groups": {"added_in": "3.11", "note": "ExceptionGroups and except* added"},
        "tomllib": {"added_in": "3.11", "note": "tomllib module added"},
        
        # Python 3.12+ features
        "fstring_debug": {"added_in": "3.12", "note": "Enhanced f-string debugging"},
        "type_parameter_syntax": {"added_in": "3.12", "note": "New type parameter syntax"},
        
        # === Critical Deprecations ===
        "cgi": {"deprecated_in": "3.11", "removed_in": "3.13", "note": "cgi module deprecated"},
        "distutils": {"deprecated_in": "3.10", "removed_in": "3.12", "note": "distutils deprecated"},
        "imp": {"deprecated_in": "3.4", "removed_in": "3.12", "note": "imp module deprecated"},
        "asyncore": {"deprecated_in": "3.6", "note": "asyncore module deprecated"},
        "asynchat": {"deprecated_in": "3.6", "note": "asynchat module deprecated"},
        
        # === Syntax Changes ===
        "raise Exception, args": {"removed_in": "3.0", "note": "Old raise syntax removed"},
        "except Exception, e": {"removed_in": "3.0", "note": "Old except syntax removed"},
        "backticks": {"removed_in": "3.0", "note": "Backticks for repr() removed"},
        "<>": {"removed_in": "3.0", "note": "<> operator removed, use !="},
        
        # === Standard Library Changes ===
        "thread": {"removed_in": "3.0", "note": "thread module renamed to _thread"},
        "dummy_thread": {"removed_in": "3.0", "note": "dummy_thread module removed"},
        "anydbm": {"removed_in": "3.0", "note": "anydbm module removed"},
        "dbhash": {"removed_in": "3.0", "note": "dbhash module removed"},
        "dumbdbm": {"removed_in": "3.0", "note": "dumbdbm module removed"},
        "gdbm": {"removed_in": "3.0", "note": "gdbm module removed"},
        "whichdb": {"removed_in": "3.0", "note": "whichdb module removed"},
        "bsddb": {"removed_in": "3.0", "note": "bsddb module removed"},
        "md5": {"removed_in": "3.0", "note": "md5 module removed, use hashlib"},
        "sha": {"removed_in": "3.0", "note": "sha module removed, use hashlib"},
        "crypt": {"removed_in": "3.0", "note": "crypt module removed"},
        "popen2": {"removed_in": "3.0", "note": "popen2 module removed"},
        "commands": {"removed_in": "3.0", "note": "commands module removed, use subprocess"},
    }

    warnings = []
    target = version.parse(str(python_version)) if python_version else None

    try:
        spec = importlib.util.find_spec(module_name)
        if not spec or not spec.origin or not spec.origin.endswith(".py"):
            warnings.append("No source file (.py) found for static analysis.")
        else:
            with open(spec.origin, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Tokenize to ignore comments/docstrings
            tokens = tokenize.generate_tokens(io.StringIO(content).readline)
            words = [tok.string for tok in tokens if tok.type == tokenize.NAME]
            full_content_lower = content.lower()

            # Check each compatibility rule
            for key, rule in COMPAT_RULES.items():
                if (key in words) or (key in full_content_lower):
                    if target:
                        # Check if feature was removed
                        if "removed_in" in rule and target >= version.parse(rule["removed_in"]):
                            warnings.append(f"REMOVED: {key} - {rule['note']}")
                        # Check if feature was changed
                        elif "changed_in" in rule and target >= version.parse(rule["changed_in"]):
                            warnings.append(f"CHANGED: {key} - {rule['note']}")
                        # Check if feature was added after target
                        elif "added_in" in rule and target < version.parse(rule["added_in"]):
                            warnings.append(f"UNAVAILABLE: {key} - Added in {rule['added_in']}")
                        # Check if feature is deprecated
                        elif "deprecated_in" in rule and target >= version.parse(rule["deprecated_in"]):
                            if "removed_in" in rule and target < version.parse(rule["removed_in"]):
                                warnings.append(f"DEPRECATED: {key} - {rule['note']}")
                    else:
                        # Generic warnings without target version
                        if "removed_in" in rule:
                            warnings.append(f"[Removed {rule['removed_in']}] {key} - {rule['note']}")
                        elif "changed_in" in rule:
                            warnings.append(f"[Changed {rule['changed_in']}] {key} - {rule['note']}")
                        elif "added_in" in rule:
                            warnings.append(f"[Added {rule['added_in']}] {key} - {rule['note']}")
                        elif "deprecated_in" in rule:
                            warnings.append(f"[Deprecated {rule['deprecated_in']}] {key} - {rule['note']}")

            # Advanced AST-based syntax checks
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    # Python 2 print statement
                    if hasattr(ast, "Print") and isinstance(node, ast.Print):
                        warnings.append("PY2_SYNTAX: Python 2 print statement (invalid in Python 3)")
                    # Python 2 exec statement  
                    if hasattr(ast, "Exec") and isinstance(node, ast.Exec):
                        warnings.append("PY2_SYNTAX: Python 2 exec statement (exec() is a function in Python 3)")
                    # Check for walrus operator (3.8+)
                    if isinstance(node, ast.NamedExpr) and target and target < version.parse("3.8"):
                        warnings.append("SYNTAX: Walrus operator := requires Python 3.8+")
                    # Check for match statement (3.10+)
                    if hasattr(ast, "Match") and isinstance(node, ast.Match) and target and target < version.parse("3.10"):
                        warnings.append("SYNTAX: Match statement requires Python 3.10+")
            except SyntaxError as e:
                warnings.append(f"SYNTAX_ERROR: Could not parse - {e}")

            # String pattern checks for syntax features
            if "yield from" in content and target and target < version.parse("3.3"):
                warnings.append("SYNTAX: 'yield from' requires Python 3.3+")
            if "async def" in content and target and target < version.parse("3.5"):
                warnings.append("SYNTAX: 'async def' requires Python 3.5+")
            if "await " in content and target and target < version.parse("3.5"):
                warnings.append("SYNTAX: 'await' requires Python 3.5+")
            if ":=" in content and target and target < version.parse("3.8"):
                warnings.append("SYNTAX: Walrus operator ':=' requires Python 3.8+")
            if "match " in content and "case " in content and target and target < version.parse("3.10"):
                warnings.append("SYNTAX: Pattern matching requires Python 3.10+")
            if "f\"" in content or "f'" in content and target and target < version.parse("3.6"):
                warnings.append("SYNTAX: f-strings require Python 3.6+")
            if "_" in content and any(c.isdigit() for c in content) and "1_000" in content and target and target < version.parse("3.6"):
                warnings.append("SYNTAX: Underscore in numeric literals requires Python 3.6+")

        if not warnings:
            warnings.append("No compatibility issues detected for target version.")

    except ModuleNotFoundError:
        warnings.append(f"Module '{module_name}' not found.")
    except Exception as e:
        warnings.append(f"Analysis error: {e}")

    # Output results
    print(f"Compatibility Report for: {module_name}")
    print(f"Target Python Version: {python_version if python_version else 'All versions'}")
    print(f"Warnings Found: {len(warnings)}")
    print("-" * 50)
    
    for i, warning in enumerate(warnings, 1):
        print(f"{i}. {warning}")
