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
            if line == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print("{}".format(new_instance.id))
            else:
                print("** class doesn't exist **")
        else:
                print("** class name missing **")

    def do_show(self, line):
        """
         Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

            If the class name is missing, print ** class name missing ** (ex: $ show)
            If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
            If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
            If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)

        """
        the_dict = storage.all()
        if line:
            commands = line.split()
            if commands[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            elif the_dict["{}.{}".format(commands[0], commands[1])]:
                print ()


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
