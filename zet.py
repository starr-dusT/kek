import argparse
import os
import sys
from command import Command

class Zet(Command):
    def zet(self): 
        super().__init__('edit')

        # Read command attributes
        parser = argparse.ArgumentParser()
        parser.add_argument('file', help='file to edit')
        args = parser.parse_args(sys.argv[2:])
        
        # Parse command attributes
        if args.file == 'last':
            super()._run_last()
        else:
            self._edit_file(args.file)
    
    # Idea: make it open multiple files (if there are multiple) in split?
    # Idea: detect chezmoi file and apply on close of file
    def _edit_file(self, file):
        file_abs_path = os.path.abspath(os.path.expanduser(file))
        super()._run_expression('nvim ' + file_abs_path)
