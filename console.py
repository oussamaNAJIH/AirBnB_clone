#!/usr/bin/python3
"""
this module contains the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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
    
    def do_create(self, arg):
        if not arg:
            print("** class name missing **")

        else:
            try:
                cls = models.classes[arg]
                obj = cls()
                models.storage.new(obj)
                models.storage.save()
                print(obj.id)
            except:
                print("** class doesn't exist **")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
