![logo2](https://user-images.githubusercontent.com/33743193/122555900-2bb71a00-d03b-11eb-8b01-92e194bd4d86.png)

## Threading Class

This is a created class for threading that can run in infinite loop.

* Creating a class for threading.
* Being able to stop it with special stop() method.
* Adjusting deamon state of the created thread.

### Used external modules
1. [Threading Module / import datetime](https://docs.python.org/3/library/threading.html)
2. [Time Module / import sys](https://docs.python.org/3/library/time.html)

### Availability properties
1. Multiple thread class can be created
2. Each thread can run in infinity loop (while loop)
3. Special stop() method to stop the thread which is inside the loop
4. Availability to set deamon statue of the thread

__Note__: If thread is not deamon, be sure that you called stop() method

---
### Code and Syntax

> It must has threading and time modules with `import threading, time`

```python
import threading
import time
```
> After than that, external function class has been created, which is called as ` class functionClass` to have example class that runs as thread.

```python
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

```
> To be able to create a thread, `class threadClass` has been created with parent class thread.

```python
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
```

> As final test implementation, `if __name__ == '__main__':` has been added to test each functionality.

```python
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

```
> And when you run the code, output will be like;

```python
Thread has been started!
Thread is running!
Function runs in thread!
Thread is running!
Function runs in thread!
Thread is running!
Function runs in thread!
Thread is running!
Function runs in thread!
Thread is running!
Function runs in thread!
Main thread ends!
Stop thread has been called!
Thread has stopped!

Process finished with exit code 0
```

__Note__: Thread which is running in the infinite loop can be stopped with stop() method.  
If you thread is Non-Deamon, it is important to stop it before main thread ends. Otherwise,  
it will run all the time. If it is a Deamon thread, it is not important to stop at the end of  
main thead, because it will stop and end as soon as main thread ends. You can still used stop()  
middle of the main thread even if it is  Deamon thread.




