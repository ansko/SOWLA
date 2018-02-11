class AtomicSystem(dict):
    def __init__(self,
                 atoms, bonds, angles, dihedrals, impropers,
                 masses,
                 atomTypesNumber=None, bondTypesNumber=None,
                     angleTypesNumber=None, dihedralTypesNumber=None,
                     improperTypesNumber=None,
                 pairCoeffs=None, bondCoeffs=None, angleCoeffs=None,
                     dihedralCoeffs=None, improperCoeffs=None,
                 boundaries=None
                 ):
        self['atoms'] = atoms
        if atomTypesNumber is not None:
            self['atomTypesNumber'] = atomTypesNumber
        if pairCoeffs is not None:
            self['pairCoeffs'] = pairCoeffs
        ##
        self['bonds'] = bonds
        if bondTypesNumber is not None:
            self['bondTypesNumber'] = bondTypesNumber
        if bondCoeffs is not None:
            self['bondCoeffs'] = bondCoeffs
        ##
        self['angles'] = angles
        if angleTypesNumber is not None:
            self['angleTypesNumber'] = angleTypesNumber
        if angleCoeffs is not None:
            self['angleCoeffs'] = angleCoeffs
        ##
        self['dihedrals'] = dihedrals
        if dihedralTypesNumber is not None:
            self['dihedralTypesNumber'] = dihedralTypesNumber
        if dihedralCoeffs is not None:
            self['dihedralCoeffs'] = dihedralCoeffs
        ##
        self['impropers'] = impropers
        if improperTypesNumber is not None:
            self['improperTypesNumber'] = improperTypesNumber
        if improperCoeffs is not None:
            self['improperCoeffs'] = improperCoeffs
        ##
        if boundaries is not None:
            self['boundaries'] = boundaries
        self['masses'] = masses
