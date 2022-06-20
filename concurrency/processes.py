'''
GitHub/cpbunker/learn/concurrency/processes.py
'''

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    num_pros = 5;
    for proi in range(num_pros):
        p = Process(target=f, args=(proi,))
        p.start()
        #p.join() 
