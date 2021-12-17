import os

from . import console_colours
from . import objects


def parse_folder_contents(foldroot, folder_set = None):
    if folder_set is None:
        folder_set = foldroot.mainfunc
    os.chdir(folder_set)
    folder_commands = os.listdir()
    folder_commands.sort(key=lambda cmd: cmd[0])
    commands = ""
    for command in folder_commands:
        if len(os.listdir(command)) > 0:
            root_cmd = ":".join(command.split(":")[1:])

            cmds_to_add = parse_folder_contents(foldroot, command)
            cmds_to_add = cmds_to_add.split("\n")[1:]


            newcmds = ""
            for cmd in cmds_to_add:
                newcmds = newcmds + "\n    " + cmd

            commands = commands + "\n" + root_cmd + newcmds
        else:
            command = command.split(":")
            command = ":".join(command[1:])
            commands = commands + "\n" + command
    os.chdir("..")

    return commands

