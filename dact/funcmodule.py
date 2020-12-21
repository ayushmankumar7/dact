import os


def manipulate_settings(setting_file):
    with open(setting_file, 'r') as b:
        lines = b.readlines()

    with open(setting_file, 'w') as b:
        for i, line in enumerate(lines):
            if i== 39:
                b.write("\t'reactfrontend.apps.ReactfrontendConfig',\n")
            b.write(line)
     



def startDjangoProject(name):
    print("[INFO] Creating Django Project ....")
    os.system(f"django-admin startproject {name}")
    os.chdir(name)
    print("[INFO] Creating React App ....")
    os.system("django-admin startapp reactfrontend")
    os.chdir(name)
    manipulate_settings('settings.py')