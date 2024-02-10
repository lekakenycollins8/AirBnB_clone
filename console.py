#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage
import json
import re

class HBNBCommand(cmd.Cmd):
    """implements quit, EOF, help and prompt"""
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """does not execute empty line plus ENTER"""
        pass

    def do_create(self, arg):
        """creates a new instance o Base and all child classes"""
        class_name = arg.strip()
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in storage.allclasses():
            print("** class doesn't exist **")
            return
        if class_name in storage.allclasses():
            instance = storage.allclasses()[class_name]()
            instance.save()
            print(instance.id)
            return

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.strip().split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.allclasses():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all().keys():
            print(storage.all()[key])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and
        id (save the change into the JSON file)
        """
        args = arg.strip().split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.allclasses():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all().keys():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """prints string representation of instances based on not on class name"""
        if not arg:
            instances = storage.all().values()
        else:
            class_name = arg.split()[0]
            if class_name not in storage.allclasses():
                print("** class doesn't exist")
                return

            instances = [obj for obj in storage.all().values()if type
                    (obj).__name__ == class_name]
        str_instances = [str(obj) for obj in instances]
        print(str_instances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

