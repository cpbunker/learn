'''
GitHub/cpbunker/learn/concurrency/threads.py

Intro to python threading module
https://realpython.com/intro-to-python-threading/
'''

import time
import threading

def wait_five(thread_name: str) -> None:
    print(" - Thread "+thread_name+" starting");
    time.sleep(5);
    print(" - Thread "+thread_name+" finishing");

def create_and_run(thread_name: str, thread_target: callable, thread_args: tuple) -> threading.Thread:
    if( not isinstance(thread_name, str)): raise TypeError;
    if( not isinstance(thread_args, tuple)): raise TypeError;
    
    print(" - Creating "+thread_name);
    thread_obj = threading.Thread(target = thread_target, args = thread_args);
    print(" - Running "+thread_name);
    thread_obj.start();
    return thread_obj

#### joining a single thread
print("1. A simple example with join()");

# init thread object with target, a callable, args for callable
myname = "Bill"
mythread = create_and_run(myname, wait_five, (myname,) );

# run thread with or without joining
join = True;
if join:
    mythread.join();
    print("We waited for the thread to end");
else:
    print("We reached the end before thread is finished");


#### starting and finishing orders
print("2. Demonstrating ordering");

print("Creating and starting threads");
numthreads = 3;
threads = [];
for i in range(numthreads):
    th = create_and_run(str(i), wait_five, (str(i),) );
    threads.append(th);

for i in range(numthreads):
    print("Joining thread "+str(i));
    threads[i].join();

#### what the with statement does
print("3. The with statement");

class dummy(object):

    def __enter__(self):
        print(" - the with statement calls __enter__ first");
        return [0,1,2];

    def __exit__(self, exception_type, exception_value, traceback):
        print(" - the with statement calls __exit__ last");
        print(" - __exit__ requires four args:");
        argnames = ["self", "exception_type", "exception_value", "traceback"];
        args = [self, exception_type, exception_value, traceback];
        for i in range(len(args)):
            print("  -> ", argnames[i],": ",args[i]);

with dummy() as mydummy:
    print(" - Code block");
    print(" - mydummy = ",mydummy,"comes from the return value of __enter__");

      
