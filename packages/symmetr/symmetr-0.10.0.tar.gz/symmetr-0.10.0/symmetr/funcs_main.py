from __future__ import print_function
from __future__ import absolute_import
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from builtins import str
from builtins import range
import re
import sys
import os
import time
from collections import defaultdict
from itertools import combinations

from . import symmetrize
from . import symmetrize_exp as st
from . import fslib
from . import find_eq
from . import symT
from . import mham
from . import groups
from .tensors import Tensor,matrix,NumTensor
from . import symmetry

import sympy
from sympy import sympify as spf

__all__ = ['def_symmetr_opt', 'sym_res_nonexp', 'sym_res_exp', 'sym_res', 'sym_mham']

#this finds the location of the main.py file and ads this location to the path where modules are searched
#this way the modules have to be present only in the install directory and not in the run directory
dirname, filename = os.path.split(os.path.abspath(__file__))
sys.path.append(str(dirname))

def def_symmetr_opt(opt):
    s_opt = symmetrize.SymmetrOpt(num_prec=opt['num_prec'],
                                   debug=opt['debug_sym'],
                                   debug_time=opt['debug_time'],
                                   debug_Y=opt['debug_symY'],
                                   round_prec=opt['round_prec'],
                                   numX=opt['numX'])
    return s_opt

def get_tensor_class(opt):
    if opt['numX']:
        return NumTensor
    else:
        return Tensor

def reorder_configuration(C,C2):
    C2_new = find_eq.confs()
    for conf in C.confs:
        for conf2 in C2.confs:
            same = True
            for mi in C.confs[conf]:
                dif = C.confs[conf][mi] - C2.confs[conf2][mi]
                for i in range(3):
                    if dif[i].round(4) != 0:
                        same = False
            if same:
                C2_new.add(C.confs[conf],C2.Xs[conf2])
    return C2_new

def find_equivalent_pairs(ops,index_shift=0):

    # Group indices by string value
    groups = defaultdict(list)
    for i, s in enumerate(ops):
        groups[s].append(i)

    # Create all index pairs inside each group
    result = []
    for indices in groups.values():
        if len(indices) > 1:
            # Take all 2-combinations of indices
            for i, j in combinations(indices, 2):
                result.append((i+index_shift,j+index_shift))

    # Join with ":" for final string
    return result

def determine_sym_inds(opt):
    if any(x is not None for x in [opt['sym_inds'], opt['asym_inds'], opt['T_sym_inds'], opt['T_asym_inds']]):
        symmetrize_sym_inds = True
        sym_inds = opt['sym_inds']
        asym_inds = opt['asym_inds']
        T_sym_inds = opt['T_sym_inds']
        T_asym_inds = opt['T_asym_inds']
    else:

        asym_inds = None
        T_sym_inds = None
        T_asym_inds = None

        ops1 = opt['op_types'][:opt['op_lengths'][0]]
        ops2 = opt['op_types'][-opt['op_lengths'][1]:]
        sym_inds1 = find_equivalent_pairs(ops1)
        sym_inds2 = find_equivalent_pairs(ops2,index_shift=len(ops1))

        if len(sym_inds1) > 0 or len(sym_inds2) > 0:
            symmetrize_sym_inds = True
            sym_inds = sym_inds1 + sym_inds2
            sym_inds_out = [(x[0]+1,x[1]+1) for x in sym_inds]
            print('Symmetrizing indices: {}.'.format(sym_inds_out))
        else:
            symmetrize_sym_inds = False
            sym_inds = None
    return symmetrize_sym_inds, sym_inds, asym_inds, T_sym_inds, T_asym_inds

