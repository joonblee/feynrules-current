# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Tue 12 Dec 2023 11:56:50


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_160_38,(0,0,1):C.R2GC_160_39})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV12, L.VVVV13, L.VVVV15, L.VVVV20 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_118_14,(0,0,1):C.R2GC_118_15,(2,0,0):C.R2GC_118_14,(2,0,1):C.R2GC_118_15,(6,0,0):C.R2GC_121_19,(6,0,1):C.R2GC_165_45,(7,0,0):C.R2GC_122_21,(7,0,1):C.R2GC_164_44,(5,0,0):C.R2GC_116_10,(5,0,1):C.R2GC_116_11,(1,0,0):C.R2GC_116_10,(1,0,1):C.R2GC_116_11,(4,0,0):C.R2GC_116_10,(4,0,1):C.R2GC_116_11,(3,0,0):C.R2GC_116_10,(3,0,1):C.R2GC_116_11,(8,0,0):C.R2GC_117_12,(8,0,1):C.R2GC_117_13,(11,3,0):C.R2GC_120_17,(11,3,1):C.R2GC_120_18,(10,3,0):C.R2GC_120_17,(10,3,1):C.R2GC_120_18,(9,3,1):C.R2GC_119_16,(0,1,0):C.R2GC_118_14,(0,1,1):C.R2GC_118_15,(2,1,0):C.R2GC_118_14,(2,1,1):C.R2GC_118_15,(6,1,0):C.R2GC_161_40,(6,1,1):C.R2GC_161_41,(7,1,0):C.R2GC_122_21,(7,1,1):C.R2GC_122_22,(5,1,0):C.R2GC_116_10,(5,1,1):C.R2GC_116_11,(1,1,0):C.R2GC_116_10,(1,1,1):C.R2GC_116_11,(4,1,0):C.R2GC_116_10,(4,1,1):C.R2GC_116_11,(3,1,0):C.R2GC_116_10,(3,1,1):C.R2GC_116_11,(8,1,0):C.R2GC_117_12,(8,1,1):C.R2GC_166_46,(0,2,0):C.R2GC_118_14,(0,2,1):C.R2GC_118_15,(2,2,0):C.R2GC_118_14,(2,2,1):C.R2GC_118_15,(6,2,0):C.R2GC_121_19,(6,2,1):C.R2GC_121_20,(7,2,0):C.R2GC_162_42,(7,2,1):C.R2GC_118_15,(5,2,0):C.R2GC_116_10,(5,2,1):C.R2GC_116_11,(1,2,0):C.R2GC_116_10,(1,2,1):C.R2GC_116_11,(4,2,0):C.R2GC_116_10,(4,2,1):C.R2GC_116_11,(3,2,0):C.R2GC_116_10,(3,2,1):C.R2GC_116_11,(8,2,0):C.R2GC_117_12,(8,2,1):C.R2GC_163_43})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS8 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_157_36})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS7, L.FFS8 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_175_49,(0,1,0):C.R2GC_178_52})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_147_31})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS6 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_146_30})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.s__tilde__, P.c, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS7 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_158_37})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS7, L.FFS8 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_179_53,(0,1,0):C.R2GC_174_48})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_155_34})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_176_50})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_35})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_177_51})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_125_25})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_125_25})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_125_25})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_23})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_123_23})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_23})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_124_24})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_24})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_124_24})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_24})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_124_24})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_24})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_139_27})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_139_27})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_139_27})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_139_27})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_139_27})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_139_27})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_106_9,(0,1,0):C.R2GC_154_33})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_106_9,(0,1,0):C.R2GC_154_33})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_106_9,(0,1,0):C.R2GC_154_33})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,1,0):C.R2GC_145_29})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,1,0):C.R2GC_145_29})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,1,0):C.R2GC_145_29})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF9 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_127_26})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF10, L.FF11, L.FF12, L.FF14 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_151_32,(0,2,0):C.R2GC_151_32,(0,1,0):C.R2GC_127_26,(0,3,0):C.R2GC_127_26})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF10, L.FF11, L.FF12, L.FF14 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_47,(0,2,0):C.R2GC_170_47,(0,1,0):C.R2GC_127_26,(0,3,0):C.R2GC_127_26})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF9 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_127_26})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF9 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_127_26})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF13, L.FF15 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_143_28,(0,1,0):C.R2GC_127_26})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV7, L.VV8, L.VV9 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,3):C.R2GC_86_54,(0,0,0):C.R2GC_92_55,(0,0,2):C.R2GC_92_56,(0,0,4):C.R2GC_92_57,(0,1,1):C.R2GC_95_63})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_94_60,(0,0,1):C.R2GC_94_61,(0,0,2):C.R2GC_94_62})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV20 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_105_8})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV20 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_98_68,(0,0,1):C.R2GC_98_69})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV20 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_101_3,(0,0,1):C.R2GC_101_4})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV20 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_96_64,(0,0,1):C.R2GC_96_65})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV11, L.VVVV20 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_100_1,(1,0,1):C.R2GC_100_2,(0,1,0):C.R2GC_99_70,(0,1,1):C.R2GC_99_71})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV20 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_97_66,(0,0,1):C.R2GC_97_67})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_93_58,(0,0,1):C.R2GC_104_7,(0,0,2):C.R2GC_93_59})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_93_58,(0,0,1):C.R2GC_104_7,(0,0,2):C.R2GC_93_59})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_104_6,(0,0,1):C.R2GC_104_7})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV4, L.VVV5, L.VVV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_160_58,(0,1,1):C.UVGC_160_59,(0,1,2):C.UVGC_160_60,(0,1,5):C.UVGC_160_61,(0,2,3):C.UVGC_107_1,(0,0,4):C.UVGC_108_2})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV12, L.VVVV13, L.VVVV15, L.VVVV20 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_117_11,(0,0,5):C.UVGC_117_10,(2,0,4):C.UVGC_117_11,(2,0,5):C.UVGC_117_10,(6,0,0):C.UVGC_164_75,(6,0,2):C.UVGC_164_76,(6,0,3):C.UVGC_164_77,(6,0,4):C.UVGC_165_81,(6,0,5):C.UVGC_165_82,(6,0,6):C.UVGC_164_80,(7,0,0):C.UVGC_164_75,(7,0,2):C.UVGC_164_76,(7,0,3):C.UVGC_164_77,(7,0,4):C.UVGC_164_78,(7,0,5):C.UVGC_164_79,(7,0,6):C.UVGC_164_80,(5,0,4):C.UVGC_116_8,(5,0,5):C.UVGC_116_9,(1,0,4):C.UVGC_116_8,(1,0,5):C.UVGC_116_9,(4,0,4):C.UVGC_116_8,(4,0,5):C.UVGC_116_9,(3,0,4):C.UVGC_116_8,(3,0,5):C.UVGC_116_9,(8,0,4):C.UVGC_117_10,(8,0,5):C.UVGC_117_11,(11,3,4):C.UVGC_120_14,(11,3,5):C.UVGC_120_15,(10,3,4):C.UVGC_120_14,(10,3,5):C.UVGC_120_15,(9,3,4):C.UVGC_119_12,(9,3,5):C.UVGC_119_13,(0,1,4):C.UVGC_117_11,(0,1,5):C.UVGC_117_10,(2,1,4):C.UVGC_117_11,(2,1,5):C.UVGC_117_10,(6,1,0):C.UVGC_161_62,(6,1,2):C.UVGC_161_63,(6,1,4):C.UVGC_161_64,(6,1,5):C.UVGC_161_65,(6,1,6):C.UVGC_161_66,(7,1,1):C.UVGC_121_16,(7,1,4):C.UVGC_122_18,(7,1,5):C.UVGC_122_19,(5,1,4):C.UVGC_116_8,(5,1,5):C.UVGC_116_9,(1,1,4):C.UVGC_116_8,(1,1,5):C.UVGC_116_9,(4,1,4):C.UVGC_116_8,(4,1,5):C.UVGC_116_9,(3,1,4):C.UVGC_116_8,(3,1,5):C.UVGC_116_9,(8,1,0):C.UVGC_166_83,(8,1,2):C.UVGC_166_84,(8,1,3):C.UVGC_166_85,(8,1,4):C.UVGC_166_86,(8,1,5):C.UVGC_166_87,(8,1,6):C.UVGC_166_88,(0,2,4):C.UVGC_117_11,(0,2,5):C.UVGC_117_10,(2,2,4):C.UVGC_117_11,(2,2,5):C.UVGC_117_10,(6,2,1):C.UVGC_121_16,(6,2,4):C.UVGC_121_17,(6,2,5):C.UVGC_119_12,(7,2,0):C.UVGC_161_62,(7,2,2):C.UVGC_161_63,(7,2,4):C.UVGC_162_67,(7,2,5):C.UVGC_162_68,(7,2,6):C.UVGC_161_66,(5,2,4):C.UVGC_116_8,(5,2,5):C.UVGC_116_9,(1,2,4):C.UVGC_116_8,(1,2,5):C.UVGC_116_9,(4,2,4):C.UVGC_116_8,(4,2,5):C.UVGC_116_9,(3,2,4):C.UVGC_116_8,(3,2,5):C.UVGC_116_9,(8,2,0):C.UVGC_163_69,(8,2,2):C.UVGC_163_70,(8,2,3):C.UVGC_163_71,(8,2,4):C.UVGC_163_72,(8,2,5):C.UVGC_163_73,(8,2,6):C.UVGC_163_74})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS8 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_157_49,(0,0,2):C.UVGC_157_50,(0,0,1):C.UVGC_157_51})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS7, L.FFS8 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_175_100,(0,0,2):C.UVGC_175_101,(0,0,1):C.UVGC_175_102,(0,1,0):C.UVGC_178_105,(0,1,2):C.UVGC_178_106,(0,1,1):C.UVGC_178_107})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_147_39})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_146_38})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS7 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_158_52,(0,0,2):C.UVGC_158_53,(0,0,1):C.UVGC_158_54})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS7, L.FFS8 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_179_108,(0,0,2):C.UVGC_179_109,(0,0,1):C.UVGC_179_110,(0,1,0):C.UVGC_174_97,(0,1,2):C.UVGC_174_98,(0,1,1):C.UVGC_174_99})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_155_47})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_176_103})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_156_48})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_177_104})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV9 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_114_5})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV10, L.FFV6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,1,0):C.UVGC_114_5,(0,0,0):C.UVGC_149_41})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_114_5,(0,1,0):C.UVGC_168_90,(0,2,0):C.UVGC_168_90})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_110_4,(0,2,0):C.UVGC_110_4})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_110_4,(0,2,0):C.UVGC_110_4})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_141_33,(0,2,0):C.UVGC_141_33})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,5):C.UVGC_124_21,(0,1,0):C.UVGC_129_23,(0,1,1):C.UVGC_129_24,(0,1,2):C.UVGC_129_25,(0,1,3):C.UVGC_129_26,(0,1,4):C.UVGC_129_27,(0,1,6):C.UVGC_129_28,(0,1,5):C.UVGC_129_29,(0,2,0):C.UVGC_129_23,(0,2,1):C.UVGC_129_24,(0,2,2):C.UVGC_129_25,(0,2,3):C.UVGC_129_26,(0,2,4):C.UVGC_129_27,(0,2,6):C.UVGC_129_28,(0,2,5):C.UVGC_129_29})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_124_21,(0,1,0):C.UVGC_129_23,(0,1,1):C.UVGC_129_24,(0,1,3):C.UVGC_129_25,(0,1,4):C.UVGC_129_26,(0,1,5):C.UVGC_129_27,(0,1,6):C.UVGC_129_28,(0,1,2):C.UVGC_150_42,(0,2,0):C.UVGC_129_23,(0,2,1):C.UVGC_129_24,(0,2,3):C.UVGC_129_25,(0,2,4):C.UVGC_129_26,(0,2,5):C.UVGC_129_27,(0,2,6):C.UVGC_129_28,(0,2,2):C.UVGC_150_42})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,5):C.UVGC_124_21,(0,1,0):C.UVGC_129_23,(0,1,1):C.UVGC_129_24,(0,1,2):C.UVGC_129_25,(0,1,3):C.UVGC_129_26,(0,1,4):C.UVGC_129_27,(0,1,6):C.UVGC_129_28,(0,1,5):C.UVGC_169_91,(0,2,0):C.UVGC_129_23,(0,2,1):C.UVGC_129_24,(0,2,2):C.UVGC_129_25,(0,2,3):C.UVGC_129_26,(0,2,4):C.UVGC_129_27,(0,2,6):C.UVGC_129_28,(0,2,5):C.UVGC_169_91})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d, P.g] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_124_21,(0,1,0):C.UVGC_129_23,(0,1,1):C.UVGC_129_24,(0,1,3):C.UVGC_129_25,(0,1,4):C.UVGC_129_26,(0,1,5):C.UVGC_129_27,(0,1,6):C.UVGC_129_28,(0,1,2):C.UVGC_129_29,(0,2,0):C.UVGC_129_23,(0,2,1):C.UVGC_129_24,(0,2,3):C.UVGC_129_25,(0,2,4):C.UVGC_129_26,(0,2,5):C.UVGC_129_27,(0,2,6):C.UVGC_129_28,(0,2,2):C.UVGC_129_29})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,5):C.UVGC_124_21,(0,1,0):C.UVGC_129_23,(0,1,1):C.UVGC_129_24,(0,1,2):C.UVGC_129_25,(0,1,3):C.UVGC_129_26,(0,1,4):C.UVGC_129_27,(0,1,6):C.UVGC_129_28,(0,1,5):C.UVGC_129_29,(0,2,0):C.UVGC_129_23,(0,2,1):C.UVGC_129_24,(0,2,2):C.UVGC_129_25,(0,2,3):C.UVGC_129_26,(0,2,4):C.UVGC_129_27,(0,2,6):C.UVGC_129_28,(0,2,5):C.UVGC_129_29})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV6, L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_124_21,(0,1,0):C.UVGC_129_23,(0,1,2):C.UVGC_129_24,(0,1,3):C.UVGC_129_25,(0,1,4):C.UVGC_129_26,(0,1,5):C.UVGC_129_27,(0,1,6):C.UVGC_129_28,(0,1,1):C.UVGC_142_34,(0,2,0):C.UVGC_129_23,(0,2,2):C.UVGC_129_24,(0,2,3):C.UVGC_129_25,(0,2,4):C.UVGC_129_26,(0,2,5):C.UVGC_129_27,(0,2,6):C.UVGC_129_28,(0,2,1):C.UVGC_142_34})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_139_30,(0,0,1):C.UVGC_139_31})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_152_44,(0,0,2):C.UVGC_139_30,(0,0,1):C.UVGC_139_31})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_171_93,(0,0,2):C.UVGC_171_94,(0,0,1):C.UVGC_139_31})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_139_30,(0,0,1):C.UVGC_139_31})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_152_44,(0,0,2):C.UVGC_139_30,(0,0,1):C.UVGC_139_31})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_171_93,(0,0,2):C.UVGC_171_94,(0,0,1):C.UVGC_139_31})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_153_45,(0,1,0):C.UVGC_154_46})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_172_95,(0,1,0):C.UVGC_173_96})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_144_36,(0,1,0):C.UVGC_145_37})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF11, L.FF14, L.FF9 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,2,0):C.UVGC_127_22,(0,0,0):C.UVGC_109_3,(0,1,0):C.UVGC_109_3})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF10, L.FF11, L.FF12, L.FF14 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_151_43,(0,2,0):C.UVGC_151_43,(0,1,0):C.UVGC_148_40,(0,3,0):C.UVGC_148_40})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF10, L.FF11, L.FF12, L.FF14 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_170_92,(0,2,0):C.UVGC_170_92,(0,1,0):C.UVGC_167_89,(0,3,0):C.UVGC_167_89})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF11, L.FF14, L.FF9 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,2,0):C.UVGC_127_22,(0,0,0):C.UVGC_109_3,(0,1,0):C.UVGC_109_3})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF16 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_109_3})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF13, L.FF15 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_143_35,(0,1,0):C.UVGC_140_32})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV10, L.VV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_159_55,(0,0,1):C.UVGC_159_56,(0,0,4):C.UVGC_159_57,(0,1,2):C.UVGC_115_6,(0,1,3):C.UVGC_115_7})

