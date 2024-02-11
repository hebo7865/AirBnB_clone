#!/usr/bin/python3
"""The command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Interpreter class."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF to quit the program."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Handle empty line."""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
