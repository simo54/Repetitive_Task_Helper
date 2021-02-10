# -----------------------------------------------------------
# Repetitive Task Helper
#
# Author: simo54
# -----------------------------------------------------------

from tasks import *


def main():
    logging.basicConfig(filename='test/myapp.log', level=logging.INFO)
    logging.info('Started')

    test()

    logging.info('Finished')


if __name__ == "__main__":
    main()
