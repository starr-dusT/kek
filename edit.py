import argparse
import os
import sys
from command import Command

class Edit(Command):
    def edit(self): 
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
        not_in_chezmoi = super()._run_expression('chezmoi source-path ' + file_abs_path, capture=True)
        if not_in_chezmoi == 1:
            super()._run_expression('nvim ' + file_abs_path, save=True)
        else:
            super()._run_expression('chezmoi edit ' + file_abs_path, save=True)
