import os

def startDjangoProject(name):
    os.system(f"django-admin startproject {name}")
    os.chdir(name)
    os.system("django-admin startapp reactfrontend")
    