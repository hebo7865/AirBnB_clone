#!/usr/bin/python3
"""The command line."""

import cmd
from models import base_model
from models import user
from models import state
from models import city
from models import amenity
from models import place
from models import review
from models.__init__ import storage
import re


class HBNBCommand(cmd.Cmd):
    """Interpreter class."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": base_model.BaseModel,
        "User": user.User,
        "State": state.State,
        "City": city.City,
        "Amenity": amenity.Amenity,
        "Place": place.Place,
        "Review": review.Review
        }

    def do_EOF(self, line):
        """EOF to quit the program."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Handle empty line."""
        return False

    def fill_in(self, line, num):
        """To fill the desired arguments."""
        result = (re.findall(r'"([^"]*)"|([^\s]+)', line))
        arr = []
        for i in range(num):
            try:
                for j in result[i]:
                    if j != "":
                        arr.append(j)
            except Exception:
                arr.append(None)
        return arr

    def do_create(self, model):
        """Create new instance of a class."""
        if not model:
            print("** class name missing **")
            return False
        elif model not in self.classes.keys():
            print("** class doesn't exist **")
            return False
        else:
            obj = self.classes[model]()
            obj.save()
            print(f"{obj.id}")

    def do_show(self, line, print_value=True):
        """Show object from specific model."""
        model, id = self.fill_in(line, 2)
        if not model:
            print("** class name missing **")
            return False
        elif model not in self.classes.keys():
            print("** class doesn't exist **")
            return False
        elif not id:
            print("** instance id missing **")
            return False
        else:
            objs = storage.all()
            key = f"{model}.{id}"
            if key not in objs.keys():
                print("** no instance found **")
                return False
            else:
                if print_value:
                    print(objs[key].__str__())
                else:
                    return objs[key]

    def do_destroy(self, line):
        """Delete object from specific model."""
        model, id = self.fill_in(line, 2)

        if not model:
            print("** class name missing **")
            return False
        elif model not in self.classes.keys():
            print("** class doesn't exist ** ")
            return False
        elif not id:
            print("** instance id missing **")
            return False
        else:
            objs = storage.all()
            key = f"{model}.{id}"
            if key not in objs.keys():
                print("** no instance found **")
                return False
            else:
                del objs[key]
                storage.save()

    def do_all(self, model):
        """Print all string representation of all instances."""
        if model and model not in self.classes.keys():
            print("** class doesn't exist **")
            return False
        else:
            objs = storage.all()
            my_list = []
            if model:
                for key, value in objs.items():
                    if model in key:
                        my_list.append(value.__str__())
            else:
                for key, value in objs.items():
                    my_list.append(value.__str__())
            print(my_list)

    def do_update(self, line):
        """To update instance of a class."""
        model, id, attr_name, attr_value = self.fill_in(line, 4)
        if not model:
            print("** class name missing **")
            return False
        elif model not in self.classes.keys():
            print("** class doesn't exist **")
            return False
        elif not id:
            print("** instance id missing **")
            return False
        elif not attr_name:
            print("** attribute name missing **")
            return False
        elif not attr_value:
            print("** value missing **")
            return False
        else:
            key = f"{model}.{id}"
            objs = storage.all()
            objs[key].__dict__[attr_name] = attr_value
            objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
