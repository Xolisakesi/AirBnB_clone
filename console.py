#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        argdict = {"all": self.do_all, "show": self.do_show, "destroy": self.do_destroy,
                   "count": self.do_count, "update": self.do_update}
        match = re.search(r"\.", arg)
        if match:
            argl = arg.split("(")
            cmd, args = argl[0], argl[1].strip(")")
            if cmd in argdict:
                return argdict[cmd](args)
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj = eval(arg)()
        print(obj.id)
        storage.save()

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id."""

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""

    def do_all(self, arg):
        """Display string representations of all instances of a given class."""
        # Same as original, unchanged

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""

    def do_update(self, arg):
        """Update a class instance of a given id with new attributes."""


if __name__ == "__main__":
    HBNBCommand().cmdloop()

