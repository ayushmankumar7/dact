from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'dact',
    version = '1.2.1',
    author = "Ayushman Kumar|Arkaprabha Chakraborty",
    author_email="ayushmankumar7@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ayushmankumar7/dact",
    packages = ['dact'],
    entry_points = {
        'console_scripts': [
            'dact = dact.__main__:main', 
            'dact-watch = dact.__main__:watch_react', 
            'dact-test = dact.__main__:testing'
        ]
    },
    install_requires=[
        'django==3.0.8'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    
    )