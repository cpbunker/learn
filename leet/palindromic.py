'''
https://github.com/cpbunker/learn/leet

5. Longest Palindromic Substring
'''

import time

def solution(s: str, method = 'brute', comp = False) -> str:
    '''
    Given string s, find the longest interior palindrome, case-sensitive
    longest is not unique, in case of ties use first occuring
    '''

    if(method == 'brute'):

        # complexity info
        n_subs = 0;
        n_checks = 0;

        # default answer is first char
        sol = s[0];

        # iter over longer
        for starti in range(len(s)):
            for stopi in range(starti+len(sol)+1,len(s)+1): # only check longer
                sub = s[starti:stopi]; # sub will cover all longer substrings
                
                # reassign sol if needed
                if(is_palindromic(sub)): # check palindrome status
                    sol = sub;

                # complexity info
                n_subs += 1;
                n_checks += 1;
        if(comp): print(len(s)," "*(10-len(str(len(s)))), len(sub)," "*(10-len(str(len(sub)))),n_subs," "*((10-len(str(n_subs)))),n_checks);   
                    
        return sol;

    elif(method == 'fast'):

        # complexity info
        n_subs = 0;
        n_checks = 0;

        # default answer is first char
        sol = s[0];

        # iter over longer
        for starti in range(len(s)):
            for stopi in range(starti+1,min(starti + 3, len(s))): # 2-3 char sub
                sub = s[starti:stopi+1]; # +1 bc indices are always inclusive
                print(starti, stopi, sub)
                n_subs += 1;
                n_checks += 1;
                
                # check palindrome 
                if(sub[0] == sub[-1]):
                    newstarti, newstopi = starti-1, stopi+1; # recall indices should still be inclusive

                    # keep expanding while still a palindrome and still in string
                    while( newstarti >= 0 and newstopi < len(s) and s[newstarti] == s[newstopi]): 
                        sub = s[newstarti:newstopi+1];
                        print("->", newstarti, newstopi, sub)
                        newstarti -= 1;
                        newstopi += 1;
                        n_checks += 1;

                    # reassign sol if needed
                    if(len(sub) > len(sol)):
                        sol = sub;

        # complexity info
        #if(comp): print(len(s)," "*(10-len(str(len(s)))), len(sub)," "*(10-len(str(len(sub)))),n_subs," "*((10-len(str(n_subs)))),n_checks);
        
        return sol;

# test
tries = ['aba7','9racecare9','civil','cbbd','bbbbbbb8'];
print("len(try)"," "*(2), "len(sub)"," "*(2),"n_subs"," "*(4),"n_checks");
print("-"*50);
for tri in tries:
    my = solution(tri, method = 'fast', comp = True);
    print(tri, ' -> ',my)
    



