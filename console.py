#!/usr/bin/python3
'''
    command prompt
'''
import cmd
from models.base_model import BaseModel

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
        if len(cmds) == 0:
            print("** class name missing **")
        elif arg[0] in HBNBCommand.__classes:
            obj = BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")
    def do_show(self, arg):
        '''Prints the string representation of an instance based on class name'''
        cmds = arg.split(' ')
        objdict = storage.all()
        len_c = len(cmds)
        if len_c == 0:
            print("** class name missing **")
        elif cmds[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len_c == 1:
            print("** instance id missing **")
        elif cmds[1] not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
