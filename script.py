# -----------------------------------------------------------
# Repetitive Task Helper
#
# Author: simo54
# -----------------------------------------------------------

from tasks import *


def main():
    logging.basicConfig(filename='test/myapp.log', level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',)
    logging.info('Started')

    test()

    logging.info('Finished')


if __name__ == "__main__":
    main()
