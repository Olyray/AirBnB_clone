#!/usr/bin/python3
"""
console module
"""
import cmd
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User

CLASSES = [
        "BaseModel",
        "User"
]


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
            elif line == "User":
                new_instance = User()
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
            if commands[0] not in CLASSES:
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
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        the_dict = storage.all()
        if line:
            commands = line.split()
            if commands[0] not in CLASSES:
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
        Prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        if line == "":
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        elif line == "BaseModel":
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                if "BaseModel" in obj_id:
                    print(all_objs[obj_id])
        elif line == "User":
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                if "User" in obj_id:
                    print(all_objs[obj_id])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        the_dict = storage.all()
        if line:
            commands = line.split()
            if commands[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            elif commands[0] + "." + commands[1] not in the_dict:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            elif len(commands) > 4:
                commands = commands[:4]
            else:
                setattr(
                    the_dict[commands[0] + "." + commands[1]],
                    commands[2],
                    ast.literal_eval(commands[3]),
                )
                storage.save()
        else:
            print("** class name missing **")

    def do_EOF(self, line):
        """handles EOF"""
        return True

    def do_quit(self, line):
        """
        Quits command to exit the program
        """
        return True

    def emptyline(self):
        """empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
