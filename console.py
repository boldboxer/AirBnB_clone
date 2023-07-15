#!/usr/bin/python3
"""
Entry point of the command intepreter
used for CRUD operations
"""

import cmd
from models import storage
from models.base_model import  BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """The command shell processor"""

    prompt = "(hbnb) "

    def help_help(self):
        """Help command describes a specific cmd"""
        print("Describes the function of a given command")

    def emptyline(self):
        """Does nothing when an empty line is encountered"""
        pass

    def do_quit(self, line):
        """Quit command to exit program"""
        return True;

    def do_EOF(self, line):
        """ End_of_file command to terminate the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
