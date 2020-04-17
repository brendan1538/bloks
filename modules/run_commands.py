from subprocess import run
import re

def main_process(cmdsList, repoDir):
  for cmd in cmdsList:
    parsedCmd = re.findall(r'"[^"]+"|[\w]+', cmd)
    output = run(parsedCmd, cwd=repoDir)

    print(output.stdout)

if __name__ == '__run__':
  main_process()
