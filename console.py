#!/usr/bin/python3
"""Defines HBnB console."""
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
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

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
