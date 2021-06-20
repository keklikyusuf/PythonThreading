"""
This is created for class Threading!
You can create your class and push inside Threading class to run it while main thread is keep running.
version 0.0.1
@keklikyusuf
"""

import threading
import time


class functionClass:
    """
    This is the class that is going to be called as a Thread.
    """
    def function(self):
        """
        :return: It returns a string that we created in this example.
        """
        doSomething = f'Function runs in thread!'
        print(doSomething)
        return doSomething

aDaemonThread = DaemonThread()

aDaemonThread.daemon = False

aDaemonThread.start()

print("My Daemon will take care")


class threadClass(threading.Thread):
    """
    This is the threading class, that it can be called with an external method to be able run at separated thread.
    """
    def __init__(self, sleepTime):
        """
        :param sleepTime: Time that has been implemented for sleeping time of the thread.
        """
        super(threadClass, self).__init__()
        self.sleepTime = sleepTime
        self._stop_event = threading.Event()

    def stop(self):
        """
        :return: Stop event of the threading library to be able to end the thread.
        """
        print("Stop thread has been called!")
        return self._stop_event.set()

    def run(self):
        """
        :return: It returns none
        It is an infinete loop that has sleep time. To be able to stop it stop() method needs to be called.
        """
        print("Thread has been started!")
        Action = functionClass()
        while not self._stop_event.is_set():
            print("Thread is running!")
            Action.function()
            time.sleep(self.sleepTime)
        print("Thread has stopped!")


if __name__ == '__main__':
    MyThread1 = threadClass(2)
    MyThread1.start()
    time.sleep(10)
    MyThread1.stop()