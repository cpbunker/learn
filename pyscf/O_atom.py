#!/usr/bin/env python

'''
First principles + DMRG on oxygen
'''

import fci_mod

import numpy as np
from pyscf import gto, scf, mcscf, lo, tools, ao2mo, symm
from pyblock3 import fcidump, hamiltonian, algebra
from pyblock3.algebra.mpe import MPE

######################################################################
#### DFT on O2

# set up molecule geometry and solve with DFT
O_mol = gto.M(atom="O 0 0 0;", basis="STO3G", symmetry = "d2h"); # mol geomtry
O_dft = scf.RKS(O_mol).run(); # restricted Kohn sham
nelecs = (O_mol.nelectron//2, O_mol.nelectron//2)

# convert to h1e and h2e array reps in molecular orb basis
h1e, g2e = fci_mod.scf_to_arr(O_mol, O_dft);

# store as fcidump
norbs = np.shape(h1e)[0];
fcid = fcidump.FCIDUMP(h1e=h1e,g2e=g2e, const_e = O_mol.energy_nuc(), pg = 'd2h', n_sites = norbs, n_elec = sum(nelecs), twos = nelecs[0]-nelecs[1]);
fcid.write("dat/O_atom.FCIDUMP");

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

        

