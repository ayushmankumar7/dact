import sys
from .classmodule import MyClass
from .funcmodule import startDjangoProject

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    startDjangoProject(args)

    my_object = MyClass('Django + React Haha')
    my_object.say_name()

def testing():
    print("Testing function was called")

if __name__ == '__main__':
    main()