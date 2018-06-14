#!/usr/bin/env python

import time
from pytimer import PyTimer

if __name__ == "__main__":
    print "About to run Task A"
    with PyTimer("Task A", enabled=True):
        time.sleep(1)

    print "About to run Task B"
    with PyTimer("Task B", enabled=True):
        time.sleep(1)

    print "About to run Task C (not profiled)"
    with PyTimer("Task C", enabled=False):
        time.sleep(1)

