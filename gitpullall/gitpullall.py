import os
import sys
import gitpullall
import subprocess


try:
    from argparse import ArgumentParser as ArgParser
except ImportError:
    from optparse import OptionParser as ArgParser


def printcmd(cmd):
    """Call the command, then end with a blank space."""
    subprocess.call(cmd, shell=True)
    print("")  # Just to make a space after command


def version():
    """Display the current version of the command."""
    print(gitpullall.__version__)
    sys.exit(0)


def parse_args():
    """Parge the arguments."""
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
    """Shell commands for the different methods."""
    args = parse_args()
    if args.version:
        version()

    gitcounter = 0
    for g in os.listdir():
        if os.path.isdir(g) is True and ".git" in os.listdir(g):
            print("{}".format(g))
            gitcounter = gitcounter + 1
            printcmd("cd {} && git pull".format(g))

    print("Successfully git pulled on {} subfolder{}".format(
        gitcounter,
        "" if gitcounter == 1 else "s"
    ))


def main():
    """Caller for everything in the background."""
    try:
        shell()
    except KeyboardInterrupt:
        print('\nCancelling...')
    except PermissionError:
        print('Seems like you are missing permissions to access a folder inside this directory...')


if __name__ == '__main__':
    main()
