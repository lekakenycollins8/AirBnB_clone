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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        instance_dict = storage.all()[key]
        if len(args) == 4:
            attribute = args[2]
            value = args[3]
            if attribute in storage.classes_attributes()[class_name]:
                value = storage.classes_attributes()[class_name]
                setattr(instance_dict, attribute, value)
                storage.save()

    def do_count(self, arg):
        """counts instances of a class"""
        counter = 0
        for instance in storage.all().keys():
            cls_name, inst_id = instance.split(".")
            if arg == cls_name:
                counter += 1
        print(counter)

    def parse_command(self, command):
        """Parse the command to extract class name, command, and ID."""
        pattern = r'^(\w+)\.(\w+)\(([^)]+)\)$'
        match = re.match(pattern, command)
        if match:
            class_name = match.group(1)
            command_name = match.group(2)
            args = match.group(3).split(',')
            return class_name, command_name, args
        else:
            return None, None, None

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        class_name, command_name, args = self.parse_command(line)
        if class_name and command_name and args:
            if command_name == 'show':
                # Call the show method
                self.do_show(f"{class_name} {' '.join(args)}")
            elif command_name == 'destroy':
                # Call the destroy method
                self.do_destroy(f"{class_name} {' '.join(args)}")
            elif command_name == 'update':
                # Call the update method
                self.do_update(f"{class_name} {' '.join(args)}")
            else:
                print("** Invalid command name **")
        else:
            print("** Invalid command syntax **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

