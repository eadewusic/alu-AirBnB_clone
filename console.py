#!/usr/bin/python3
"""
This module contains the entry point for the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class inherits from cmd.Cmd and represents
    the command interpreter for the HBNB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when encountering the end-of-file (EOF).
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
