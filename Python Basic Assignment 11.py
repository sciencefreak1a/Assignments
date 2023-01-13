#1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.
try :
    spam = -1
    assert spam == 10
except:
    AssertionError

#2.Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and &#39;goodbye&#39; and &#39;GOODbye&#39; are also considered the same).
try :
    eggs = "goodbye"
    bacon = "GOODbye"
    assert eggs.lower()!=bacon.lower()
    print("The eggs and bacon variables are the same")
except :
    AssertionError

#3Create an assert statement that throws an AssertionError every time.
try :
    assert False
except :
    AssertionError


#4 What are the two lines that must be present in your software in order to call logging.debug()?
 import logging
 logging.basicConfig(level=DEBUG,
                    format='%(asctime)s (levelname)s%-%(messages)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

 #5What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
import logging
 logging.basicConfig(filename='programLOg.exe',
                    level=DEBUG,
                    format='%(asctime)s (levelname)s%-%(messages)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

 #6. What are the five levels of logging?
 #DEBUG,INFO,WARNING,ERROR,CRITICAL

 #7. What line of code would you add to your software to disable all logging messages?
 logging.disable(logging.CRITICAL)

 #8.Why is using logging messages better than using print() to display the same message?
 #By using logging to track the code, we can format the messages based on our needs.
 #Logging can be differentiated based on severity. It is easy to see where and when along with the line number a logging call is being made from.

 #9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
# The Step In button will move the debugger into a function call.
# The Step Over button will quickly execute the function call without stepping into it.
# The Step Out button will quickly execute the rest of the code until it steps out of the function it currently is in.

#10.After you click Continue, when will the debugger stop ?
#Continuing means resuming program execution until your program completes normally i.e., end of the program or a line with a break point

#11. What is the concept of a breakpoint?
#A breakpoint is a setting in the line of a code that causes the debugger to pause when the program execution reaches the line











