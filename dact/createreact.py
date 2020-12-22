import os
from pathlib import Path as path

def getcurrent():
    y = os.getcwdb()
    return y

def make_dirs(x):
    os.mkdir("static")
    os.chdir("static")
    os.mkdir("src")
    os.mkdir("js")
    os.mkdir("css")
    os.chdir("..")
    os.chdir(x)
    os.mkdir("templates")
    os.chdir("templates")
    

def create():
    x = getcurrent()
    make_dirs(x)

     


