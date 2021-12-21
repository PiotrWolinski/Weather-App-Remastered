"""Script for deploying app with given settings.

Command line arguments:
 -d - run detached
 -n - build without using cache

Keyword arguments:
argument -- description
Return: return_description
"""

import subprocess
import sys

def deploy(detached=False, no_cache=False):
    subprocess.check_call(f"docker-compose build {'--no-cache' if no_cache else ''}", stdout=sys.stdout, stderr=subprocess.STDOUT)
    subprocess.check_call(f"docker-compose up {'-d' if detached else ''}", stdout=sys.stdout, stderr=subprocess.STDOUT)

def main():
    opts = [opt[1:].lower() for opt in sys.argv[1:] if opt.startswith("-")]
    print(f'opts = {opts}')

    detached = 'd' in opts
    no_cache = 'n' in opts

    deploy(detached=detached, no_cache=no_cache)

if __name__ == '__main__':
    main()
    