# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Module for parsing user input."""
from __future__ import absolute_import
from __future__ import division

from builtins import range
from past.utils import old_div
from builtins import object
import argparse
import sys
import textwrap
from math import log10
from .version import __version__
from .magndata import get_magndata_structure
import sys
import numpy as np

__all__ = ['options', 'parse', 'create_symmetr_input']

class InputError(Exception):
    pass

class options(object):
    """Class to store all the input options.

    Is meant to be used only in conjuction with the parse function.
    Initialize by running
        opt = options(args),
    where args is a dictionary of all arguments.
    Check method controls whether there are comflicting options, however this is not complete and it does not
    check whether the options have allowed values!
    You can access the options by:
        opt['option']
    and also change by:
        opt['option'] = new_value
    """
    def __init__(self,args):
        """During init only the mandatory arguments are set, the rest are set to default values."""
        self.args = args
        self.check()

    def __setitem__(self,key,value):
        self.args[key] = value
        #The checking is a problem when magndata is used and is probably not really necessary
        #should be enough to do the check on creation
        #self.check()

    def __getitem__(self,key):
        return self.args[key]

    def __str__(self):
        return self.args.__str__()

    def check(self):
        if self['transform_result'] and self['transform_syms']:
            raise InputError('You cannot specify both --transform-result and --transform-syms')

        inputs = [self['inp'], self['group'], self['inp_magndata']]
        inputs2 = []
        for inp in inputs:
            if inp is not None:
                inputs2.append(inp)

        if len(inputs2) == 0:
            raise InputError('You have to specify either input file, magndata id or a group.')

        if len(inputs2) > 1:
            raise InputError('You have to specify only one of: input file, magndata id or a group.')

        if self['mode'] == 'res':
            if self['atom2'] != -1:
                if self['atom'] == -1:
                    raise InputError('projection2 can be setonly if projection1 is set')

            if ( self['atom'] != -1 or self['atom2'] !=-1 ) and self['group']:
                raise InputError('Projections not possible with group name input. Use Findsym input instead.')

            if self['equiv'] and self['group']:
                raise InputError('Equivalent configurations are not possible with group name input. Use findsym input file.')

            if self['noso'] and self['group']:
                raise InputError('Spin-orbit coupling cannot be ignored when group name is used as an input.')

            #if self['noso'] and (self['equiv'] or (self['exp'] != -1) or (self['atom2'] != -1)):
            #if self['noso'] and (self['equiv'] or (self['exp'] != -1)):
            if self['noso'] and ((self['exp'] != -1)):
                raise InputError('This is not implemented.')

            if (self['equiv']) and self['syms_sel'] != -1:
                raise InputError('You cannot select symmetries when exp or equiv is set since this is not implemented')

            if self['equiv'] and ( self['exp'] != -1 ):
                raise InputError('You cannot use --equiv and --exp together. Equivalent configurations not supported\
                        for expansions.')
            if self['exp'] != -1 and (self['T_sym_inds'] is not None or self['T_asym_inds'] is not None):
                raise InputError('--T-sym-inds and --T-asym-inds cannot be used with expansions.')
        if self['mode'] == 'mham':
            if self['group'] is not None:
                raise InputError('group input is not allowed for mham')
        if not self['inp'] and self['print_pos']:
            raise InputError('print-pos is only possible with findsym input.')

