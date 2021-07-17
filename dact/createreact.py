import os
from pathlib import Path as path
from .template_files.css_data import Css_Templates
from .template_files.html_data import Html_Templates
from .template_files.js_data import React_templates
from .template_files.package_file import Package_Json

css = Css_Templates()
css = css.get_initial_css_files()
html = Html_Templates()
html = html.get_html_files()
js = React_templates()
js = js.get_intial_js_files()
package = Package_Json()
package = package.get_package_json()

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

def make_template():
    open("index.html",'x')
    with open("index.html",'r+') as file:
        file.write(html['index.html'])
        file.close()

def write_webpack_config():
    open('webpack.config.js','x')
    with open('webpack.config.js','r+') as file:
        file.write(js['webpack.config.js'])
        file.close()

def write_react_App_js():
    open("App.js",'x')
    with open('App.js','w') as file:
        file.write(js['App.js'])
        file.close()

def write_index_js():
    open('index.js','x')
    with open('index.js','w') as file:
        file.write(js['index.js'])
        file.close()

def write_package_json():
    open('package.json','x')
    with open('package.json','w') as file:
        file.write(package)
        file.close()


def write_svg():
    open("dact.svg",'x')
    with open("dact.svg",'w') as file:
        file.write(html['dact.svg'])
        file.close()

def write_app_css():
    open("App.css",'x')
    with open("App.css",'w') as file:
        file.write(css['App.css'])
        file.close()

def write_index_css():
    open("index.css","x")
    with open("index.css",'w') as file:
        file.write(css['index.css'])
def add_gitignore():
    open(".gitignore", "x")
    with open(".gitignore", "w") as f:
        f.write("node_modules")

def create():
    x = getcurrent()
    make_dirs(x)
    os.chdir("static")
    write_webpack_config()
    add_gitignore()
    write_package_json()
    os.system(f"npm install --package-lock --force")
    os.chdir("src")
    write_index_js()
    write_react_App_js()
    write_svg()
    write_app_css()
    write_index_css()
    os.chdir('..')
    os.chdir(x)
    os.chdir('templates')
    make_template()
    os.chdir('..')
    os.chdir(x)
    os.chdir("static")
    try:
        os.system(f"npm run webpack --no-hot")
    except:
        print("Exited")
    os.chdir("..")
    os.chdir(x)



     


