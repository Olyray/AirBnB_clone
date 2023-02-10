#!/usr/bin/python3
"""
console module
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Class
    """

    prompt = "(hbnb)"

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if line:
            if line == "BaseModel"
                new_instance = BaseModel()
                new_instance.save()
                print("{}".format(new_instance.id))
            else:
                print("** class doesn't exist **")
        else:
                print("** class name missing **")

    def do_EOF(self, line):
        """ handles EOF """
        return True

    def do_quit(self, line):
        """
        Quits command to exit the program
        """
        return True

    def emptyline(self):
        """ empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
