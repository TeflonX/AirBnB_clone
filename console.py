#!/usr/bin/python3
"""
a program called console.py that contains the entry point of the
command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the command interpreter at EOF (Ctrl + D)
        """
        return True

    def emptyline(self):
        """
        Does nothing for an empty line
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
