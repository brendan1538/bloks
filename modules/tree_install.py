#!/usr/bin/python3

from subprocess import Popen, STDOUT, PIPE

def run(packageManager, env, dirs):
    env=('--'+env) if not env else ''

    for dir in dirs:
        install = Popen([packageManager, 'install', env], STDOUT=PIPE, STDERR=STDOUT)
        installOut,installErr = install.communicate()

        if installErr:
            print(installErr)
        else:
            print(f"Finished installing in {dir}") 

if __name__ == '__tree_install__':
    run()
