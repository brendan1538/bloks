#!/usr/bin/python3

from importlib import import_module
import jobs
import os
from subprocess import run
import yaml

def main(remoteOrigin):
    get_repo(remoteOrigin)
    with open('process.yaml') as y:
        yamlFile = yaml.load(y, Loader=yaml.FullLoader)

    # @TODO: toss these into conditionals based on jobs in yaml
    jobs.build(yamlFile, remoteOrigin)
    # jobs.deploy(yamlFile, remoteOrigin)

def get_repo(url):
    run(['mkdir', 'repo_build'], cwd=os.getcwd())
    buildDir = os.path.join(os.getcwd(), 'repo_build/')
    if not os.listdir(buildDir):
        print('Cloning project into build folder...')
        Git(os.path.join(os.getcwd(), 'repo_build/')).clone(url)
        run(['git', 'clone', '--single-branch', url])
    
    repoName = os.listdir(buildDir)
    repoDir = os.path.join(buildDir+repoName[0])

    return repoDir


if __name__ == '__main__':
    main()
