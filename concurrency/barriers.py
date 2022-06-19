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

class H2O:

    def __init__(self, n: int):

        # init
        self.n = n;
        self.stdout = '';

        # construct threads
        self.Hthread = ThreadManager('H', self.hydrogen, ());
        self.Othread = ThreadManager('O', self.oxygen, ());

        # start threads
        self.Hthread.start();
        self.Othread.start();

        # keep going till threads finish
        while(self.Hthread.running() or self.Othread.running()):
            time.sleep(1);

    def printout(self):
        print("\nFooBar stdout: ",self.stdout);

    def status(self):
        print("\nFooBar status:");
        print(" - foothread running: ",self.foothread.running());
        print(" - barthread running: ",self.barthread.running());

    def hydrogen(self):
        for i in range(2*self.n):
            self.stdout += 'H';

    def oxygen(self):
        for i in range(self.n):
            self.stdout += 'O';
            




my = H2O(2);
my.printout();



