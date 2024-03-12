#!/usr/bin/env python3
"""
A module that defines the class HBNBCommand
"""

from models.base_model import BaseModel
from datetime import datetime
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

    prompt = "(hbnb) "

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
            class_model = globals()[arg]
        except KeyError:
            print("** class doesn't exist **")
            return


        new_instance = class_model()
        #new_id = str(uuid.uuid4())
        #settattr(new_instance, "id", new_id)

        storage.new(new_instance)
        new_instance.save()

        print(new_instance.id)

    def check_erro(self, arg):
        """"""

        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return

        class_name = arg[0]

        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]

        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return


    def do_show(self, arg):
        """
        Save instance data to a JSON file.
        """
        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return

        class_name = arg[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]

        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)

        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """"""
        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return

        class_name = arg[0]

        if class_name not in globals():
            print("** class doesn't exist **")

        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]

        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)

        if instance:
            del storage.all()[key]
            storage.save()
        else:
            print("no instance found")

    def do_all(self, arg):
        """"""
        instances = []

        if len(arg) < 1:
            var = storage.all().values()
            #instances = [(str(instance) for instance in storage.all().values())]
            for obj in var:
                class_name = f"[{obj['__class__']}]"
                del obj['__class__']
                obj_model = f"{class_name} ({obj['id']}) {str(obj)}"
                instances.append(obj_model)
        else:
            class_name = arg.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            for instance in storage.all().values():
                class_name = f"[{instance['__class__']}]"
                del instance['__class__']
                instance_id = f"({instance['id']})"
                instance_attr = str(instance)
                instance_model = f"{class_name} {instance_id} {instance_attr}"
                instances.append(instance_model)
        print(instances)

    def do_update(self, arg):
        """"""

        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return
        class_name = arg[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]
        key = class_name + '.' + instance_id
        every_instance = storage.all()

        if key not in every_instance:
            print("** no instance found **")
            return

        instance = every_instance[key]

        if len(arg) < 3:
            print("** attribute name missing **")
            return

        attribute_name = arg[2]

        if len(arg) < 4:
            print("** value missing **")
            return

        attribute_value = arg[3]

        if len(arg) > 4:
            return

        if hasattr(instance, attribute_name):
            if attribute_name == "id" or attribute_name == "created_at" or attribute_name == "updated_at":
                return
            attribute_value = type(getattr(instance, attribute_name))(attribute_value)
            try:
                setattr(instance, attribute_name, attribute_value)
                storage.save()
            except AttributeError:
                pass
            except ValueError:
                pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
