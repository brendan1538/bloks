#!/usr/bin/python3

from subprocess import Popen, PIPE
import os

def run(config, repoDir):
    env = config['env']
    env=('--'+env) if not env else ''
    packageManager = config['use']
    dirs = config['dirs']

    for dir in dirs:
        install = Popen([packageManager, 'install', env], stdout=PIPE, stderr=PIPE, cwd=repoDir+dir)
        installOut,installErr = install.communicate()

        if installErr:
            print(installErr)
        else:
            print(f"Finished installing in {dir}") 

if __name__ == '__tree_install__':
    run()
