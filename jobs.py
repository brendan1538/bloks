#!/usr/bin/python3

from git import Git
from importlib import import_module
from subprocess import run
import yaml
import os

def run_job(yamlFile):
    bucket = yamlFile['jobs']['deploy']['bucket']

# build job
def build(yamlFile):
    buildProcess = yamlFile['jobs']['build']
    repoDir = get_repo(buildProcess['repo'])

    run_module(buildProcess, repoDir)

    deploy(yamlFile, repoDir)

    print('*** Clearing build folder ***')
    run(['rm', '-rf', (os.path.join(os.getcwd(), 'build/'))])

def deploy(yamlFile, repoDir):
    deployProcess = yamlFile['jobs']['deploy']
    buildOutputFolder = deployProcess['build_output_folder']
 
    run_module(deployProcess, repoDir, buildOutputFolder)

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

def get_repo(url):
    run(['mkdir', 'repo_build'], cwd=os.getcwd())
    buildDir = os.path.join(os.getcwd(), 'repo_build/')
    if not os.listdir(buildDir):
        print('Cloning project into build folder...')
        Git(os.path.join(os.getcwd(), 'repo_build/')).clone(url)
    
    repoName = os.listdir(buildDir)
    repoDir = os.path.join(buildDir+repoName[0])

    return repoDir

# def delete_repo():

if __name__ == '__jobs__':
    deploy()
