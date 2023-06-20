#!/usr/bin/python3
"""Module that contains the code for the command
interpreter"""

import cmd
import models
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """class HBNB inherits from cmd.Cmd, define
    methods and our own command-line applications"""
    # Defining a custom prompt attribute
    prompt = '(hbnb) '

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """Exit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """
        Method that creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id.
        """
        if len(arg) < 1:
            print("** class name missing **")
        elif arg in classes.keys():
            new = classes[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Method that prints the string representation of
        an object based on the class name and id.
        """
        args2 = args.split(' ')
        if args == "":
            print("** class name missing **")
        elif args2[0] in classes.keys():
            if len(args2) < 2:
                print("** instance id missing **")
            else:
                item_search = args2[0] + "." + args2[1]
                item_all = storage.all()  # retrieve all objects from storage
                if item_search in item_all:
                    print(item_all[item_search])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the
        class name and id, and saves the change into
        the JSON file.
        """
        args2 = args.split(' ')
        if args == "":
            print("** class name missing **")
        elif args2[0] in classes.keys():
            if len(args2) < 2:
                print("** instance id missing **")
            else:
                item_search = args2[0] + "." + args2[1]
                item_all = storage.all()
                if item_search in item_all:
                    del item_all[item_search]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Method that prints a string representation
        of all objects based on the class name given
        or all objects if no class name given.
        """
        if "." not in arg:
            print("** Unknown syntax: {}.all()".format(arg))
            return
        class_name = arg.split(".")[0]
        if class_name not in classes.keys():
            print("** class doesn't exist **")
            return

        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                print(str(obj))

    def do_update(self, args):
        """
        This method updates an instance based on the class
        name and id by adding or updating an attribute..
        """
        args2 = args.split(' ')
        if not args:
            print("** class name missing **")
        elif len(args2) < 2:
            print("** instance id missing **")
        elif len(args2) < 3:
            print("** attribute name missing **")
        elif len(args2) < 4:
            print("** value missing **")
        elif args2[0] not in classes:
            print("** class doesn't exist **")
        else:
            item_search = args2[0] + "." + args2[1]
            item_all = storage.all()
            if item_search in item_all:
                setattr(storage.all()[item_search],
                        args2[2], args2[3].strip('\'"'))
                storage.save()
            else:
                print("** no instance found **")


    def do_count(self, args):
        """ retrieve the number of instances of a class """
        if "." not in arg:
            print("** Unknown syntax: {}.count()".format(arg))
            return
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = arg.split(".")[0]
        if class_name not in classes.keys():
            print("** class doesn't exist **")
            return
        instance_count = 0
        for obj_instance in storage.all().values():
            if obj_instance.__class__.__name__ == class_name:
                instance_count += 1
            print(instance_count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
