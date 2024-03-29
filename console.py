#!/usr/bin/python3
"""Defines HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
