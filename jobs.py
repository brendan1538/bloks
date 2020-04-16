#!/usr/bin/python3

from git import Git
from importlib import import_module
import static_deploy
import yaml
import os

def run_job(yamlFile):
    bucket = yamlFile['jobs']['deploy']['bucket']
    static_deploy.list_bucket_objects(bucket)

# build job
def build(yamlFile):
    buildProcess = yamlFile['jobs']['build']
    clone_repo(buildProcess['repo'])

    for moduleName in buildProcess['use']:
        module = get_module(moduleName)
        module.run(buildProcess[moduleName])

# import modules based on use key in yaml
def get_module(moduleName):
    module = import_module('..'+moduleName.replace('-', '_'), package='modules.subpkg') 

    return module

def clone_repo(url):
    Git(os.path.join(os.getcwd(), 'build/')).clone(url)
    

# def delete_repo():

if __name__ == '__jobs__':
    build()
