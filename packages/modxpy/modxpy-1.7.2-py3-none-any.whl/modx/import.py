def import_all():
    """Import almost every module in Python that is given when downloading Python."""
    import builtins
    caller_globals = globals()
    builtins.__import__ = _original_import
    success = []
    failed = []
    try:
        for m in modules:
            try:
                # Import AND add to caller's globals
                module_obj = importlib.import_module(m)
                caller_globals[m] = module_obj
                _imported_by_modx.add(m)
                success.append(m)
            except Exception as e:
                failed.append((m, str(e)))
    finally:
        builtins.__import__ = _tracking_import
    
    # Show results
    print(f"import_all() Results:")
    print(f"SUCCESS: {len(success)} modules")
    print(f"FAILED: {len(failed)} modules")
    if failed:
        print("\nFailed imports:")
        for mod, error in failed[:10]:  # Show first 10 failures
            print(f"   {mod}: {error}")
        if len(failed) > 10:
            print(f"   ... and {len(failed) - 10} more")

def import_random(n):
    """Import n random stdlib modules and track them."""
    import builtins
    caller_globals = globals()
    chosen = random.sample(modules, min(n, len(modules)))
    builtins.__import__ = _original_import
    success = []
    failed = []
    try:
        for m in chosen:
            try:
                # Import AND add to caller's globals
                module_obj = importlib.import_module(m)
                caller_globals[m] = module_obj
                _imported_by_modx.add(m)
                success.append(m)
            except Exception as e:
                failed.append((m, str(e)))
    finally:
        builtins.__import__ = _tracking_import
    
    # Show results
    print(f" import_random({n}) Results:")
    print(f" REQUESTED: {len(chosen)} modules")
    print(f" SUCCESS: {len(success)} modules") 
    print(f" FAILED: {len(failed)} modules")
    if failed:
        print("\nFailed imports:")
        for mod, error in failed:
            print(f"   {mod}: {error}")
    
    return success


def import_external():
    """Import all installed third-party modules (not in stdlib list)."""
    import builtins
    caller_globals = globals()
    stdlib_set = set(modules) | set(sys.builtin_module_names)
    builtins.__import__ = _original_import
    success = []
    failed = []
    try:
        for finder, name, ispkg in pkgutil.iter_modules():
            if name not in stdlib_set:
                try:
                    # Import AND add to caller's globals
                    module_obj = importlib.import_module(name)
                    caller_globals[name] = module_obj
                    _imported_by_modx.add(name.partition('.')[0])
                    success.append(name)
                except Exception as e:
                    failed.append((name, str(e)))
    finally:
        builtins.__import__ = _tracking_import
    
    # Show results
    print(f" import_external() Results:")
    print(f" SUCCESS: {len(success)} third-party modules")
    print(f" FAILED: {len(failed)} modules")
    if failed:
        print("\nFirst 10 failures:")
        for mod, error in failed[:10]:
            print(f"   {mod}: {error}")

def import_screen():
    """Import common screen/GUI/game modules if available."""
    import builtins
    caller_globals = globals()
    screen_modules = ['pygame', 'pyglet', 'arcade', 'tkinter', 'turtle']
    builtins.__import__ = _original_import
    success = []
    failed = []
    try:
        for m in screen_modules:
            try:
                # Import AND add to caller's globals
                module_obj = importlib.import_module(m)
                caller_globals[m] = module_obj
                _imported_by_modx.add(m)
                success.append(m)
            except Exception as e:
                failed.append((m, str(e)))
    finally:
        builtins.__import__ = _tracking_import
    
    # Show results
    print(f" import_screen() Results:")
    print(f" SUCCESS: {len(success)} GUI modules")
    print(f" FAILED: {len(failed)} modules")
    if failed:
        print("\nFailed imports:")
        for mod, error in failed:
            print(f"   {mod}: {error}")

def import_letter(letter):
    """Import every stdlib module from ModX 'modules' list whose name starts with given letter."""
    import builtins
    caller_globals = globals()
    letter = letter.lower()
    success = []
    failed = []
    builtins.__import__ = _original_import
    try:
        for m in modules:
            if m.lower().startswith(letter):
                try:
                    # Import AND add to caller's globals
                    module_obj = importlib.import_module(m)
                    caller_globals[m] = module_obj
                    _imported_by_modx.add(m)
                    success.append(m)
                except Exception as e:
                    failed.append((m, str(e)))
    finally:
        builtins.__import__ = _tracking_import
    
    # Show results
    print(f" import_letter('{letter}') Results:")
    print(f" SUCCESS: {len(success)} modules starting with '{letter}'")
    print(f" FAILED: {len(failed)} modules")
    if failed:
        print("\nFailed imports:")
        for mod, error in failed:
            print(f"   {mod}: {error}")
    
    return success