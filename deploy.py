"""Script for deploying app with given settings.

Command line arguments:
 -d - run detached

Keyword arguments:
argument -- description
Return: return_description
"""

import subprocess
import sys

def deploy():
    subprocess.run("docker-compose up", shell=True, capture_output=True)

def main():
    opts = [opt[1:].lower() for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg.lower() for arg in sys.argv[1:] if not arg.startswith("-")]
    print(f'opts = {opts}')
    print(f'args = {args}')

if __name__ == '__main__':
    main()
    