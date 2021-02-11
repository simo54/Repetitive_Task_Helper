# -----------------------------------------------------------
# Repetitive Task Helper
#
# Author: simo54
# -----------------------------------------------------------

from tasks import *
import logging


def main():
    logging.basicConfig(filename='test/myapp.log', level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',)
    logging.info('Beginning of script')

    vsc_projectOne()
    speed()

    logging.info('End of script')


if __name__ == "__main__":
    main()
