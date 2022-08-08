#!/usr/bin/python3
'''
    command prompt
'''
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(arg):
    """parse string to list"""
    return arg.strip().split(" ")


class HBNBCommand(cmd.Cmd):
    '''
        HBNBCommand class extends Cmd
    '''
    prompt = "(hbnb) "
    __classes = [
            "BaseModel",
            "User",
            "City",
            "State",
            "Place",
            "Amenity",
            "Review"
            ]

    def emptyline(self):
        """ Do nothing upon receiving an empty line. """
        pass

    def do_quit(self, arg):
        """ To exit from the console """
        return True

    def do_EOF(self, arg):
        """ to handle EOF """
        return True

    def do_create(self, arg):
        """ create an instance of BaseModel """
        cmds = parse(arg)
        if len(cmds) == 0 or cmds[0] == "":
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(cmds[0])().id)
            storage.save()

    def do_show(self, arg):
        '''Prints the string representation of an instance
        based on class name'''
        cmds = parse(arg)
        objdict = storage.all()
        len_c = len(cmds)
        if len_c == 0 or cmds[0] == "":
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len_c == 1 or cmds[1] == "":
            print("** instance id missing **")
        elif (cmds[0] + "." + cmds[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(cmds[0], cmds[1])])

    def do_destroy(self, arg):
        """Delete object of model"""
        cmds = parse(arg)
        objdict = storage.all()
        len_c = len(cmds)
        if len_c == 0 or cmds[0] == "":
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len_c == 1 or cmds[1] == "":
            print("** instance id missing **")
        elif (cmds[0] + "." + cmds[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(cmds[0], cmds[1])]
            storage.save()

    def do_all(self, arg):
        """ prints all instances of a class else print all"""
        cmds = parse(arg)
        objdict = storage.all()
        check_class = cmds[0] not in HBNBCommand.__classes
        if cmds[0] != "" and check_class and len(cmds) > 0:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in objdict.values():
                if len(cmds) > 0 and cmds[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif cmds[0] == "":
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        cmds = parse(arg)
        objdict = storage.all()
        len_c = len(cmds)
        if len_c == 0 or cmds[0] == "":
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len_c == 1:
            print("** instance id missing **")
        elif (cmds[0] + "." + cmds[1]) not in objdict.keys():
            print("** no instance found **")
        elif len_c == 2:
            print("** attribute name missing **")
        elif len_c == 3:
            print("** value missing **")
        else:
            cls_name = objdict["{}.{}".format(cmds[0], cmds[1])]
            setattr(cls_name, cmds[2], cmds[3].strip('"'))
            storage.save()


if __name__ == '__main__':

    HBNBCommand().cmdloop()
