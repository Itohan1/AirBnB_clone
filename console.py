#!/usr/bin/env python3
"""
A module that defines the class HBNBCommand
"""

from models.base_model import BaseModel
import cmd
import os
import json
import uuid
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Represent a class HBNBCommand that uses the command 
    interpreter
    """

    prompt = "(hbnb)"
    filepath = "file.json"

    def do_EOF(self, arg):
        """
        Handle end-of-file marker
        """

        return (True)

    def do_quit(self, arg):

        """
        Quit the command interpreter.
        """
        return (True)

    def do_help(self, arg):
        """
        Display help information for the command interpreter.
        """ 
        cmd.Cmd.do_help(self, arg)
            
    def emptyline(self):
        """
        Called when the user enters an empty line.
        """
        pass

    
    def onecmd(self, obj):
        """
        Execute a single command entered by the user.
        """
        
        if not obj.strip():
            return self.emptyline()
        return super().onecmd(obj)

    
    def help_quit(self):
        """
        Display help information for the quit command
        """
        print("Quit command to exit the program\n")

    
    def help_EOF(self):
        """
        Display help information for the EOF command.
        """
        pass

    def help_help(self):
        """
        Display help information for the help command.
        """
        return True

    def do_create(self, arg):
        """
        Create a new instance of a specified class.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            model_cls = globals()[arg]

        except KeyError:
            print("** class doesn't exist **")
            return

        storage.all()

        new_instance = model_cls()
        new_id = str(uuid.uuid4())
        setattr(new_instance, "id", new_id)
        
        self.save(new_instance)
        print(new_id)

    def save(self, arg):
        """
        Save instance data to a JSON file.
        """

        if os.path.isfile(HBNBCommand.filepath):
            with open(HBNBCommand.filepath, 'r') as file:
                data = json.load(file)
        else:
            data = {}

        instance_dict = arg.to_dict()

        data[arg.__class__.__name__ + "." + instance_dict["id"]] = instance_dict

        with open(HBNBCommand.filepath, 'w') as file:
            json.dump(data, file)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
