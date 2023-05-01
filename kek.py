#!/usr/bin/env python

import sys
import argparse
from edit import Edit 

class Kek(Edit):
    def __init__(self):
        print('KEKW')

        # Read command attributes
        parser = argparse.ArgumentParser()
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])

        # Run command if we have it
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

if __name__ == '__main__':
    Kek()
