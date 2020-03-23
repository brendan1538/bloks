#!/usr/bin/python3
from importlib import import_module

def check_modules(buildYAML):
    for moduleName in buildYAML['use']:
        print(moduleName)

if __name__ == '__main__':
    check_modules(yaml)
