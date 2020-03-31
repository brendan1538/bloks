#!/usr/bin/python3

from importlib import import_module
import static_deploy
import yaml

def run_job(yamlFile):
    bucket = yamlFile['jobs']['deploy']['bucket']
    static_deploy.list_bucket_objects(bucket)

# build job
def build(yamlFile):
    for moduleName in yamlFile['jobs']['build']['use']:
        module = get_module(moduleName)
        module.run(yamlFile['jobs']['build'][moduleName])

# import modules based on use key in yaml
def get_module(moduleName):
    module = import_module('..'+moduleName.replace('-', '_'), package='modules.subpkg') 

    return module

if __name__ == '__jobs__':
    build()
