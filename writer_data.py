#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import datetime
import sys

# my imports
from atom import Atom
from bond import Bond
from angle import Angle
from dihedral import Dihedral
from improper import Improper


"""
    - Types of bonds, angles, etc. are hardcoded!
"""


class WriterData(dict):
    def __init__(self, atomicSystem, atomicStyle='full', fname=None):
        self['atomicSystem'] = atomicSystem
        self['fname'] = fname
        self['atomicStyle'] = atomicStyle
        self.__addParserFullAttributes()

    def writeData(self):
        if self['atomicStyle'] == 'full':
            self.__writeDataFull()

    def __addParserFullAttributes(self):
        attrs = dict()
        attrs['atomTypesNumber'] = self['atomicSystem']['atomTypesNumber']
        attrs['bondTypesNumber'] = self['atomicSystem']['bondTypesNumber']
        attrs['angleTypesNumber'] = self['atomicSystem']['angleTypesNumber']
        attrs['dihedralTypesNumber'] = self['atomicSystem']['dihedralTypesNumber']
        attrs['improperTypesNumber'] = self['atomicSystem']['improperTypesNumber']
        attrs['pairCoeffs'] = self['atomicSystem']['pairCoeffs']
        attrs['bondCoeffs'] = self['atomicSystem']['bondCoeffs']
        attrs['angleCoeffs'] = self['atomicSystem']['angleCoeffs']
        attrs['dihedralCoeffs'] = self['atomicSystem']['dihedralCoeffs']
        attrs['improperCoeffs'] = self['atomicSystem']['improperCoeffs']
        self.__parserAttributes = attrs


    def __writeDataFull(self):
        atSys = self['atomicSystem']
        if self['fname'] == None:
            f = sys.stdout
        else:
            f = open(self['fname'], 'w')
        now = datetime.datetime.now()
        comment = ('LAMMPS data file. ' +
                   'CompDrawer / ' +
                   str(now.day) + ' ' + str(now.month) + ' ' + str(now.year) + ' /'
                   ' UNDEFINED_STRING') # This is not important for me now,
                                        # but it should be done in a proper
                                        # way later!
      ### Start string
        f.write(comment)
        f.write('\n\n')
      ### Number of atoms, etc.
        # is it possible for LAMMPS datafile indent here to be not equal to 7?..
        f.write(' ')
        f.write(str(len(atSys['atoms'])))
        f.write(' atoms\n')
        f.write(' ')
        f.write(str(len(atSys['bonds'])))
        f.write(' bonds\n')
        f.write(' ')
        f.write(str(len(atSys['angles'])))
        f.write(' angles\n')
        f.write(' ')
        f.write(str(len(atSys['dihedrals'])))
        f.write(' dihedrals\n')
        f.write(' ')
        f.write(str(len(atSys['impropers'])))
        f.write(' impropers\n')
        f.write('\n')
      ### Number of atom types, etc.
        # is it possible for LAMMPS datafile indent here to be not equal to 4?..
        for key in ['atom', 'bond', 'angle', 'dihedral', 'improper']:
            keytn = key + 'TypesNumber'
            f.write(' ')
            f.write(str(self.__parserAttributes[keytn]))
            f.write(' ' + key + ' types\n')
        f.write('\n')
      ### Boundaries
        f.write('\t' + str(atSys['boundaries'][0]) +
                '\t' + str(atSys['boundaries'][1]))
        f.write(' xlo xhi\n')
        f.write('\t' + str(atSys['boundaries'][2]) +
                '\t' + str(atSys['boundaries'][3]))
        f.write(' ylo yhi\n')
        f.write('\t' + str(atSys['boundaries'][4]) +
                '\t' + str(atSys['boundaries'][5]))
        f.write(' zlo zhi\n')
        f.write('\n')
      ### Masses
        f.write('Masses\n\n')
        for i in range(len(atSys['masses'])):
            f.write(' ' + str(i + 1) + ' ' +
                    str(atSys['masses'][i]) + '\n')
        f.write('\n')
      ### Pair Coeffs # lj/cut/coul/long - maybe comment is optional?..
        array = ['Pair', 'Bond', 'Angle', 'Dihedral', 'Improper']
        for i, key in enumerate(array):
            keylc = key.lower() + 'Coeffs'
            if self.__parserAttributes[keylc] == 0:
                continue
            if i == 0:
                f.write(key + ' Coeffs # lj/cut/coul/long\n\n')
            elif i == len(array) - 1:
                f.write(key + ' Coeffs # cvff\n\n')
            else:
                f.write(key + ' Coeffs # harmonic\n\n')
            for coeffNumber, coeff in enumerate(self.__parserAttributes[keylc]):
                f.write(str(coeffNumber + 1) + ' ')
                for j in range(len(coeff)):
                    if coeff[j].is_integer():
                        coeff[j] = int(coeff[j])                    
                    f.write(str(coeff[j]))
                    if j != len(coeff) - 1:
                        f.write(' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys['atoms']) > 0:
            f.write('Atoms # full\n\n')
            for atom in atSys['atoms']:
                f.write(str(atom['lam_id']) + ' ')
                f.write(str(atom['molecule']) + ' ')
                f.write(str(atom['ff_type']) + ' ')
                f.write(str(atom['ff_charge']) + ' ')
                f.write(str(atom['x']) + ' ')
                f.write(str(atom['y']) + ' ')
                f.write(str(atom['z']) + ' ')
                f.write(str(atom['flags'][0]) + ' ')
                f.write(str(atom['flags'][1]) + ' ')
                f.write(str(atom['flags'][2]) + ' ')
                if 'comment' in atom.keys():
                    f.write(str(atom['comment']))
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys['bonds']) > 0:
            f.write('Bonds\n\n')
            for bond in atSys['bonds']:
                f.write(str(bond['lam_id']) + ' ')
                f.write(str(bond['ff_type']) + ' ')
                f.write(str(bond['atomOne']['lam_id']) + ' ')
                f.write(str(bond['atomTwo']['lam_id']) + ' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys['angles']) > 0:
            f.write('Angles\n\n')
            for angle in atSys['angles']:
                f.write(str(angle['lam_id']) + ' ')
                f.write(str(angle['ff_type']) + ' ')
                f.write(str(angle['atomOne']['lam_id']) + ' ')
                f.write(str(angle['atomTwo']['lam_id']) + ' ')
                f.write(str(angle['atomThree']['lam_id']) + ' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys['dihedrals']) > 0:
            f.write('Dihedrals\n\n')
            for dihedral in atSys['dihedrals']:
                f.write(str(dihedral['lam_id']) + ' ')
                f.write(str(dihedral['ff_type']) + ' ')
                f.write(str(dihedral['atomOne']['lam_id']) + ' ')
                f.write(str(dihedral['atomTwo']['lam_id']) + ' ')
                f.write(str(dihedral['atomThree']['lam_id']) + ' ')
                f.write(str(dihedral['atomFour']['lam_id']) + ' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys['impropers']) > 0:
            f.write('Impropers\n\n')
            for improper in atSys['impropers']:
                f.write(str(improper['lam_id']) + ' ')
                f.write(str(improper['ff_type']) + ' ')
                f.write(str(improper['atomOne']['lam_id']) + ' ')
                f.write(str(improper['atomTwo']['lam_id']) + ' ')
                f.write(str(improper['atomThree']['lam_id']) + ' ')
                f.write(str(improper['atomFour']['lam_id']) + ' ')
                f.write('\n')
