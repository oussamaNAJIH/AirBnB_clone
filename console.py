#!/usr/bin/python3
"""
this module contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class inherits from Cmd class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
