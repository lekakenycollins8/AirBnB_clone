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
    all_methods = {'all', 'count', 'show', 'destroy', 'update'}

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
        """prints string representation of instances basedon class name"""
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
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = arg.strip().split()

        if not arg:
            print("** class name missing **")
        class_name = args[0]
        if class_name not in storage.allclasses():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        instance_dict = storage.all()[key]
        if len(args) < 3:
            print("** attributes name missing **")
            return
        if args[2].startswith("{") and args[-1].endswith("}"):
            attributes_dict = eval(" ".join(args[2:]))
            for attr_name, attr_value in attributes_dict.items():
                setattr(instance_dict, attr_name, attr_value)
        else:
            for i in range(2, len(args), 2):
                attribute_name = args[i]
                attribute_value = args[i + 1]
                setattr(instance_dict, attribute_name, attribute_value)
        storage.save()

    def do_count(self, arg):
        """counts instances of a class"""
        counter = 0
        for instance in storage.all().keys():
            cls_name, inst_id = instance.split(".")
            if arg == cls_name:
                counter += 1
        print(counter)


    def precmd(self, arg):
        """advanced command syntax
        Usage: <class name>.<command>(<id>)
        """
        args = arg.split(".", 1)
        if len(args) != 2:
            return arg
        class_name, remaining = args
        args = remaining.split("(", 1)
        
        command, args_part = args
        args_part = args_part.rstrip(")")
        id_, *argms = map(str.strip, args_part.split(","))

        if command not in HBNBCommand.all_methods:
            return arg
        if argms and argms[0].startswith("{") and argms[-1].endswith("}"):
            argms = " ".join(argms)
        else:
            argms = " ".join(argms).replace(",", "")
        return "{} {} {} {}".format(command, class_name, id_, argms)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

