#!/usr/bin/python3
"""
console for the module
"""

import cmd
import json
from models.base_model import BaseModel
import models
import uuid
import os.path
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Goodbye!")
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("Goodbye!")
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        filename = "{}.json".format(class_name)
        if not os.path.isfile(filename):
            print("** no instance found **")
            return
        with open(filename, "r") as f:
            instances = f.readlines()
        found = False
        for instance in instances:
            instance = json.loads(instance)
            if instance['id'] == instance_id:
                print(instance)
                found = True
                break
        if not found:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist ")
            return
        if len(args) == 1:
            print(" instance id missing ")
            return
        instance_id = args[1]
        file_name = class_name + "." + instance_id + ".json"
        if not os.path.exists(file_name):
            print(" no instance found **")
            return
        os.remove(file_name)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