def sym_res_nonexp(opt,printit=False):

    #the symmetry operations given in the basis used by findsym
    if opt['noso']:
        syms = symT.get_syms_noso(opt)
    else:
        syms = symT.get_syms(opt)

    #transformation matrix from the basis used by findsym to the user defined basis
    T = symT.get_T(opt)
    if opt['num_prec'] is not None:
        T = sympy.N(T)
    #if transform_result is not set we transform the symmetries
    if not opt['transform_result']:
        for sym in syms:
            sym.convert(T,in_place=True)

    op_contravar = (1,)*opt['op_lengths'][0] + (-1,)*opt['op_lengths'][1]

    op_types = opt['op_types']
    TensorClass = get_tensor_class(opt)
    X1 = TensorClass('s', 3, len(op_types), ind_types=op_contravar)

    if opt['T_permute_inds']:
        permutation = {}
        for i in range(X1.dim2):
            permutation[i] = i
        for inds in opt['T_permute_inds']:
            permutation[inds[0]] = inds[1]
            permutation[inds[1]] = inds[0]
    else:
        permutation = None

    X1.def_trans(ind_trans=op_types, T_comp=-1, permute_inds = permutation)

    X2 = TensorClass('s', 3, len(op_types), ind_types=op_contravar)
    X2.def_trans(ind_trans=op_types, T_comp=1 ,permute_inds = permutation)

    if permutation is not None:
        permutation
    eo = symmetrize.even_odd([X1,X2])

    same_op_sym = False
    if opt['same_op_sym']:
        same_op_sym = determine_onsager(opt['op_types'], opt['op_lengths'])
        if same_op_sym:
            print('Applying Onsager relations.')
    symmetrize_sym_inds, sym_inds, asym_inds, T_sym_inds, T_asym_inds = determine_sym_inds(opt)

    if same_op_sym or symmetrize_sym_inds:
        #the metric is for the findsym basis
        G = symT.get_metric(opt,debug=False)
        if opt['num_prec'] is not None:
            G = sympy.N(G)
        if not opt['transform_result']:
            G = T * G * T.T

        X1.def_metric(G)
        X2.def_metric(G)

    s_opt = def_symmetr_opt(opt)

    Xs = []
    Xs.append(symmetrize.symmetrize_res(syms,X1,opt['atom'],s_opt))
    Xs.append(symmetrize.symmetrize_res(syms,X2,opt['atom'],s_opt))

    if same_op_sym:
        for i in range(2):
            Xs[i] = symmetrize.symmetrize_same_op(Xs[i],s_opt)
    
    if symmetrize_sym_inds:
        for i in range(2):
            Xs[i] = symmetrize.symmetrize_sym_inds(Xs[i],sym_inds,asym_inds,T_sym_inds,T_asym_inds,s_opt)

    if opt['atom2'] != -1:
        Xs_2 = symmetrize.symmetr_AB(syms,Xs,opt['atom'],opt['atom2'],round_prec=opt['round_prec'])
        if Xs_2 is None:
            raise Exception('Did not find symmetry connecting the two atoms!')

    #if transform result is set we convert the symmetrized tensor
    if opt['transform_result']:
        for i in range(2):
            Xs[i].convert(T)
        if opt['atom2'] != -1:
            for i in range(2):
                Xs_2[i].convert(T)


    if opt['numX']:
        for i in range(2):
            Xs[i] = Xs[i].convert2tensor(opt['num_prec'])
        if opt['atom2'] != -1:
            for i in range(2):
                Xs_2[i] = Xs_2[i].convert2tensor(opt['num_prec'])

    if printit:
        print('{0} part of the response tensor:'.format(eo[0]))
        Xs[0].pprint(print_format=opt['print_format'])
        if opt['latex']:
            Xs[0].pprint(print_format=opt['print_format'],latex=True)
        print('{0} part of the response tensor:'.format(eo[1]))
        Xs[1].pprint(print_format=opt['print_format'])
        if opt['latex']:
            Xs[1].pprint(print_format=opt['print_format'],latex=True)

        
        if opt['atom2'] != -1:
            if Xs_2 is None:
                print('no relation with atom %s found' % opt['atom2'])
            else:
                print('First part of the response tensor, atom %s' % (opt['atom2']))
                Xs_2[0].pprint(print_format=opt['print_format'])
                if opt['latex']:
                    Xs_2[0].pprint(print_format=opt['print_format'],latex=True)
                print('Second part of the response tensor, atom %s' % (opt['atom2']))
                Xs_2[1].pprint(print_format=opt['print_format'])
                if opt['latex']:
                    Xs_2[1].pprint(print_format=opt['print_format'],latex=True)
                print('')
    
    if opt['equiv']:

        mags = symT.get_mags(opt['inp']) #magnetic moments 
        syms_nm = symT.get_syms_nonmag(opt) #the symmetry operations for nonmagnetic system

        Tm = symT.get_Tm(opt['inp']) #transformation matrix from the input basis to the basis used by findsym
        #transformation matrix form the input basis to the basis used by findsym for nonmagnetic system 
        Tnm = symT.get_Tm(opt['inp'],nonmag=True) 

        #magnetic moments are in the input basis, we need to convert them to the user selected basis
        #First convert to the magnetic findsym basis and from that to the user selected one.
        mags = symT.convert_vecs(mags,T*Tm.inv())
        #The symmetry operations are in the findsym uses for nonmagnetic input. We first transform to the input
        #basis, then to the magnetic findsym basis and then to the user chosen one.
        T2 = T*Tm.inv()*Tnm
        for sym in syms_nm:
            sym.convert(T2,in_place=True)

        C = find_eq.find_equiv(Xs,mags,syms_nm,opt['atom'],debug=opt['debug_equiv'],round_prec=opt['round_prec'])
        if opt['atom2'] != -1:
            C2 = find_eq.find_equiv(Xs_2,mags,syms_nm,opt['atom2'],debug=opt['debug_equiv'],round_prec=opt['round_prec'])
            #The order of the magnetic configurations in C2 can be different than in C, so we reorder them
            C2 = reorder_configuration(C,C2)
        if printit:
            print('')
            print('Equivalent configurations:')
            C.pprint(print_format=opt['print_format'])
            if opt['atom2'] != -1:
                print('Equivalent configurations for atom 2')
                C2.pprint(print_format=opt['print_format'])
    
    if opt['atom2'] == -1:
        if opt['equiv']:
            return Xs,C
        else:
            return Xs
    else:
        if opt['equiv']:
            return Xs,C,Xs_2,C2
        else:
            return Xs,Xs_2

