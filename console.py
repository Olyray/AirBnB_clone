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
        Prints the string representation of an instance based
        on the class name and id.
        """
        the_dict = storage.all()
        if line:
            commands = line.split()
            if commands[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                try:
                    print(the_dict["{}.{}".format(commands[0], commands[1])])
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
		destroy: Deletes an instance based on the class name and id 
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        the_dict = storage.all()
        if line:
            commands = line.split()
            if commands[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                try:
                    del the_dict["{}.{}".format(commands[0], commands[1])]
                    storage.save()
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class name missing **")
    
    def do_all(self, line):
        """
		Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.

			The printed result must be a list of strings (like the example below)
			If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        """
        if line == "BaseModel" or line is None:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        else:
            print("** class doesn't exist **")

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
