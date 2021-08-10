#!/usr/bin/env python

'''
First principles + DMRG on N2
'''

import numpy as np
from pyscf import gto, scf, mcscf, lo, tools, ao2mo, symm
from pyblock3 import fcidump, hamiltonian, algebra
from pyblock3.algebra.mpe import MPE

######################################################################
#### DFT on N2

# set up molecule geometry and solve with DFT
R = 1.2; # bond length
N2_mol = gto.M(atom="N 0 0 0; N 0 0 "+str(R), basis="STO3G", symmetry = "d2h"); # mol geomtry
N2_dft = scf.RKS(N2_mol).run(); # restricted Kohn sham
coeffs, hcore = N2_dft.mo_coeff, N2_dft.get_hcore(); # unpack DFT results
norbs = np.shape(coeffs)[0]
nelecs = (N2_mol.nelectron//2, N2_mol.nelectron//2)

# convert to h1e and h2e array reps in molecular orb basis
h1e = np.dot(coeffs.T, hcore @ coeffs);
g2e = ao2mo.restore(1, ao2mo.kernel(N2_mol, coeffs), norbs);

# store as fcidump
fcid = fcidump.FCIDUMP(h1e=h1e,g2e=g2e, const_e = N2_mol.energy_nuc(), pg = 'd2h', n_sites = norbs, n_elec = sum(nelecs), twos = nelecs[0]-nelecs[1]);
fcid.write("N2_mol.FCIDUMP");

######################################################################
#### DMRG ground state

# control dmrg
bdims = [100,200,300];
noises = [1e-6,1e-7,0];

# build hamiltonian as MPO
h_obj = hamiltonian.Hamiltonian(fcid, flat = True);
h_mpo = h_obj.build_qc_mpo();
h_mpo, _ = h_mpo.compress(cutoff=1e-9);
psi_mps = h_obj.build_mps(bdims[0]);

# do dmrg to find gd state vi MPE
mpe_obj = MPE(psi_mps, h_mpo, psi_mps);
dmrg_obj = mpe_obj.dmrg(bdims = bdims, noises = noises);
                    




        

