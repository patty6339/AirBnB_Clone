#!/usr/bin/python3
""" This module is the entry point of the program"""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command exits the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_quit(self):
        """Help information for quit command"""
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """Help information for EOF command"""
        print("Exit - command interpreter by pressing Ctrl+D.")

    def emptyline(self):
        """Do nothing on empty line input"""
        pass

    def do_help(self, arg):
        """Display help for a given command. USAGE: help [command]"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        print("Created new instance:", new_instance.id)  # Debug print
        storage.reload()
        print("Storage after create and reload:", storage.all())  # Debug print

    def do_show(self, arg):
        """
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
        """Deletes an instance based on the class name and id."""
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
        """
        Parse the argument to extract class names.
        """
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
        storage.save()  # Ensure the storage is saved



if __name__ == '__main__':
    HBNBCommand().cmdloop()