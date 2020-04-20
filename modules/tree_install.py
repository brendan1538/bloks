#!/usr/bin/python3

import logging
from subprocess import run
import os

def main_process(config, repoDir, *args):
    env = config['env']
    env=('--'+env) if not env else ''
    packageManager = config['use']
    dirs = config['dirs']

    for dir in dirs:
        install = run([packageManager, 'install', env], cwd=repoDir+dir)
        installErr = install.stderr

        if installErr:
            logging.error('error: '+installErr)
        else:
            print(f"Finished installing in {dir}") 

if __name__ == '__tree_install__':
    main_process()
