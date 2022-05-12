'''
https://github.com/cpbunker/learn/leet

5. Longest Palindromic Substring
'''

import time

def solution(s: str, method = 'brute') -> str:
    '''
    Given string s, find the longest interior palindrome, case-sensitive
    longest is not unique, in case of ties use first occuring
    '''

    def is_palindrome(subs: str) -> bool:

        # front of string
        front = subs[:len(subs)//2];

        # back of string, reversed
        back = subs[::-1][:len(subs)//2];

        return(front == back);
            

    if(method == 'brute'):

        # default answer is first char
        default = s[0];

        # iter over longer

        return default;

    if(method == 'fast'):
        return;


# test
s = "civilizationivbeyondthesword";
s = "babad"
start = time.time();
pal = solution(s);
stop = time.time();
print("Solution = ",pal);
print("Time = ", stop - start);



