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
O_mol = gto.M(atom="Be 0 0 0;", basis="STO3G", symmetry = "d2h", spin = 0); # mol geomtry
O_dft = scf.UKS(O_mol).run(); # restricted Kohn sham
coeffs, hcore = O_dft.mo_coeff, O_dft.get_hcore(); # unpack DFT results
print( hcore );
print(coeffs);
print(coeffs[0]);

#coeffs by spin
for coeff in coeffs: # tuple of up, down coefs
    norbs = np.shape(coeff)[0]
    nelecs = (O_mol.nelectron//2, O_mol.nelectron//2)

    # convert to h1e and h2e array reps in molecular orb basis
    h1e = np.dot(coeff.T, hcore @ coeff);
    g2e = ao2mo.restore(1, ao2mo.kernel(O_mol, coeff), norbs);
    print("spin dependent:\n",hcore, "\n", h1e, "\n", g2e);

# store as fcidump
assert False;
fcid = fcidump.FCIDUMP(h1e=h1e,g2e=g2e, const_e = O_mol.energy_nuc(), pg = 'd2h', n_sites = norbs, n_elec = sum(nelecs), twos = nelecs[0]-nelecs[1]);
fcid.write("dat/O_atom.FCIDUMP");

######################################################################
#### DMRG ground state

# control dmrg
bdims = [10,20,30];
noises = [1e-4,1e-5,0];

# build hamiltonian as MPO
h_obj = hamiltonian.Hamiltonian(fcid, flat = True);
h_mpo = h_obj.build_qc_mpo();
h_mpo, _ = h_mpo.compress(cutoff=1e-15);
psi_mps = h_obj.build_mps(bdims[0]);

# do dmrg to find gd state vi MPE
mpe_obj = MPE(psi_mps, h_mpo, psi_mps);
dmrg_obj = mpe_obj.dmrg(bdims = bdims, noises = noises);

# compare w/ direct fci (exact result)
fci_mod.direct_FCI(h1e, g2e, norbs, nelecs, verbose = 1);

        

