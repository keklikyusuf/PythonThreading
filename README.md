![logo2](https://user-images.githubusercontent.com/33743193/122555900-2bb71a00-d03b-11eb-8b01-92e194bd4d86.png)

## Functional Printing

This is a created class for functional printing.

* Printing with time, date or timedate stamps.
* Adding colors to increasing interactivity.
* Can be used itself, or imported with its class

### Used external modules
1. [Datetime Module / import datetime](https://docs.python.org/3/library/datetime.html)
2. [System Module / import sys](https://docs.python.org/3/library/sys.html)

### Avaliable printing options
1. Print with time stamp (hh.mm.ss)
2. Print with date stamp (dd/mm/yyyy)
3. Print with date and time stamps (dd/mm/yyyy - hh.mm.ss)
4. Available colors: Purple, Blue, Cyan, Green, Yellow, Red, Normal

__Note__: Colors can be used with any options of stamping.

---
### Code and Syntax

> It must has datetime and sys modules with `import datetime, sys`

```python
import datetime
import sys
```
> After than that, colors has been defined together with a class, which is called as ` class BColor` to have stdout color codes with simple naming.

```python
class BColors:
    """
    Color codes has been named for easy usage that can be called with their names.
    """
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    normal = '\033[0m'
```
> To be able to create proper printing with stamps, `class PrintStamps` has been created with multiple functions.

```python
class PrintStamps:

    def __init__(self, color):
        """
        :param color: Enter desired color that has been alredy defined at BColors class!
        Funtional printing object is being created. For seperation spacer can be changed according to wishes. 
        """
        self.spacer = '------------------------------------------------------------------------------------'
        self.color = color

    def dateStamp(self, message):
        """
        :param message: Text message that wanted to be printed
        :return: This function returns to printed text message
        Any message is being printed with defined stamp to create functional colorful printing
        """
        sys.stdout.write(self.color)
        now = datetime.datetime.now()
        text = f'{now.strftime("%d/%m/%Y")}: {message} \n{self.spacer}'
        print(text)
        return text

    def timeStamp(self, message):
        """
        :param message: Text message that wanted to be printed
        :return: This function returns to printed text message
        Any message is being printed with defined stamp to create functional colorful printing
        """
        sys.stdout.write(self.color)
        now = datetime.datetime.now()
        text = f'{now.strftime("%X")}: {message} \n{self.spacer}'
        print(text)
        return text

    def datetimeStamp(self, message):
        """
        :param message: Text message that wanted to be printed
        :return: This function returns to printed text message
        Any message is being printed with defined stamp to create functional colorful printing
        """
        sys.stdout.write(self.color)
        now = datetime.datetime.now()
        text = f'{now.strftime("%d/%m/%Y - %X")}: {message} \n{self.spacer}'
        print(text)
        return text
```
> That, it can be created as multiple times for each spesific usage or, it can be created with one purpuse and different variations of the stamping options.

> As final test implementation, `if __name__ == '__main__':` has been added to test each functinallty.

```python
if __name__ == '__main__':
    printPurple = PrintStamps(BColors.purple)
    printBlue = PrintStamps(BColors.blue)
    printCyan = PrintStamps(BColors.cyan)
    printGreen = PrintStamps(BColors.green)
    printYellow = PrintStamps(BColors.yellow)
    printRed = PrintStamps(BColors.red)
    printNormal = PrintStamps(BColors.normal)
    printPurple.dateStamp('Printing with date stamp!')
    printPurple.timeStamp('Printing with time stamp!')
    printPurple.datetimeStamp('Printing with date and time stamp!')
    printBlue.dateStamp('Printing with date stamp and error!')
    printBlue.timeStamp('Printing with time stamp!')
    printBlue.datetimeStamp('Printing with date and time stamp!')
    printCyan.dateStamp('Printing with date stamp and error!')
    printCyan.timeStamp('Printing with time stamp!')
    printCyan.datetimeStamp('Printing with date and time stamp!')
    printGreen.dateStamp('Printing with date stamp and error!')
    printGreen.timeStamp('Printing with time stamp!')
    printGreen.datetimeStamp('Printing with date and time stamp!')
    printYellow.dateStamp('Printing with date stamp and error!')
    printYellow.timeStamp('Printing with time stamp!')
    printYellow.datetimeStamp('Printing with date and time stamp!')
    printRed.dateStamp('Printing with date stamp and error!')
    printRed.timeStamp('Printing with time stamp!')
    printRed.datetimeStamp('Printing with date and time stamp!')
    printNormal.dateStamp('Printing with date stamp and error!')
    printNormal.timeStamp('Printing with time stamp!')
    printNormal.datetimeStamp('Printing with date and time stamp!')

```
> And when you run the code, output will be like;

```python
18/06/2021: Printing with date stamp with Purple! 
------------------------------------------------------------------------------------
12:23:57: Printing with time stamp with Purple! 
------------------------------------------------------------------------------------
18/06/2021 - 12:23:57: Printing with date and time stamp with Purple! 
------------------------------------------------------------------------------------
18/06/2021: Printing with date stamp with Blue! 
------------------------------------------------------------------------------------
12:23:57: Printing with time stamp with Blue! 
------------------------------------------------------------------------------------
18/06/2021 - 12:23:57: Printing with date and time stamp with Blue! 
------------------------------------------------------------------------------------
18/06/2021: Printing with date stamp with Cyan! 
------------------------------------------------------------------------------------
12:23:57: Printing with time stamp with Cyan! 
------------------------------------------------------------------------------------
18/06/2021 - 12:23:57: Printing with date and time stamp with Cyan! 
------------------------------------------------------------------------------------
18/06/2021: Printing with date stamp with Green! 
------------------------------------------------------------------------------------
12:23:57: Printing with time stamp with Green! 
------------------------------------------------------------------------------------
18/06/2021 - 12:23:57: Printing with date and time stamp with Green! 
------------------------------------------------------------------------------------
18/06/2021: Printing with date stamp with Yellow! 
------------------------------------------------------------------------------------
12:23:57: Printing with time stamp with Yellow! 
------------------------------------------------------------------------------------
18/06/2021 - 12:23:57: Printing with date and time stamp with Yellow! 
------------------------------------------------------------------------------------
18/06/2021: Printing with date stamp with Red! 
------------------------------------------------------------------------------------
12:23:57: Printing with time stamp with Red! 
------------------------------------------------------------------------------------
18/06/2021 - 12:23:57: Printing with date and time stamp with Red! 
------------------------------------------------------------------------------------
18/06/2021: Printing with date stamp with Normal/Gray! 
------------------------------------------------------------------------------------
12:23:57: Printing with time stamp with Normal/Gray! 
------------------------------------------------------------------------------------
18/06/2021 - 12:23:57: Printing with date and time stamp with Normal/Gray! 
------------------------------------------------------------------------------------
```

__Note__: Output comes with added colors but cannot be seen here!




