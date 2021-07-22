from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'dact',
    version = '1.3.0',
    author = "Ayushman Kumar|Arkaprabha Chakraborty",
    author_email="ayushmankumar7@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ayushmankumar7/dact",
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'dact = dact.__main__:main', 
            'dact-watch = dact.__main__:watch_react', 
            'dact-test = dact.__main__:testing',
            'dact-install = dact.__main__:package_install'
        ]
    },
    install_requires=[
        'django==3.2.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    
    )