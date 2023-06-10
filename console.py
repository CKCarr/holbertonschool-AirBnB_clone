#!/usr/bin/python3
"""Module 6. Console 0.0.1"""
import cmd
import shlex  # Used to handle arguments with spaces in them.
import models

class HBNBCommand(cmd.Cmd):
    """class HBNB inherits from cmd.Cmd, define
    methods and our own command-line applications"""

    prompt = '(hbnb) '
    # Defining a custom prompt attribute

    def __init__(self):
        super().__init__()
        # self.storage = FileStorage() 

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance = storage.get("BaseModel", args[1])
            if not instance:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if not storage.delete("BaseModel", args[1]):
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class, or all
        instances if no class name is provided."""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            instances = storage.all("BaseModel" if len(args) > 0 else None)
            for instance in instances.values():
                print(instance)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating an attribute."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print

if __name__ == '__main__':
    HBNBCommand().cmdloop()
