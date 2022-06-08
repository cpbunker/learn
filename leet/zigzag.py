'''
https://github.com/cpbunker/learn/leet

6. Zigzag Conversion
'''


def solution(s: str, numRows: int) -> str:
    '''
    reorder the string s in the zigzag pattern
    '''

    # calculate the number of steps between values in each row
    rowSteps = [];
    if(numRows == 1):
        rowSteps.append([1,1]); # no skipping
    else:
        for rowi in range(numRows):
            maxStep = 2 + (numRows-2)*2;
            rowsFromEdge = min(rowi, numRows - 1 - rowi);
            thisStep = 2 + (numRows-2-rowsFromEdge)*2;

            # assign step values, depending on which row
            if(rowi == 0 or rowi == numRows - 1): # double long steps
                rowSteps.append([thisStep, thisStep]);
            elif(rowi > rowsFromEdge): # short step first
                rowSteps.append([maxStep - thisStep, thisStep]);
            else: # long step first
                rowSteps.append([thisStep, maxStep - thisStep]);
    #print(rowSteps)

    # convert the old string by stepping through
    snew = '';
    for rowi in range(numRows):
        si = rowi; # for stepping through
        whichstep = 0; # 0 for long step, 1, for short step
        while(si < len(s)): # step through while in length
            snew += s[si]; # update converted string
            #print(rowi, si)
            si += rowSteps[rowi][whichstep % 2];
            whichstep += 1;

    #assert(len(s) == len(snew));
    return snew;


#### test the soln
mys = 'PAYPALISHIRING';
myn = 3;
print(solution(mys, myn));
    




