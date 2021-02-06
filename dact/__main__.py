import sys
import os
import json

from .classmodule import MyClass
from .funcmodule import startDjangoProject
from .createreact import getcurrent
from .visuals import ascii_dact

def main():
    
    args = sys.argv[1:]
   
    if len(args) < 1: 
        ascii_dact()
        print(
            
            """
            Congratulations! Dact is successfully installed in your system. 
            To learn more about dact, go to https://ayushmankumar7.github.io/dact/. 

            To get started with Dact, type dact newproject 

            Hurray! Your first Django + React Project is ready to be worked on.

            """
        )


    elif len(args) == 1:
        startDjangoProject(args[0])
        
    elif len(args) ==2:
        startDjangoProject(args[0], args[1])
    

def watch_react():
    with open("dact_config.json") as f:
        data = json.load(f)
    frontend_app = data['Frontend_AppName']
    os.chdir(f"{frontend_app}/static")
    os.system("npm run dev")

def package_install():
    with open("dact_config.json") as f:
        data = json.load(f)
    frontend_app = data['Frontend_AppName']
    os.chdir(f"{frontend_app}/static")
    os.system("npm install")


def testing():
    print("Testing function was called")

if __name__ == '__main__':
    main()