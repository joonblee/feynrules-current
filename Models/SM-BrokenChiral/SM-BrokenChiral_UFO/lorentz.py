# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Tue 12 Dec 2023 11:56:50


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


FF9 = Lorentz(name = 'FF9',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,1)')

FF10 = Lorentz(name = 'FF10',
               spins = [ 2, 2 ],
               structure = 'ProjM(2,1)')

FF11 = Lorentz(name = 'FF11',
               spins = [ 2, 2 ],
               structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1)')

FF12 = Lorentz(name = 'FF12',
               spins = [ 2, 2 ],
               structure = 'ProjP(2,1)')

FF13 = Lorentz(name = 'FF13',
               spins = [ 2, 2 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FF14 = Lorentz(name = 'FF14',
               spins = [ 2, 2 ],
               structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

FF15 = Lorentz(name = 'FF15',
               spins = [ 2, 2 ],
               structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

FF16 = Lorentz(name = 'FF16',
               spins = [ 2, 2 ],
               structure = '-(P(-1,1)*Gamma(-1,2,1)) + P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

VV6 = Lorentz(name = 'VV6',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2)')

VV7 = Lorentz(name = 'VV7',
              spins = [ 3, 3 ],
              structure = 'Metric(1,2)')

VV8 = Lorentz(name = 'VV8',
              spins = [ 3, 3 ],
              structure = 'P(-1,2)**2*Metric(1,2)')

VV9 = Lorentz(name = 'VV9',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2) - (3*P(-1,2)**2*Metric(1,2))/2.')

VV10 = Lorentz(name = 'VV10',
               spins = [ 3, 3 ],
               structure = 'P(1,2)*P(2,2) - P(-1,2)**2*Metric(1,2)')

UUS2 = Lorentz(name = 'UUS2',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV2 = Lorentz(name = 'UUV2',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS2 = Lorentz(name = 'SSS2',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS5 = Lorentz(name = 'FFS5',
               spins = [ 2, 2, 1 ],
               structure = 'Gamma5(2,1)')

FFS6 = Lorentz(name = 'FFS6',
               spins = [ 2, 2, 1 ],
               structure = 'Identity(2,1)')

FFS7 = Lorentz(name = 'FFS7',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS8 = Lorentz(name = 'FFS8',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV9 = Lorentz(name = 'FFV9',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1) - Gamma(3,2,-1)*ProjM(-1,1) - Gamma(3,2,-1)*ProjP(-1,1)')

FFV10 = Lorentz(name = 'FFV10',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)')

VSS2 = Lorentz(name = 'VSS2',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV4 = Lorentz(name = 'VVV4',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - 3*P(3,2)*Metric(1,2) - P(3,3)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,2)*Metric(1,3) + 3*P(2,3)*Metric(1,3) + 2*P(1,2)*Metric(2,3) - 2*P(1,3)*Metric(2,3)')

VVV5 = Lorentz(name = 'VVV5',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVV6 = Lorentz(name = 'VVV6',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - (11*P(3,2)*Metric(1,2))/17. + (3*P(3,3)*Metric(1,2))/17. - P(2,1)*Metric(1,3) - (3*P(2,2)*Metric(1,3))/17. + (11*P(2,3)*Metric(1,3))/17. + (14*P(1,2)*Metric(2,3))/17. - (14*P(1,3)*Metric(2,3))/17.')

SSSS2 = Lorentz(name = 'SSSS2',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Epsilon(1,2,3,4)')

VVVV12 = Lorentz(name = 'VVVV12',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3)')

VVVV13 = Lorentz(name = 'VVVV13',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4)')

VVVV14 = Lorentz(name = 'VVVV14',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV15 = Lorentz(name = 'VVVV15',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,2)*Metric(3,4)')

VVVV16 = Lorentz(name = 'VVVV16',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV17 = Lorentz(name = 'VVVV17',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV18 = Lorentz(name = 'VVVV18',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV19 = Lorentz(name = 'VVVV19',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV20 = Lorentz(name = 'VVVV20',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

