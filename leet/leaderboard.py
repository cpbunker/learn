'''
https://github.com/cpbunker/learn/leet

Week 3: Climbing the Leaderboard (HackerRank)
'''

import time
import random

def climbingLeaderboard(ranked, player, method = 'brute'):
    '''
    Args
    -ranked, list of m positive integers, descending order
    -players, list of n positive integers in ascending order
    '''

    if(method == 'brute'):

        # form dense leaderboard
        rankeddense = [];
        for r in ranked:
            if r not in rankeddense:
                rankeddense.append(r);
        rankeddense.sort(reverse = True); # dense scores in descending order

        # convert player scores to rank
        pranks = [];
        for pscore in player:
            appended = False;
            for rscorei in range(len(rankeddense)):
                if(pscore >= rankeddense[rscorei]):
                    pranks.append(rscorei + 1);
                    appended = True;
                    break; # only one append per rscore
            if not appended: # this score is last
                pranks.append(len(rankeddense)+1)
        return pranks;

    elif(method == 'fast'):

        # form dense leaderboard as dict with key scores and values dense rank
        rankedhist = dict();
        
        # combine ranked and player scores into hist and offset later
        rankedex = ranked[:]; # copy
        rankedex.extend(player);
        rankedex.sort(reverse = True); # descending, so ranked[i] is i+1th rank
        counter = 1;
        for r in rankedex:
            if r not in rankedhist:
                rankedhist[r] = counter;
                counter += 1; # update rank counter only at unique r's

        # get player scores from hist
        pranks = []; # return value
        appears = [1 if p in ranked else 0 for p in player];
        # iter over player scores
        for pscorei in range(len(player)):
            prank = rankedhist[player[pscorei]]; # rank is value, score is key
            # need to ignore all the players higher scores (dont count yet)
            ignore = len(player) - (pscorei+1);
            # however, if a higher player score appears in ranked, dont ignore!
            # so we count 1 for every subsequent score in player, also in ranked
            dontignore = sum(appears[pscorei+1:])
            #print("->",player[pscorei],prank, ignore, dontignore);
            pranks.append(prank - ignore + dontignore);

        return pranks;

    else:
        raise NotImplementedError;


    
####

rs = [100, 90, 90, 80, 75, 60];
ps = [0, 65, 77, 90, 100];
answer = climbingLeaderboard(rs, ps, method = 'fast');
print(answer);
assert False

# test time complexity
score_range = (0,10**2)
n = 5; # num player scores
mvals = [5] # list( range(500,10000,500));
tvals_b, tvals_f = [], [];
for m in mvals:

    player = [random.randint(*score_range) for _ in range(n)];
    player.sort(); # acending
    ranked = [random.randint(*score_range) for _ in range(m)];
    ranked.sort(reverse = True); # descending

    # do brute operation
    start = time.time();
    bans = climbingLeaderboard(ranked, player, method = 'brute');
    stop = time.time();
    tvals_b.append(stop - start);

    # do fast operation
    start = time.time();
    fans = climbingLeaderboard(ranked, player, method = 'fast');
    stop = time.time();
    tvals_f.append(stop - start);

    if(bans != fans):
        print(ranked);
        print(player);
        assert False;

# visualize
import matplotlib.pyplot as plt
plt.plot(mvals, tvals_b, color = 'blue');
plt.plot(mvals, tvals_f, color = 'red');
plt.show();



