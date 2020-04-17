#!/usr/bin/python3

from git import Git
from importlib import import_module
import static_deploy
from subprocess import run
import yaml
import os

def run_job(yamlFile):
    bucket = yamlFile['jobs']['deploy']['bucket']
    static_deploy.list_bucket_objects(bucket)

# build job
def build(yamlFile):
    buildProcess = yamlFile['jobs']['build']
    repoDir = get_repo(buildProcess['repo'])

    for moduleName in buildProcess['use']:
        module = get_module(moduleName)
        print(f'Running {moduleName}')
        module.main_process(buildProcess[moduleName], repoDir)
    
    print('*** Clearing build folder ***')
    run(['rm', '-rf', (os.path.join(os.getcwd(), 'build/'))])

# import modules based on use key in yaml
def get_module(moduleName):
    module = import_module('..'+moduleName.replace('-', '_'), package='modules.subpkg') 

    return module

def get_repo(url):
    run(['mkdir', 'build'], cwd=os.getcwd())
    buildDir = os.path.join(os.getcwd(), 'build/')
    if not os.listdir(buildDir):
        print('Cloning project into build folder...')
        Git(os.path.join(os.getcwd(), 'build/')).clone(url)
    
    repoName = os.listdir(buildDir)
    repoDir = os.path.join(buildDir+repoName[0])

    return(repoDir)

    

# def delete_repo():

if __name__ == '__jobs__':
    build()
