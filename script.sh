#!/usr/bin/env python3

# -----------------------------------------------------------
# Repetitive Task Helper
#
# Author: simo54
# -----------------------------------------------------------

import os
import logging

from tasks import *
from utils import *

def main():
    logging.basicConfig(filename='test/output.log', level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(funcName)s: %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
    new_line()
    
    logging.info('--------- START of tasks ---------')
    
    # -------- Process List --------
    git_status()
    ls_view()
    # -------- Process List --------

    logging.info('--------- END of tasks ---------')

if __name__ == "__main__":
    main()
