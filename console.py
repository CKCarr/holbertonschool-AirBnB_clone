#!/usr/bin/python3
"""Module 6. Console 0.0.1"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNB inherits from cmd.Cmd, define
    methods and our own command-line applications"""

    prompt = '(hbnb) '
    # Defining a custom prompt attribute

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
