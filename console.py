#!/usr/bin/python3
"""
a program called console.py that contains the entry point of the
command interpreter
"""


import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(hbnb) "
    rec_classes = ["BaseModel", "User", "City", "State", "Review", "Amenity"]

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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.rec_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(f"{args[0]}()")
            storage.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        arg_split = arg.split()
        if not arg_split:
            print('** class name missing **')
        else:
            class_name = arg_split[0]
            if class_name not in self.rec_classes:
                print("** class doesn't exist **")
            elif len(arg_split) < 2:
                print("** instance id missing **")
            else:
                obj_id = arg_split[1]
                key = f"{class_name}.{obj_id}"
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.rec_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = f"{class_name}.{obj.id}"
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        args = arg.split()
        if not args:
            for obj in storage.all().value():
                print(str(obj))
        elif args[0] not in self.rec_classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    print(str(obj))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.rec_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            key = f"{args[0]}.{obj_id}"
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(instance, attr_name, attr_value)
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
