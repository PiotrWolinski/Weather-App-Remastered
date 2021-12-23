"""Script for deploying and overviewing app.

All CLI arguments are parsed using argparse. Add -h to get help.
"""

import subprocess
import sys
import argparse

def deploy(detached=False, no_cache=False):
    """"Build and deploy containers.

    Arguments:
    - detached - run containers in detached mode
    - no_cache - build services without cache
    """
    # Remove services if any are running
    stop_and_remove_services()

    try:
        subprocess.check_call(f"docker-compose build {'--no-cache' if no_cache else ''}", stdout=sys.stdout, stderr=subprocess.STDOUT)
        subprocess.check_call(f"docker-compose up {'-d' if detached else ''}", stdout=sys.stdout, stderr=subprocess.STDOUT)
    except:
        pass

def stop_and_remove_services():
    """Stop and remove running docker containers.
    """
    try:
        subprocess.check_call("docker-compose down", stdout=sys.stdout, stderr=subprocess.STDOUT)
    except:
        pass

def show_logs():
    """Show logs output.
    """
    
    try:
        subprocess.check_call(f"docker-compose logs", stdout=sys.stdout, stderr=subprocess.STDOUT)
    except:
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--detached", help="run containers detached", action="store_true")
    parser.add_argument("-n", "--no_cache", help="build services without cache", action="store_true")
    parser.add_argument("-l", "--logs", help="stop and remove containers if any are running", action="store_true")
    parser.add_argument("--down", help="stop and remove containers if any are running", action="store_true")

    args = parser.parse_args()

    if args.logs:
        show_logs()

    if args.down:
        stop_and_remove_services()

    if not args.logs and not args.down:
        deploy(detached=args.detached, no_cache=args.no_cache)

if __name__ == '__main__':
    main()
    