def sym_res_exp(opt,printit=False):
    """
    Finds the tensor describing expansion term of linear response in the direction of magnetization.

    Args:
        opt (class options): stores all the input arguments. Only some are used here.
        printit (optional[boolean]): if true this prints the output
    """

    if opt['group']:
        print('!!!The input group must be one of the nonmagnetic point groups, otherwise the ouput will be wrong.!!!') 
        syms_nm = symT.get_syms(opt)
        T = symT.get_T(opt)
        mags = []
    else:
        T = symT.get_T(opt,nonmag=True)
        syms_nm = symT.get_syms_nonmag(opt)
        mags = symT.get_mags(opt['inp'])

    if not opt['transform_result']:
        for sym in syms_nm:
            sym.convert(T,in_place=True)
        mags = symT.convert_vecs(mags,T)

    syms_L = st.def_syms_L(mags,syms_nm,debug=False)

    op_contravar = (1,)*opt['op_lengths'][0] + (-1,)*opt['op_lengths'][1] + (-1,) * opt['exp']
    op_types = opt['op_types'] + ['N'] * opt['exp']
    TensorClass = get_tensor_class(opt)
    X = TensorClass('s', 3, len(op_types), ind_types=op_contravar)
    X.def_trans(ind_trans=op_types,T_comp=1)
    T_inv = symmetry.create_T()
    T_inv.def_custom_R('N',T_inv.Rs)
    if not X.is_even(T_inv):
        X.def_trans(ind_trans=op_types,T_comp=-1)
    s_opt = def_symmetr_opt(opt)

    symmetrize_sym_inds, sym_inds, asym_inds, T_sym_inds, T_asym_inds = determine_sym_inds(opt)

    same_op_sym = False
    if opt['same_op_sym']:
        same_op_sym = determine_onsager(opt['op_types'], opt['op_lengths'])
        if same_op_sym:
            print('Applying Onsager relations.')

    if same_op_sym or symmetrize_sym_inds:
        #the metric is for the findsym basis
        G = symT.get_metric(opt,False,nonmag=True)
        if opt['num_prec'] is not None:
            G = sympy.N(G)
        if not opt['transform_result']:
            G = T * G * T.T

        X.def_metric(G)

    X = symmetrize.symmetrize_res(syms_L,X,opt['atom'],s_opt)

    if symmetrize_sym_inds:
        X = symmetrize.symmetrize_sym_inds(X,sym_inds,asym_inds,T_sym_inds,T_asym_inds,s_opt)

    if same_op_sym:
        X = symmetrize.symmetrize_same_op(X,s_opt)

    if opt['transform_result']:
        X.convert(T)

    n_op = opt['op_lengths'][0] + opt['op_lengths'][1]
    if opt['numX']:
        t1 = time.perf_counter()
        X = X.convert2tensor(opt['num_prec'])
        #X = X.convert2tensor(None)
        t2 = time.perf_counter()
    Xm = st.sub_m(X,n_op)

    if printit:
        Xm.pprint()
        if opt['latex']:
            Xm.pprint(latex=True,no_newline=no_newline)  

    return Xm