def parse(clargs=None):
    """Parses the input line arguments

    If clargs is not set then this parses the input arguments. Otherwise clargs is a string that contains the input arguments
    like on command line.
    Args:
        clargs (optional[string]): The input arguments to be parsed.
    """

    parser_parent = argparse.ArgumentParser(add_help=False)
    parser_parent.add_argument('-f','--findsym',help='Findsym input file',default=None,dest='inp')
    parser_parent.add_argument('--magndata',help='The id of a structure from MAGNDATA that will be used as an input.',default=None,dest='inp_magndata')
    parser_parent.add_argument('--magndata-filename',help='The name of the file to which the MAGNDATA input will be saved.',default=None,dest='magndata_fname')
    parser_parent.add_argument('-b','--basis',help='Sets a coordinate basis: abc for conventional crystallographic basis, i for the one used in input \
    (default). cart for a cartesian basis in which the input basis is define. \
    abc_c for orthogonalized crystalographic basis (not tested much).',default='cart')
    parser_parent.add_argument('--print-syms',action='store_const',const=True,default=False,help='Prints all symmetry operations.')
    parser_parent.add_argument('--transform-result',action='store_const',const=True,default=False,help=
            'Keep the symmetry operations in findsym basis and transform the result to the correct basis.')
    parser_parent.add_argument('--transform-syms',action='store_const',const=True,default=False,help=\
            'Transform the symmetry operations to the correct basis instead of transforming the result.')
    parser_parent.add_argument('--syms',default=-1,help='Choose which symmetry operations to take, the rest is ignored.\
            Insert symmetry operation numbers separated by commas with no spaces. They are numbered as they appear\
            in the findsym output file. Also can include ranges. Example: 1-3,7,9-12',dest='syms_sel')
    parser_parent.add_argument('--print-opt',action='store_const',const=True,default=False,help='If set all the input options are printed.')
    parser_parent.add_argument('-g','--group',help='group name',default=None)
    parser_parent.add_argument('--latex',action='store_const',const=True,default=False,help='If set, the matrices are printed also in a latex format.')
    parser_parent.add_argument('--print-pos',action='store_const',const=True,default=False,help='If set prints the atomic sites used in\
            findsym.')
    parser_parent.add_argument('--symbolic',action='store_true',default=False,help=
    'If chosen, the symbolical mode will be used. This means that the symmetrization is done exactly without taking \
     into account finie precision of the input. Use carefully as it can fail in some cases !!!')
    parser_parent.add_argument('--num-prec',dest='num_prec',default=1e-3,help='The numerical precision.\
            Within the alghoritm for symmetrizing, two numbers are considered the same when they are closer\
            then num-prec. Default value 1e-3. Setting this the same as precision for findsym should be a safe choice.' )
    parser_parent.add_argument('--round-prec',dest='round_prec',default=None,help='In the numerical mode, this gives the \
            number of digits for rounding. Default value is int(log10(1/num_prec))')
    parser_parent.add_argument('--dont-round',action='store_const',const=True,default=False,help=
            'If selected, no rounding is done.')
    parser_parent.add_argument('--pos-prec',dest='pos_prec',default=None,help='Precision for the positions. \
    This refers to the positions written in the basis of the unic cell vectors. \
    The positions are read from the findsym output.\
    Default value is maximum of 1.1e-5 and findsym precision (second line of the findsym input file.')
    parser_parent.add_argument('--print-format',dest='print_format',default=None,type=int,help='Format for printing')
    parser_parent.add_argument('--version',action='store_const',const=True,default=False,help=
            'Print version.')
    parser_parent.add_argument('--no-numX',action='store_const',const=True,default=False,help=
    '')
    parser_parent.add_argument('--generators',action='store_const',const=True,default=False,help=
    'Tries to find the group generators and use only those for the symmetrization since the symmetry'
    ' is fully determined by the generators. This can increase the speed significantly.'
    'The algorithm is not guaranteed to always find the smallest group of generators.'
    )
    parser_parent.add_argument('--remove-P',action='store_const',const=True,default=False,help=
    'Removes the inversion symmetry from symmetry operations. Useful for phenomena that '
    'are inveriant under inversion. Should not be used with projections!')
    parser_parent.add_argument('--remove-T',action='store_const',const=True,default=False,help=
    'Removes the inversion symmetry from symmetry operations. Useful for phenomena that '
    'are inveriant under inversion.')
    parser_parent.add_argument('--noso-prec',dest='noso_prec',default=1e-3,type=float)
    parser_parent.add_argument('--noso-moment-zero',dest='noso_moment_zero',default=1e-3,type=float)
    parser_parent.add_argument('--noso-debug',dest='noso_debug',default=0,type=int)


    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,\
            description=textwrap.dedent('''\
            There are two modes: res and mham.
                * res is for symmetry of response functions                *
                * mham is for symmetry of magnetic Hamiltonians
            Use symmetr [res,mham] -h for description of input arguments of each mode. '''))
    subparsers = parser.add_subparsers(dest='mode')
    parser_res = subparsers.add_parser('res',parents=[parser_parent])
    parser_mham = subparsers.add_parser('mham',parents=[parser_parent])

    parser_res.add_argument('op1', help='The opeator of which response we are evaluating.',metavar='A')
    parser_res.add_argument('op2', help='The field which induces the response.',metavar='F')
    parser_res.add_argument('-p','--projection',help='Sets a projection on an atom.',default=-1,dest='atom',type=int)
    parser_res.add_argument('-p2','--projection2',help='Sets a projection on a second atom. Tries to find a relation between tensors on the first \
            atom and on the second atom.',default=-1,dest='atom2',type=int)
    parser_res.add_argument('-e','--equivalent',action='store_const',const=True,default=False,help=
            'finds response matrices for equivalent magnetic configurations.',dest='equiv')
    parser_res.add_argument('--no-rename',action='store_true')
    parser_res.add_argument('--debug',help='Controls if debug output is printed. all means all debug output is printed, symmetrize means debug\
            output for symmetrizing, rename for renaming, equiv for finding the equivalent configurations,\
            noso for the symmetry without spin-orbit coupling. op1eqop2 is also possible.',default='')
    parser_res.add_argument('--exp',default=-1,help=\
            'Prints the tensor, which describes the expansion of the linear response tensor in magnetic moments.\
            Choose which order term in the expansion.\
            Only works for ferromagnets and collinear antiferromagnets. In antiferromagnets only for quantities\
            on a sublattice!!!',type=int)
    parser_res.add_argument('--syms-noso',default=-1,help='Like --syms, but fot noso symmetry operations',dest='syms_sel_noso')
    parser_res.add_argument('--noso',action='store_const',const=True,default=False,help=
            'Symmetry without spin-orbit coupling. Very experimental.')
    parser_res.add_argument('--ignore-onsager', '--ignore-same-op-sym',dest='same_op_sym',action='store_false',default=True,
                            help='Turns off automatic application of Onsager relations.')
    parser_res.add_argument('--sym-inds',default=None,
                            help='Specifies symmetric indices. Multiple pairs can be specified, for example: 0,1:2,3.')
    parser_res.add_argument('--asym-inds',default=None,
                            help='Specifies anti-symmetric indices.')
    parser_res.add_argument('--T-sym-inds',default=None,
                            help='Specifies indices that are symmetric for the T-even component and anti-symmetric for the T-odd component')
    parser_res.add_argument('--T-asym-inds',default=None,
                            help='Specifies indices that are anti-symmetric for the T-even component and symmetric for the T-odd component')
    parser_res.add_argument('--T-permute-inds',default=None)



    parser_mham.add_argument('-s','--sites',help='Atomic sites for which the Magnetic Hamiltonian is considered.\
            List of integeres separated by commas with no spaces, e.g. 1,2. Corresponds to the order of the \
            Hamiltonian. Number of sites must be even!',required=True)
    parser_mham.add_argument('--debug',help='Controls if debug output is printed.',default='')
    parser_mham.add_argument('-e','--equivalent',action='store_const',const=True,default=False,\
            help='Finds the magnetic Hamiltonian also magnetic sites related to the input one by a symmetry operation.',\
            dest='equiv')

    if clargs != None:
        args = parser.parse_args(clargs.split())
    else:
        args = parser.parse_args()

    args_dict = vars(args)

    args_dict['debug'] = args_dict['debug'].split(',')

    #set the debug variables
    args_dict['debug_sym'] = False
    args_dict['debug_rename'] = False
    args_dict['debug_equiv'] = False
    args_dict['debug_tensor'] = False
    args_dict['debug_time'] = False
    args_dict['debug_symY'] = False
    args_dict['debug_noso'] = False
    args_dict['debug_op1eqop2'] = False

    if 'symmetrize' in args_dict['debug'] or 'all' in args_dict['debug'] or 'symmetrizeY' in args_dict['debug']:
        args_dict['debug_sym'] = True
    if 'rename' in args_dict['debug'] or 'all' in args_dict['debug']:
        args_dict['debug_rename'] = True
    if 'equiv' in args_dict['debug'] or 'all' in args_dict['debug']:
        args_dict['debug_equiv'] = True
    if 'exp' in args_dict['debug'] or 'all' in args_dict['debug']:
        args_dict['debug_tensor'] = True
    if 'time' in args_dict['debug'] or 'all' in args_dict['debug']:
        args_dict['debug_time'] = True
    if 'symmetrizeY' in args_dict['debug']:
        args_dict['debug_symY'] = True
    if 'noso' in args_dict['debug']:
        args_dict['debug_noso'] = True
    if 'op1eqop2' in args_dict['debug']:
        args_dict['debug_op1eqop2'] = True

    if args_dict['mode'] == 'mham':
        args_dict['sites'] = args_dict['sites'].split(',')
        for i,x in enumerate(args_dict['sites']):
            args_dict['sites'][i] = x

    #this sets the op variables
    def convert_op1(op1):
        if op1 == 'j':
            return 'v'
        elif op1 == 'B':
            return 's'
        else:
            return op1
    def convert_op2(op2):
        if op2 == 'E':
            return 'v'
        elif op2 == 'B':
            return 's'
        else:
            return op2

    if args_dict['mode'] == 'res':
        op_types1 = args_dict['op1'].split('.')
        #for i,op in enumerate(op_types1):
        #    op_types1[i] = convert_op1(op)
        if args_dict['op2'] == '0':
            op_types2 = []
        else:
            op_types2 = args_dict['op2'].split('.')
        #    for i,op in enumerate(op_types2):
        #        op_types2[i] = convert_op2(op)
        args_dict['op_types'] = op_types1 + op_types2
        args_dict['op_lengths'] = (len(op_types1),len(op_types2))
        args_dict['op3'] = None

    if args_dict['symbolic']:
        args_dict['num_prec'] = None
    else:
        args_dict['num_prec'] = float(args_dict['num_prec'])

    if not args_dict['symbolic']:
        if args_dict['round_prec'] is None:
            args_dict['round_prec'] = int(log10(old_div(1,args_dict['num_prec'])))
        else:
            args_dict['round_prec'] = int(args_dict['round_prec'])
        if args_dict['dont_round']:
            args_dict['round_prec'] = None
    
    if args_dict['pos_prec'] is not None:
        args_dict['pos_prec'] = float(args_dict['pos_prec'])

    def parse_sym_inds(sym_inds):
        if sym_inds is not None:
            #sym_inds_c = args_dict['sym_inds'].split('::')
            sym_inds_c = sym_inds.split(':')
            sym_inds = []
            for ind in sym_inds_c:
                if ind != '':
                    (j,Pj) = ind.split(',')
                    sym_inds.append((int(j)-1,int(Pj)-1))

        return sym_inds

    if args_dict['mode'] == 'res':
        sym_inds = parse_sym_inds(args_dict['sym_inds'])
        asym_inds = parse_sym_inds(args_dict['asym_inds'])
        T_sym_inds = parse_sym_inds(args_dict['T_sym_inds'])
        T_asym_inds = parse_sym_inds(args_dict['T_asym_inds'])
        args_dict['sym_inds'] = sym_inds
        args_dict['asym_inds'] = asym_inds
        args_dict['T_sym_inds'] = T_sym_inds
        args_dict['T_asym_inds'] = T_asym_inds
        args_dict['T_permute_inds'] = parse_sym_inds(args_dict['T_permute_inds'])

    if args_dict['generators'] or args_dict['remove_P'] or args_dict['remove_T']:
        args_dict['simplify_syms'] = True
    else:
        args_dict['simplify_syms'] = False

    opt = options(args_dict)

    if opt['inp_magndata'] is not None:

        struct = get_magndata_structure(opt['inp_magndata'])

        if opt['magndata_fname'] is None:
            fname = 'magndata_{}.in'.format(opt['inp_magndata'])
        else:
            fname = opt['magndata_fname']

        print(
"""Downloading data from MAGNDATA. When using these results you should cite MAGNDATA.

Do not abuse: be careful about not overloading MAGNDATA servers.

The input file is saved in "{}". You should check that it is correct. You can use it directly using the -f parameter.
""".format(fname)
        )

        create_symmetr_input(struct, True, fname)
        opt['inp'] = fname

    opt['numX'] = not opt['no_numX']
    if opt['mode'] == 'mham':
        opt['numX'] = False

    if opt['syms_sel'] != -1:
        syms_sel = opt['syms_sel'].split(',')
        syms_sel2 = []
        for i in range(len(syms_sel)):
            if '-' in syms_sel[i]:
                s = syms_sel[i].split('-')
                syms_sel2 += list(range(int(s[0]),int(s[1])+1))
            else:
                syms_sel2.append(int(syms_sel[i]))
        opt['syms_sel'] = syms_sel2

    if (not opt['transform_result']) and (not opt['transform_syms']):
            opt['transform_syms'] = True

    return opt

