def easter_egg(passcode):
    "??????????"
    a= '''          #   #  #####  #       #        ##
          #   #  #      #       #       #  #
          #####  #####  #       #      #    #
          #   #  #      #       #       #  #
          #   #  #####  #####   #####    ##

      #           #   ##    ####    #      ###    #
       #    #    #   #  #   #   #   #      #  #   #
        #   #   #   #    #  ####    #      #  #   #
         # # # #     #  #   #  #    #      #  #   
          #   #       ##    #   #   #####  ###    #
     
                        #####     #
                       #     #   #
                       #     #  #
                        #####  #
                        ######
                        # #
                        # #
                       #  #
                       #  #
                       #  #
                         # #
                        #   #
                       #     #'''
    if passcode == "abc":
        print(a)
    else:
        print("...")
        sys.exit("!)@(#$&*%^&#R&#$)!!%$@&)#@*)^!$#&!%*^)!$@#)%!$")
        quit()
         

def modx_help():
    """
    Show full ModX help including all functions and example usage.
    """
    help_text = """
ModX — The Python Module Universe
=================================

Functions:
----------

import_all()
    Import almost every standard library module at once.
    Example: modx.import_all()

import_external()
    Import all installed third-party modules.
    Example: modx.import_external()

import_screen()
    Import common screen/GUI/game modules if available (pygame, turtle, tkinter, etc.).
    Example: modx.import_screen()

import_letter(letter)
    Import every standard library module starting with a given letter.
    Example: modx.import_letter('t')

import_random(n)
    Import n random standard library modules.
    Example: modx.import_random(5)

list_importall()
    Return a list of modules that import_all() would load.
    Example: modx.list_importall()

modules_loaded()
    Show how many total modules are currently loaded in sys.modules.
    Example: modx.modules_loaded()

dependencies()
    Show what other modules a specific module depends on without importing it.
    Example: modx.dependencies("random")

imported()
    Show ALL modules imported after ModX loaded (user + ModX + dependencies).
    Example: modx.imported()

modx_imported()
    Show ONLY the modules imported directly via ModX functions (excluding dependencies).
    Example: modx.modximported()

nonimported()
    Return a list of standard library modules not yet imported.
    Example: modx.nonimported()

info(module_name)
    Show information about a module.
    Example: modx.info('random')

search_modules(keyword)
    Search for modules whose names contain the keyword.
    Example: modx.search_modules('html')

is_imported(module_name)
    Check if a module is currently imported.
    Example: modx.isimported('random')

vcompat(module_name, python_version)
    Check if a module works with different Python versions
    Example: modx.vcompat('pygame')

modx_help()
    Show this help screen.
    Example: modx.modxhelp()
"""
    print(help_text)