def sym_res(opt,printit=False):
    """A wrapper function that returns the appropriate response tensor based on the input options.

    Args:
        opt (class options): stores all the input arguments. Only some are used here.
        printit (optional[boolean]): if true this prints the output
    """
    if printit and opt['group'] is not None:
        group_name,group_num = groups.find_group(opt['group'])
        print('group name: ', group_name, 'group number: ', group_num)
    if opt['exp'] == -1:
        return sym_res_nonexp(opt,printit=printit)
    else:
        return sym_res_exp(opt,printit=printit)

def sym_mham(opt,printit=False):
    T = symT.get_T(opt,nonmag=True)
    syms = symT.get_syms_nonmag(opt)

    if not opt['transform_result']:
        for sym in syms:
            sym.convert(T,in_place=True)

    s_opt = def_symmetr_opt(opt)
    H = mham.sym_mag_ham(opt['sites'],syms,None,s_opt)

    if opt['transform_result']:
        #H = mham.convert_mag_ham(H,T)
        H.convert(T)

    if opt['equiv']:
        print("WARNING!!! The equivalent sites feature is not fully implemented. When determining the equivalent sites"
              "the program does not take into account the unit cell of the atom. This means the result can be incomplete"
              "or even wrong.\n")
        H_E = mham.equiv(H,opt['sites'],syms,T)

    if printit:
        if H.dim2 == 2:
            print('Hamiltonian term in matrix form:')
            H.pprint(latex=opt['latex'])
            print('')
        mham.print_Ham(H,opt['sites'],latex=opt['latex'])
        if opt['equiv']:
            print('')
            print('Hamiltonian terms for all equivalent combinations of sites:')
            for sites in H_E:
                print(str(sites)+':')
                mham.print_Ham(H_E[sites],sites,latex=opt['latex'])
                print('')
    if not opt['equiv']:
        return H
    else:
        return H,H_E

def determine_onsager(op_types,op_lengths):
    if op_lengths[0] == 1 and op_lengths[1] == 1:
        if op_types[0] == 'j' and (op_types[1] in ['E','V']):
            return True
        if op_types[1] == 'j' and (op_types[0] in ['E','V']):
            return True
        if op_types[0] == 'jq' and op_types[1] == 'gT':
            return True
        if op_types[1] == 'jq' and op_types[0] == 'gT':
            return True
    return False


