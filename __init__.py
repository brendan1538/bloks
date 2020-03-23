#!/usr/bin/python3

from importlib import import_module
from jobs
import yaml

def main():
    with open('process.yaml') as y:
        yamlFile = yaml.load(y, Loader=yaml.FullLoader)

    # @TODO: toss these into conditionals based on jobs in yaml
    jobs.build(yamlFile)
    jobs.deploy(yamlFile)

# import modules based on use key in yaml
def check_modules(buildYAML):
    for moduleName in buildYAML['use']:
        import_module('./modules/'+moduleName, package=None) 

if __name__ == '__main__':
    main()
