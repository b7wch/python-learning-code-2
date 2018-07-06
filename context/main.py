__author__ = 'jasonyang'


class ContextManager(object):
    """this is a contextmanager"""

    def __init__(self):
        self.str = "hello"

    def __enter__(self):  # program go into the block from here
        print "go in"
        return self.str

    def __exit__(self, exc_type, exc_value, traceback):  # when the program go out this function running
        print 'go out'


if __name__ == '__main__':
    contextmanager = ContextManager()
    with contextmanager as temp:
        print temp
