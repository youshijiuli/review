import os
import sys
ROOT_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT_DIR)
from core.src import run
if __name__ == '__main__':
    run()