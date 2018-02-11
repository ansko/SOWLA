class Angle(dict):
    def __init__(self,
                 lam_id,
                 atomOne, atomTwo, atomThree,
                 ff_type=None
                 ):
        self['lam_id'] = lam_id
        if ff_type is not None:
            self['ff_type'] = ff_type
        self['atomOne'] = atomOne
        self['atomTwo'] = atomTwo
        self['atomThree'] = atomThree
