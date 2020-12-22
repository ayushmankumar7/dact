import os
from pathlib import Path as path

def getcurrent():
    y = os.getcwdb()
    return y

def make_dirs(x):
    os.mkdir("static")
    os.mkdir("templates")

     


