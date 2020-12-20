from setuptools import setup
setup(
    name = 'dact',
    version = '0.1.0',
    packages = ['dact'],
    entry_points = {
        'console_scripts': [
            'dact = dact.__main__:main'
        ]
    })