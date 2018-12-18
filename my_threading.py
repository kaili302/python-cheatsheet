import threading
import time

class Test(object):
    def __init__(self):
        self.shutdown = threading.Event()
        self.thread = threading.Thread(target=self._run, name="Run")
        self.thread.daemon = True
        self.thread.start()

    def _run(self):
        while not self.shutdown.wait(10):
            print ("sleep")

    def stop(self):
        self.shutdown.set()

test = Test()
test.stop()

# Multi-thread programming
# The entire Python program only exits when all non-daemon threads end!
# Yes, a non-daemon thread can block main process from shutting down!


# Prefer version 1 than version 2 and 3
def _run(self): # VERSION 1
    while not self.shutdown.wait(10):
        print ("sleep")

def _run(self): # VERSION 2
    while not self.shutdown.wait(1):
        time.sleep(9)
        print ("sleep")

def _run(self): # VERSION 3
    while not self.is_shuttingdown:
        time.sleep(10)
        print ("sleep")

# Version 2 and 3 will block the program from shutting down while version 1
# exit immediately


