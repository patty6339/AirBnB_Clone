#!/usr/bin/python3
"""This module is the entry point of the program."""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from unittest.mock import patch
from io import StringIO


class HBNBCommand(cmd.Cmd):
    """Entry prompt of the program."""

    prompt = '(hbnb) '
    __classes = [
        "BaseModel",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
        "User"
    ]

    def do_quit(self, arg):
        """Quit command exits the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def help_quit(self):
        """Help information for quit command."""
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """Help information for EOF command."""
        print("Exit - command interpreter by pressing Ctrl+D.")

    def emptyline(self):
        """Do nothing on empty line input."""
        pass

    def do_help(self, arg):
        """Display help for a given command. USAGE: help [command]."""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """
        Create.

        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        # print("Created new instance:", new_instance.id)  # Debug print
        print(new_instance.id)
        storage.reload()
        # print("Storage after create & reload:", storage.all()) # Debug print

    def do_show(self, arg):
        """
        Show.

        Prints the string representation of
        an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        storage.reload()
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Delete.

        Removes an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        storage.reload()
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def parse(self, arg):
        """Parse the argument to extract class names."""
        curly_braces = re.search(r"\{(.*?)\}", arg)
        brackets = re.search(r"\[(.*?)\]", arg)
        if curly_braces is None:
            if brackets is None:
                return [i.strip(",") for i in arg.split()]
            else:
                lexer = arg.split(arg[:brackets.span()[0]])
                retl = [i.strip(",") for i in lexer]
                retl.append(brackets.group())
                return retl
        else:
            lexer = arg.split(arg[:curly_braces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())
            return retl

    def do_all(self, arg):
        """
        All.

        Prints all string representations of instances.
        """
        args = self.parse(arg)
        if args and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        storage.reload()
        instances = []
        for obj in storage.all().values():
            if not args or obj.__class__.__name__ == args[0]:
                instances.append(str(obj))

        print(instances)

    def do_update(self, args):
        """Update function."""
        args = args.split()
        if len(args) < 4:
            print("** attribute name missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        key = class_name + "." + instance_id
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return

        # Convert attribute_value to the correct type
        if hasattr(instance, attribute_name):
            current_value = getattr(instance, attribute_name)
            if isinstance(current_value, int):
                attribute_value = int(attribute_value)
            elif isinstance(current_value, float):
                attribute_value = float(attribute_value)
            elif isinstance(current_value, bool):
                attribute_value = attribute_value.lower() in ['true', '1']
        else:
            # If the attribute doesn't exist, add it as a string
            attribute_value = str(attribute_value)

        setattr(instance, attribute_name, attribute_value)
        instance.save()
        storage.save()  # Ensure storage is saved

    def help_update(self):
        """Help information for the update command."""
        print(
            "Updates an instance based on the class name "
            "and id by adding or updating an attribute."
        )
        print(
            "USAGE: update <class name> <id> "
            "<attribute name> <attribute value>"
        )
        print()

    def help_show(self):
        """Help information for the show command."""
        print('Show command to retrieve an object from a '
              'string representation')

    def do_count(self, class_name):
        """
        Count.

        Counts the number of instances of a given class.
        """
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)

    def default(self, line):
        """
        Call.

        Call on an input line when the
        command prefix is not recognized.
        In this case it will be used to handle
        <class name>.all() and
        <class name>.count() commands.
        """
        if line:
            inputs = line.split('.')
            if len(inputs) == 2:
                class_name, method_name = inputs
                method_name = method_name.strip('()')  # Strip parentheses
                if method_name == "all" and class_name in self.__classes:
                    self.do_all(class_name)
                elif method_name == "count" and class_name in self.__classes:
                    self.do_count(class_name)
                else:
                    print("*** Unknown syntax: {}".format(line))
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
