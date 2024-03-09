#!/usr/bin/env python3
""""""

from models.base_model import BaseModel
import cmd
import os
import json
import uuid

class HBNBCommand(cmd.Cmd):
    """"""

    prompt = "(hbnb) "
    filepath = "file.json"

    def do_EOF(self, arg):
        """"""

        return (True)

    def do_quit(self, arg):
        """"""

        return (True)

    def do_help(self, arg):
        """"""
        cmd.Cmd.do_help(self, arg)

    
    def emptyline(self):
        """"""
        pass

    def onecmd(self, obj):
        """"""

        if not obj.strip():
            return (self.emptyline())
        return super().onecmd(obj)

    def help_quit(self):
        """"""

        print("Quit command to exit the program\n")

    def help_EOF(self):
        """"""
        pass

    def help_help(self):
        """"""
        return (True)

    def do_create(self, arg):
        """"""

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
        """"""
        if os.path.exits(HBNBCommand.filepath):
            with open(HBNBCommand.filepath, 'r') as path:
                data = json.load(path)
        else:
            data = {}

        instance_dict = arg.to_dict()

        data[arg.__class__.__name__ + "." + instance_dict["id"]] = instance_dict

        with open(HBNBCommand.filepath, 'w') as path:
            json.dump(data, path)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
