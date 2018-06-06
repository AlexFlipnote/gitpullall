import os
import sys
import gitpullall
import subprocess


try:
    from argparse import ArgumentParser as ArgParser
except ImportError:
    from optparse import OptionParser as ArgParser


def printcmd(cmd):
    subprocess.call(cmd, shell=True)
    print("")  # Just to make a space after command


def version():
    print(gitpullall.__version__)
    sys.exit(0)


def parse_args():
    description = ("Calls the command 'git pull' on all subfolders")

    parser = ArgParser(description=description)
    try:
        parser.add_argument = parser.add_option
    except AttributeError:
        pass

    parser.add_argument('--version', action='store_true', help='Show the version number and exit')

    options = parser.parse_args()
    if isinstance(options, tuple):
        args = options[0]
    else:
        args = options
    return args


def shell():
    args = parse_args()
    if args.version:
        version()

    for g in os.listdir():
        if os.path.isdir(g) is True:
            print("{}".format(g))
            printcmd("cd {} && git pull".format(g))


def main():
    try:
        shell()
    except KeyboardInterrupt:
        print('\nCancelling...')


if __name__ == '__main__':
    main()
