import os


def manipulate_settings(setting_file, app_name):
    with open(setting_file, 'r') as b:
        lines = b.readlines()

    with open(setting_file, 'w') as b:
        for i, line in enumerate(lines):
            if i== 39:
                b.write(f"\t'{app_name}.apps.{app_name.title()}Config',\n")
            b.write(line)
     

def manipulate_project_url(pro_url, app_name):
    with open(pro_url, 'r') as b:
        lines = b.readlines()

    with open(pro_url, 'w') as b:
        for i, line in enumerate(lines):
            if i == 17:
                b.write('import django.urls import path, include \n')
            elif i == 21:
                b.write("\tpath('', include('frontend.urls')),\n")

            else:
                b.write(line)





def startDjangoProject(name, app_name = "reactfrontend"):
    print("[INFO] Creating Django Project ....")
    os.system(f"django-admin startproject {name}")
    os.chdir(name)
    print("[INFO] Creating React App ....")
    os.system(f"django-admin startapp {app_name}")
    os.chdir(name)
    manipulate_settings('settings.py', app_name)