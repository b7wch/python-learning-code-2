__author__ = 'jasonyang'
import config
from config import NoConfigType

if __name__ == '__main__':
    try:
        db = config.get_config('onlidne')
    except NoConfigType, ex:
        print ex
