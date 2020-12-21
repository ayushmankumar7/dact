import sys
from .classmodule import MyClass
from .funcmodule import startDjangoProject

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    if len(args) < 1: 
        print("Please Enter the Django Project name. Use it like 'dact yourprojectname'")
    elif len(args) == 1:

        startDjangoProject(args[0])

    elif len(args) ==2:
        startDjangoProject(args[0], args[1])

    my_object = MyClass('Your Django + reACT Project is ready to use.')
    my_object.say_name()

def testing():
    print("Testing function was called")

if __name__ == '__main__':
    main()