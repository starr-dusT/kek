import subprocess
import os
from pathlib import Path

class Command(object):
    def __init__(self, command_name): 
        # Create temp dir for persistence 
        tmp_dir = str(os.environ.get('XDG_RUNTIME_DIR')) + '/kek'
        Path(tmp_dir).mkdir(parents=True, exist_ok=True)
        self.tmp_file = tmp_dir + '/' + command_name + '_history' 

    def _run_expression(self, expression, save=False, capture=False):
        if save:
            f = open(self.tmp_file, 'a')
            f.write(expression + '\n')
            f.close
        if not capture:
            subprocess.run(expression, shell=True)
        else:
            return subprocess.call(expression, 
                                   shell=True, 
                                   stdout=subprocess.DEVNULL, 
                                   stderr=subprocess.STDOUT)

    def _run_last(self):
        with open(self.tmp_file) as f:
            last_line = f.readlines()[-1].strip('\n')
            subprocess.run(last_line, shell=True)
