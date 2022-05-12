'''
https://github.com/cpbunker/learn/leet

3. Longest Substring Without Repeating
'''

import time
import random

def solution(s: str, method = 'brute') -> int:
    '''
    '''

    if(method == 'brute'):
        counter = 0; # holds the length of longest substring at given time

        # iter over all start and end chars -> all possible substrings
        for starti in range(len(s)):
            for stopi in range(starti,len(s)):
                sub = s[starti:stopi+1];
                if(len(sub) > counter): # else don't bother
                    # iter over substring for repition
                    sub_good = True;
                    for i in range(len(sub)):
                        for j in range(len(sub)):
                            if(i != j and sub[i] == sub[j]):
                                sub_good = False; # there is repitition
                    if(sub_good):
                        counter = len(sub);

        # return length of longest substring
        return counter

    if(method == 'fast'):
        counter = 0; # stores length of longest substring at given time
        
        # special case
        if(len(s) == 1):
            return 1;
        
        # iter over all possible substrings
        for starti in range(len(s)):
            if(len(s) - starti > counter): # else don't bother
                for stopi in range(starti+1,len(s)):

                    # check for end of string or repition
                    if(s[stopi] in s[starti:stopi]):
                        counter = max(counter,stopi-starti);
                        break;
                    elif(stopi == len(s) - 1):
                        counter = max(counter, len(s) - starti);
                        break
                        
        return counter;

#### test the soln
mystr = "civilizationivbeyondthesword";
start = time.time();
sol = solution(mystr);
stop = time.time();
print("\nSolution:",sol);
print("Time = ", stop - start);
    




