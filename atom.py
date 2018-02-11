class Atom(dict):
    def __init__(self,
                 lam_id,
                 x, y, z,
                 molecule=None,
                 ff_type=None,
                 ff_charge=None,
                 v=None,
                 flags=None,
                 comment=None
                 ):
        self['lam_id'] = lam_id
        self['x'] = x
        self['y'] = y
        self['z'] = z
        if molecule is not None:
            self['molecule'] = molecule
        if ff_type is not None:
            self['ff_type'] = ff_type
        if ff_charge is not None:
            self['ff_charge'] = ff_charge
        if v is not None:
            self['vx'] = v[0]
            self['vy'] = v[1]
            self['vz'] = v[2]
        if flags is not None:
            self['flags'] = flags
        if comment is not None:
            self['comment'] = comment
