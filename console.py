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
        else:
            try:
                cls = globals()[arg]
                obj = cls()
                models.storage.new(obj)
                models.storage.save()
                print(obj.id)
            except KeyError:
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
        """to checkk"""
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
            if argl[0] not in globals():
                print("** class doesn't exist **")
            else:
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
Updates an instance based on the class name and id
        """
        instances = models.storage.all()
        argl = arg.split()

        if len(argl) == 0:
            print("** class name missing **")
        elif len(argl) == 1:
            if argl[0] not in globals():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(argl) == 2 and argl[0] in globals():
            key = "{}.{}".format(argl[0], argl[1])
            instance = instances.get(key)
            if not instance:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(argl) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            instance = instances.get(key)
            attribute = argl[2]
            if hasattr(instance, attribute):
                value = argl[3]
                setattr(instance, attribute, value)
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
