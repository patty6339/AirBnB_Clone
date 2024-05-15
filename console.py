#!/usr/bin/python3
""" This module is the entry point of the program"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command exits the program."""
        print()
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
