def list_importall():
    """Return the list of modules that import_all() would import."""
    return modules

def modules_loaded():
    """Show how many modules are currently loaded in sys.modules."""
    return len(sys.modules)

def imported():
    """Show all modules imported since ModX loaded (user + ModX + dependencies)."""
    current = set(sys.modules.keys())
    new_since = current - _initial_modules

    # Filter out modx internals and noise
    filtered_modules = set()
    for module_name in new_since:
        if (module_name == 'modx' or 
            module_name.startswith('modx.') or
            module_name.startswith('test.') or
            module_name.startswith('_test') or
            module_name in ['__main__', 'sys', 'builtins']):
            continue
        filtered_modules.add(module_name)

    sorted_modules = sorted(filtered_modules)
    print("Modules imported after ModX load (user + ModX + dependencies):")
    for name in sorted_modules:
        print("-", name)
    print(f"\nTotal modules imported after ModX load: {len(sorted_modules)}")


def modx_imported():
    """Show ONLY the modules directly imported via ModX functions."""
    shown = sorted(_imported_by_modx)
    print("Modules imported directly via ModX (excluding dependencies):")
    for name in shown:
        print("-", name)
    print(f"\nTotal modules imported via ModX: {len(shown)}")
    
def nonimported():
    """Return a list of most STANDARD LIBRARY
modules that have NOT been imported yet."""
    # Get all known standard library modules from our master list
    all_stdlib_modules = set(modules)
    
    # Add built-in modules
    all_stdlib_modules.update(sys.builtin_module_names)
    
    # Filter out modules that are already imported
    unimported = []
    for module_name in all_stdlib_modules:
        if module_name not in sys.modules:
            unimported.append(module_name)
    
    return sorted(unimported)
