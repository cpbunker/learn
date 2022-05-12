'''
https://github.com/cpbunker/learn/leet

1. Two Sum
'''

import time
import random

def solution(nums: list[int], target: int, method = 'ifin') -> list[int]:
    '''
    takes a list of nums for which there is one pair s.t.
    nums[i] + nums[j] == target, and returns indices i,j
    '''

    if(method == 'brute'):
        for i1 in range(len(nums)):
            for i2 in range(len(nums)):
                if(nums[i1] + nums[i2] == target):
                    return [i1, i2];

    if(method == 'ifin'):
        for i1 in range(len(nums)):
            complement = target - nums[i1];
            if complement in nums: # speedup 
                for i2 in range(len(nums)):
                    if(nums[i1] + nums[i2] == target):
                        return [i1, i2];

def screen(nums: list[int], target: int) -> bool:
    '''
    makes sure there is exactly one unique solution to above
    '''

    counter = 0;
    for n1 in nums:
        for n2 in nums:
            if(n1 + n2 == target):
                counter += 1;
    return(counter == 2);


#### test the soln
mynums = list(range(-10000,-100));
mynums.append(4)
mynums.append(5);
myt = 9

# randomize mynums
random.shuffle(mynums);
if screen(mynums, myt):
    start = time.time();
    inds = solution(mynums, myt);
    stop = time.time();
    print("Time = ", stop - start);
    assert(mynums[inds[0]]+mynums[inds[1]] == myt); 
    




