#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """implements quit, EOF, help and prompt"""
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, arg):
        """EOF coammnd to exit the program"""
        return True

    def postcmd(self, stop, arg):
        """executes EOF"""
        if arg == "EOF":
            return True
        return stop

    def emptyline(self):
        """does not execute empty line plus ENTER"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

