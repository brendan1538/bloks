#!/usr/bin/python3

from importlib import import_module
import jobs
import yaml

def main():
    with open('process.yaml') as y:
        yamlFile = yaml.load(y, Loader=yaml.FullLoader)

    # @TODO: toss these into conditionals based on jobs in yaml
    jobs.build(yamlFile)
    # jobs.deploy(yamlFile)

if __name__ == '__main__':
    main()
