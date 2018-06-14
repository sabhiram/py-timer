import time

class PyTimer(object):
    """ PyTimer is a simple object that implements the `__enter__` and
        `__exit__` methods to satisfy the `wait` interface.

        This allows for us to track when the scope is entered and closed,
        which provides an easy way to measure the execution time for
        arbitrary code chunks.
    """

    start   = None                  #  Start time
    end     = None                  #  End time
    enabled = True                  #  Timer enabled / disabled switch
    prefix  = ""                    #  Timer prefix to print on exit

    def __init__(self, prefix="", enabled=True):
        """ Construct the timer.  The timer is enabled by default and
            uses an empty prefix.  These can be user overridden.
        """
        self.enabled = enabled
        self.prefix  = ""
        if prefix:
            self.prefix  = prefix

    def __enter__(self):
        """ Record the time when the `with` scope is entered.
        """
        if self.enabled:
            self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        """ Track and output the time when the scope is exited.
        """
        if self.enabled:
            self.end_t = time.time()
            print("%s took %f" % (self.prefix, self.end_t - self.start))
