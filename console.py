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
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
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
        Prints the string representation of an instance based on the class name and id.
        """
        #Call storage.all to access the persistent dict representation
        the_dict = storage.all()
        #if there is a command after "show"
        if line:
            #split the line into its constituent parts
            commands = line.split()
            #Check that the right class is called
            if commands[0] != "BaseModel":
                print("** class doesn't exist **")
            #Check for an instance id.
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                #print the string representation if it's available
                try:
                    print(the_dict["{}.{}".format(commands[0], commands[1])])
                except KeyError:
                    print("** no instance found **")
        else:
            #print the appropriate error message
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
