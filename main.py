# PYFodlers
# Developed by Lewis L. Foster in December 2021

import os
import sys
import logging

import utils

logger = logging.getLogger("PYFolders")
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')


print("""
 ______   _______     _     _               
|  _ \ \ / /  ___|__ | | __| | ___ _ __ ___ 
| |_) \ V /| |_ / _ \| |/ _` |/ _ \ '__/ __|
|  __/ | | |  _| (_) | | (_| |  __/ |  \__ \\
|_|    |_| |_|  \___/|_|\__,_|\___|_|  |___/
by Lewis L. Foster (December 2021)

""")

def main():
    try:
        foldroot = sys.argv[1]
    except IndexError:
        logger.fatal(f"{utils.console_colours.red}No foldroot provided{utils.console_colours.white}")
        return 1

    if not os.path.isdir(foldroot):
        logger.fatal(f"{utils.console_colours.red}Foldroot provided is not a valid folder{utils.console_colours.white}")
        return 1

    foldrootpath = os.path.realpath(foldroot)

    if not foldroot.startswith("FR:"):
        logger.fatal(f"{utils.console_colours.red}Foldroot provided is not a valid PYFolders foldroot{utils.console_colours.white}")
        return 1

    logger.info(f"Foldroot path is: {foldrootpath}")

    os.chdir(foldrootpath)

    FR = utils.objects.Foldroot.get_root(foldrootpath)

    if not os.path.isdir(FR.mainfunc):
        logger.fatal(f"{utils.console_colours.red}PYFolders main function is invalid{utils.console_colours.white}")
        return 1

    main_function = utils.parse_folder_contents(FR)

    logger.info(f"Executing main: {FR.mainfunc}")
    print("\n============ Program ============\n")
    exec(main_function)
    print("\n======== End Of Program =========\n")


if __name__ == "__main__":
    main()