def create_symmetr_input(struct,magnetic,filename=None,latt_inp_type=2,precision=0.01):
    lattice_parameters = struct.lattice.abc + struct.lattice.angles
    atom_list = [a.name for a in struct.species]
    all_coordinates = [list(a.frac_coords) for a in struct.sites]
    all_mag_vecs = [a.properties['magmom'] for a in struct.sites]
    at = atom_list
    coord = all_coordinates
    vec = all_mag_vecs
    input_findsym = []
    input_findsym.append(' ' + '\n')
    input_findsym.append(str(precision) + '\n')
    if latt_inp_type == 2:
        input_findsym.append('2' + '\n')
        l_param = ' '.join(str(e) for e in lattice_parameters)
        input_findsym.append(l_param + '\n')
    else:
        input_findsym.append('1' + '\n')
        latt_vecs_string = np.array2string(struct.lattice.matrix).replace('[','').replace(']','')
        latt_vecs_string = latt_vecs_string.split('\n')
        for latt_vec in latt_vecs_string:
            input_findsym.append(latt_vec+'\n')
    input_findsym.append('2' + '\n')
    input_findsym.append('P' + '\n')
    input_findsym.append(str(len(at)) + '\n')
    input_findsym.append(' '.join(at) + '\n')
    if magnetic == True:
        input_findsym.append('magnetic' + '\n')
        for i in range(len(at)):
            if i < len(at) - 1:
                input_findsym.append(' '.join(str(e) for e in coord[i]) + ' ' + ' '.join(str(e) for e in vec[i]) + '\n')
            else:
                input_findsym.append(' '.join(str(e) for e in coord[i]) + ' ' + ' '.join(str(e) for e in vec[i]))
    elif magnetic == False:
        input_findsym.append('\n')
        for i in range(len(at)):
            if i < len(at) - 1:
                input_findsym.append(' '.join(str(e) for e in coord[i]) + '\n')
            else:
                input_findsym.append(' '.join(str(e) for e in coord[i]))
    if filename is not None:
        with open(filename, 'w') as f:
            for i in input_findsym:
                f.write(i)
    return input_findsym
