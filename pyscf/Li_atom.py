#!/usr/bin/env python

'''
First principles lithium --> scattering
'''

import fci_mod

import numpy as np
from pyscf import gto, scf, mcscf, lo, tools, ao2mo, symm
from pyblock3 import fcidump, hamiltonian, algebra
from pyblock3.algebra.mpe import MPE

######################################################################
#### DFT on Li

# basics
nelecs = (0,1);

# set up molecule geometry and solve with DFT
Li_mol = gto.M(atom="H 0 0 0;", basis="STO3G", symmetry = "d2h", spin = nelecs[0] - nelecs[1]); # mol geomtry
Li_dft = scf.RKS(Li_mol).run(); # do unrestricted Kohn sham
coeffs, h1e, g2e = Li_dft.mo_coeff, Li_dft.get_hcore(), Li_dft._eri; # unpack results
print(h1e,"\n",g2e);
assert False;

# store as fcidump
norbs = np.shape(h1e)[0];
fcid = fcidump.FCIDUMP(h1e=h1e,g2e=g2e, const_e = H_mol.energy_nuc(), pg = 'd2h', n_sites = norbs, n_elec = sum(nelecs), twos = nelecs[0]-nelecs[1]);
#fcid.write("dat/H_atom.FCIDUMP");

######################################################################
#### DMRG ground state

# control dmrg
bdims = [10,20,30];
noises = [1e-4,1e-5,0];

# build hamiltonian as MPE
mpe_obj = fci_mod.fd_to_mpe(fcid, bdims[0] );

# do dmrg to find gd state vi MPE
dmrg_obj = mpe_obj.dmrg(bdims = bdims, noises = noises);

# compare w/ direct fci (exact result)
fci_mod.direct_FCI(h1e, g2e, norbs, nelecs, verbose = 1);

        

