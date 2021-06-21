"""
This is created for class Threading with an interruptable infinite loop!
You can create your class and push inside Threading class to run as thread infinite loop.
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


class threadClass(threading.Thread):
    """
    This is the threading class, that it can be called with an external method to be able run at separated thread.
    It is default deamon thread which means when main thread ends, all program ends its running.
    You can use as Non-Deamon thread as well which it will run even if main thread ends and you need to call
    stop() method to be able to stop it.
    """
    def __init__(self, sleepTime, deamonState=True):
        """
        :param sleepTime: Time that has been implemented for sleeping time of the thread.
        :param deamonState: Deamon state of the thread can be defined with this boolean.
        """
        super(threadClass, self).__init__()
        self.deamonState = deamonState
        self.sleepTime = sleepTime
        self._stop_event = threading.Event()
        self.setDaemon(self.deamonState)

    def stop(self):
        """
        :return: Stop event of the threading library to be able to end the thread which is in an infinite while loop.
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
    """
    If it has been created as Non-Deamon thread, it is important to use stop() method to finish the thread
    Otherwise it will always run even if the main thread is finished!
    If thread is Deamon thread and main thread ends, it will automatically ends with it together, that no need to call
    stop() method at the end of your main thread execution. 
    """
    MyThread1 = threadClass(1, False)
    MyThread1.start()
    time.sleep(5)
    print("Main thread ends!")
    MyThread1.stop()