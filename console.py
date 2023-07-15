#!/usr/bin/python3
"""
Entry point of the command intepreter
used for CRUD operations
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The command shell processor"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit program"""
        return True;

    def do_EOF(self, line):
        """ End_of_file command to terminate the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
