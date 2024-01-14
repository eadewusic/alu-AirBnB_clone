#!/usr/bin/python3
"""
This module contains the entry point for the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    
    commands:
    quit - exit the program
    EOF - exit the program
    """
    prompt = "(hbnb) "

    def do_help(self, arg: str) -> bool | None:
        '''
        Method to handle help command
        '''
        return super().do_help(arg)

    def emptyline(self) -> bool:
        '''
        Method to handle empty line
        '''
        pass

    def help_quit(self) -> None:
        '''
        Method to print help for quit command
        '''
        print("Quit command to exit the program")

    def do_quit(self, arg: str) -> bool:
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg: str) -> bool:
        """EOF command to exit the program."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
