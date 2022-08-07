#!/usr/bin/python3
'''
    command prompt
'''
import cmd
from models import storage
from models.base_model import BaseModel

def parse(arg):
    """parse string to list"""
    return arg.split(" ")

class HBNBCommand(cmd.Cmd):
    '''
        HBNBCommand class extends Cmd
    '''
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

    def do_quit(self, arg):
        """ To exit from the console """
        return True

    def do_EOF(self, arg):
        """ to handle EOF """
        return True

    def do_create(self, arg):
        """ create an instance of BaseModel """
        cmds = arg.split(" ")
        print(len(cmds))
        if len(cmds) == 0 or cmds[0] == "":
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)
    def do_show(self, arg):
        '''Prints the string representation of an instance based on class name'''
        cmds = arg.split(' ')
        objdict = storage.all()
        len_c = len(cmds)
        if len_c == 0 or cmds[0] == "":
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len_c == 1:
            print("** instance id missing **")
        elif (cmds[0]+ "."+cmds[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(cmds[0], cmds[1])])
    def do_destroy(self, arg):
        """Delete object of model"""
        cmds = arg.split(' ')
        objdict = storage.all()
        len_c = len(cmds)
        if len_c == 0 or cmds[0] == "":
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len_c == 1:
            print("** instance id missing **")
        elif (cmds[0]+ "."+cmds[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(cmds[0], cmds[1])]
    def do_all(self, arg):
        """ print all instances """
        cmds = parse(arg)
        objdict = storage.all()
        if cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key in objdict:
                print(objdict[key])
    def do_update(self, arg):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
