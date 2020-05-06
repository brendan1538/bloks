from subprocess import run
import re

def main_process(cmdsList, repoDir, *args):
  for cmd in cmdsList:
    parsedCmd = re.findall(r'"[^"]+"|[\w]+', cmd)
    output = run(cmd, cwd=repoDir, shell=True)

if __name__ == '__run__':
  main_process()
