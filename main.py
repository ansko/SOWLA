#!/usr/bin/env python3


from reader_data import ReaderData
from writer_data import WriterData

from atomic_system import AtomicSystem

def main():
    print('starting the program')

#    infname = '/home/anton/DataExamples/MT2EtOH.data'
    infname = '/home/anton/DataExamples/10x20.data'
    outfname = 'out.data'
    reader = ReaderData(infname, 'full')
    atsys = AtomicSystem(reader['parsedAtoms'],
                         reader['parsedBonds'],
                         reader['parsedAngles'],
                         reader['parsedDihedrals'],
                         reader['parsedImpropers'],
                         reader['parsedMasses'],
                         boundaries=reader['parsedBoundaries'],
                         atomTypesNumber=reader['parsedAtomTypesNumber'],
                         bondTypesNumber=reader['parsedBondTypesNumber'],
                         angleTypesNumber=reader['parsedAngleTypesNumber'],
                         dihedralTypesNumber=reader['parsedDihedralTypesNumber'],
                         improperTypesNumber=reader['parsedImproperTypesNumber'],
                         pairCoeffs=reader['parsedPairCoeffs'],
                         bondCoeffs=reader['parsedBondCoeffs'],
                         angleCoeffs=reader['parsedAngleCoeffs'],
                         dihedralCoeffs=reader['parsedDihedralCoeffs'],
                         improperCoeffs=reader['parsedImproperCoeffs']
                         )
    writer = WriterData(atomicSystem=atsys, fname=outfname)
    writer.writeData()

    print('thanks for using! bye!')


main()
