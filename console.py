#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class inherits from Cmd class
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Creates a new instance and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = globals()[arg]()
            models.storage.new(obj)
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        argl = arg.split()

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in models.storage.all():
            print("** no instance found **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            instance = models.storage.all()[key]
            print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in models.storage.all():
            print("** no instance found **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        if arg and arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            instances = models.storage.all().values()
            if arg:
                filtered_instances = [obj.__str__() for obj in instances if obj.__class__.__name__ == arg]
                print(filtered_instances)
            else:
                print([obj.__str__() for obj in instances])

    def do_update(self, arg):
        """
        Update a class instance based on the given arguments.
        """
        argl = arg.split()
        objdict = models.storage.all()

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        elif len(argl) == 2:
            print("** attribute name missing **")
        elif len(argl) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            obj = objdict[key]
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

    def default(self, line):
        """
        Called on an input line when the command prefix is not recognized.
        """
        parts = line.split('.')
        if len(parts) == 2 and parts[0] in self.__classes and parts[1] == "all()":
            class_name = parts[0]
            all_instances = [str(obj) for obj in models.storage.all().values() if obj.__class__.__name__ == class_name]
            print(all_instances)
        elif len(parts) == 2 and parts[0] in self.__classes and parts[1] == "count()":
            count = 0
            class_name = parts[0]
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == class_name:
                    count+=1
            print(count)
        elif len(parts) == 2 and parts[0] in self.__classes and parts[1][0:4] == "show":
            if "{}.{}".format(parts[0], parts[1][6:-2]) not in models.storage.all():
                print("** no instance found **")
            else:
                key = "{}.{}".format(parts[0], parts[1][6:-2])
                instance = models.storage.all()[key]
                print(instance)
        elif len(parts) == 2 and parts[0] in self.__classes and parts[1][0:7] == "destroy":
            if "{}.{}".format(parts[0], parts[1][9:-2]) not in models.storage.all():
                print("** no instance found **")
            else:
                key = "{}.{}".format(parts[0], parts[1][9:-2])
                del models.storage.all()[key]
                models.storage.save()

        elif len(parts) == 2 and parts[0] in self.__classes and parts[1].split('(')[0] == "update":
            params = parts[1].split('(')[1].split(')')[0].split(',')
            if len(params) == 3:
                class_name, obj_id, attribute, value = parts[0], params[0].strip(), params[1].strip(), params[2].strip()
                key = "{}.{}".format(class_name, obj_id)
                obj = models.storage.all().get(key)
                if obj:
                    if hasattr(obj, attribute):
                        setattr(obj, attribute, type(getattr(obj, attribute))(value))
                        models.storage.save()
                    else:
                        setattr(obj, attribute, value)
                        models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** invalid number of arguments for update command **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
