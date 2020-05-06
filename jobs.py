#!/usr/bin/python3

from importlib import import_module
from subprocess import run
import yaml
import os

def run_job(yamlFile):
    bucket = yamlFile['jobs']['deploy']['bucket']

# build job
def build(yamlFile, remoteOrigin):
    buildProcess = yamlFile['jobs']['build']

    run_module(buildProcess, remoteOrigin)

    print('*** Clearing build folder ***')
    run(['rm', '-rf', (os.path.join(os.getcwd(), 'repo_build/'))])

def deploy(yamlFile, remoteOrigin):
    deployProcess = yamlFile['jobs']['deploy']
    buildOutputFolder = deployProcess['build_output_folder']
 
    run_module(deployProcess, remoteOrigin, buildOutputFolder)

def run_module(job, dir, *args):
    if type(job['use']) == list:
        for moduleName in job['use']:
            module = get_module(moduleName)
            print(f'Running {moduleName}')
            module.main_process(job[moduleName], dir, args)
    else:
        moduleName = job['use']
        module = get_module(moduleName)
        print(f'Running {moduleName}')
        module.main_process(job[moduleName], dir, args)

# import modules based on use key in yaml
def get_module(moduleName):
    module = import_module('..'+moduleName.replace('-', '_'), package='modules.subpkg') 

    return module

# def delete_repo():

if __name__ == '__jobs__':
    deploy()
