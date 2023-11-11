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
        """
        Creates a new instance and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            obj = BaseModel()
            models.storage.new(obj)
            models.storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        argl = arg.split()

        if len(argl) == 0:
            print("** class name missing **")
        elif len(argl) == 1 and argl[0] not in globals():
            print("** class doesn't exist **")
        elif len(argl) == 1 and argl[0] in globals():
            print("** instance id missing **")
        elif len(argl) == 2 and argl[0] in globals():
            key = "{}.{}".format(argl[0], argl[1])
            instances = models.storage.all()
            instance = instances.get(key)
            if instance:
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
        elif len(argl) == 1 and argl[0] not in globals():
            print("** class doesn't exist **")
        elif len(argl) == 1 and argl[0] in globals():
            print("** instance id missing **")
        elif len(argl) == 2 and argl[0] in globals():
            key = "{}.{}".format(argl[0], argl[1])
            instances = models.storage.all()
            instance = instances.get(key)
            if instance:
                del instances[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        if arg:
            argl = arg.split()
            if len(argl) == 1 and argl[0] not in globals():
                print("** class doesn't exist **")
            elif len(argl) == 1 and argl[0] in globals():
                filtered_instances = []
                instances = models.storage.all().values()
                for obj in instances:
                    if obj.__class__.__name__ == argl[0]:
                        filtered_instances.append(obj.__str__())
                print(filtered_instances)
        else:
            instances = models.storage.all().values()
            print([obj.__str__() for obj in instances])

    def do_update(self, arg):
        """
        Update a class instance based on the given arguments.
        """
        argl = arg.split()
        objdict = models.storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in globals():
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            print("** value missing **")
            return False

        obj = objdict["{}.{}".format(argl[0], argl[1])]
        attribute = argl[2]
        value = argl[3]

        if hasattr(obj, attribute):
            attr_type = type(getattr(obj, attribute))
            setattr(obj, attribute, attr_type(value))
            models.storage.save()
        else:
            setattr(obj, attribute, value)
            models.storage.save()

    def emptyline(self):
        """
        Called when an empty line is entered. Override to do nothing.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
