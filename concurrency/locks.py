'''
GitHub/cpbunker/learn/concurrency/locks.py

Using locks on threads
https://realpython.com/intro-to-python-threading/
'''

import time
import threading


class ThreadManager:
    
    def __init__(self, thread_name: str, thread_target: callable, thread_args: tuple):
        if( not isinstance(thread_name, str)): raise TypeError;
        if( not isinstance(thread_args, tuple)): raise TypeError;

        self.thread_name = thread_name;
        
        print(" - Creating "+thread_name);
        self.thread = threading.Thread(target = thread_target, args = thread_args);

    def start(self) -> None:
        print(" - Starting "+self.thread_name);
        self.thread.start();

    def running(self) -> bool:
        return self.thread.is_alive();

class FooBar:

    def __init__(self, n: int):

        # init
        self.n = n;
        self.stdout = '';

        # construct threads
        self.foothread = ThreadManager('foo', self.foo, ());
        self.barthread = ThreadManager('bar', self.bar, ());

        # construct locks
        self.foolock = threading.Lock();
        self.foolock.acquire();
        self.barlock = threading.Lock();
        self.barlock.acquire();
        self.lock_status();

        # unlock foo
        self.foolock.release();

        # start threads
        self.foothread.start();
        self.barthread.start();

        # keep going till threads finish
        while(self.foothread.running() or self.barthread.running()):
            time.sleep(1);

    def printout(self):
        print("\nFooBar stdout: ",self.stdout);

    def status(self):
        print("\nFooBar status:");
        print(" - foothread running: ",self.foothread.running());
        print(" - barthread running: ",self.barthread.running());

    def lock_status(self):
        print("Locked status:")
        print(" - foolock: ", self.foolock.locked());
        print(" - barlock: ", self.barlock.locked());

    def foo(self):
        for i in range(self.n):

            # pause until foolock is unlocked
            while self.foolock.locked():
                print("passfoo")
                pass;
            
            self.stdout += 'foo';

            # unlock barlock, lock foolock
            self.barlock.release();
            self.foolock.acquire();

    def bar(self):
        for i in range(self.n):

            # pause until barlock is unlocked
            while self.barlock.locked():
                print("passbar")
                pass;
            
            self.stdout += 'bar';

            # unlock foolock, lock barlock
            self.foolock.release();
            self.barlock.acquire();
            




my = FooBar(5);
my.printout();



