'''
Functions which are generally helpful in the pyscf enviro
'''

import numpy as np
import matplotlib.pyplot as plt
import pyscf as ps
from pyscf import fci

# useful reference - grab element by atomic number
PeriodicTable = [None,'H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr']

##############################################################
#### file io

def TxtHeaderDict(fname):
    '''
    Data routines save to txt file with header of physical params of form # -
    Read out these lines and save them to a dict
    '''

    # open file, get lines
    f = open(fname, 'r');
    lines = f.readlines();

    # strip off header
    header = []
    for l in lines:
        if(l[0] == '#'):
            header.append(l[2:-1]); # slice off leading #, trailing \n

    # put physical params into dict
    params = {};
    
    # physical params always start with - character
    for l in header:
        if(l[0] == '-'): # is a param

            # find equal sign to delineate string (key) from num (val)
            eq_index = -1
            for i in range(len(l)):
                if(l[i] == '='):
                    eq_index = i; # found equal sign
            assert( eq_index != -1); # check success

            # add everything before = to dict as key, everything after as val
            try: # get param as float if possible
                params[l[2:eq_index-1] ] = float(l[eq_index+2:]);
            except:
                params[l[2:eq_index-1] ] = l[eq_index+2:];

    return params;
    






##############################################################
#### constructing atom geometry dicts

# NB pyscf geometries default to angstrom, so always set unit="Bohr"
# however mole.atom_coords() returns geometry array in Bohr always

# reconfig since mole.atom takes lists, arrays !!

def MonatomicChain(el, n, R, axis = 'x'):
    '''
    Chain of same element atoms separated by distance R
    Args:
    - el, string of eement name
    - n, int, number of atoms in chain
    - R, double, distance between atoms
    - axis, string, tells which axis to run chain along
    '''
    
    # check inputs
    if(el not in PeriodicTable): # only take element names
        raise ValueError("Unsupported element passed to geo constructor\n");
    if(axis not in ['x','y','z']): # just reassign back to default
        axis = 'x';
        
    # make axis an int
    axis = ord(axis) - ord('x'); #map to ascii and subtract to get 0,1,2
    
    # return var is dict
    d = dict();
    
    for i in range(n):
    
        # construct coords based on which axis chain is along
        coords = np.zeros(3);
        coords[axis] = R*i; #update with correct number chain lengths
        d[el+str(i)] = coords
        
    return d;


##############################################################
#### interpreting atom geometry dicts

def ParseGeoDict(d):
    '''
    Given a dictionary of element names : cartesian coordinates np array,
    turn into a string formatted to pass to the mol.atom attribute
    '''
    
    # return value is string of geometry
    atomstring = '';
    
    # iter over elements aka keys
    for el in d:
    
        # get coords
        coords = d[el];
        coords = str(coords)[1:-1]; # get space seperated #s with [s deleted
        
        # update string
        atomstring += " "+el+" "+coords+";"
        
    return atomstring;


    
    
    
    
##############################################################
#### test code

def TestCode():

    f = "dat/DotCurrentData/3_1_3_e7_mu-1.0_Vg-0.5_J.txt"
    TxtHeaderDict(f);
    
    
if __name__ == "__main__":

    TestCode();

