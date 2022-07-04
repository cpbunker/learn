'''
https://github.com/cpbunker/learn/leet

Testing optimization of list based code
'''

import time
import random
import itertools
import matplotlib.pyplot as plt

#### finding number of unique pairs with correct difference

def pairs(target, arr, method = 'brute') -> int:

    if method == 'brute':
        length = len(arr);
        diffs = 0;
        for i in range(length):
            for j in range(i+1,length):
                if abs(arr[i] - arr[j]) == target:
                    diffs += 1;
        return diffs;

    elif method == 'listcomp':
        length = len(arr);
        diffs = [1 for i in range(length) for j in range(i+1,length) if abs(arr[i] - arr[j]) == target];
        return len(diffs);

    elif method == 'set':
        setarr = set(arr);
        setplus = [el+target for el in arr];
        diffs = setarr.intersection(setplus);
        return len(diffs);

    else:
        raise NotImplementedError;

if False:

    xvals = range(1000,10000,1000);
    t1vals = [];
    t2vals = [];
    for xmax in xvals:

        mymax = 1000
        maxlength = 4;
        myl = [random.randint(0,mymax) for _ in range(xmax)];

        # do brute force
        start = time.time();
        normd = ['0'*(maxlength - len(s))+s for s in myl];
        stop = time.time();
        t1vals.append(stop - start);

        # do list comp
        start = time.time();
        normd = [''.join(['0'*(maxlength)])]
        stop = time.time();
        t2vals.append(stop - start);

if False:

    xvals = range(1000,10000,1000);
    t1vals = [];
    t2vals = [];
    t3vals = [];
    for xmax in xvals:

        target = random.randint(0,100);

        # construct unique list by shuffling a list 4* as long and taking first quarter
        longlist = list(range(xmax*4));
        random.shuffle(longlist);
        myl = longlist[:xmax];

        # do brute force
        start = time.time();
        ret = pairs(target, myl, method = 'brute');
        stop = time.time();
        t1vals.append(stop - start);

        # do list comp
        start = time.time();
        ret = pairs(target, myl, method = 'listcomp');
        stop = time.time();
        t2vals.append(stop - start);

        # do list comp
        start = time.time();
        ret = pairs(target, myl, method = 'set');
        stop = time.time();
        t3vals.append(stop - start); 
    

#### list comp vs itertools

def f(x):
    if x>3:
        return 1
    else:
        return 0

if True:
    
    xvals = range(10000,200000,20000);
    t1vals = [];
    t2vals = [];
    for xmax in xvals:

        myl = [random.randint(0,1000) for _ in range(xmax)];

        # do [::-1]
        start = time.time();
        for el in range(10,200):
            if el in myl:
                pass;
        stop = time.time();
        t1vals.append(stop - start);

        # do reversed
        start = time.time();
        myset = set(myl);
        for el in range(10,200):
            if el in myset:
                pass;
        stop = time.time();
        t2vals.append(stop - start);   

#### visualize
import matplotlib.pyplot as plt
plt.plot(xvals, t1vals, color = 'blue');
plt.plot(xvals, t2vals, color = 'red');
try: plt.plot(xvals, t3vals, color = 'green');
except: pass;
plt.show();



