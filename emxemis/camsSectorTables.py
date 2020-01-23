#!/usr/bin/env python3
# The PM_split files have A,B,C,D,E,F1,F2,F3,F4,G,H,I,J,K,L,
# NB if we split A and F, set zero emissions for those sectors

cams3p1_table = """# Nov 2019
# emep  cams_code  cams_long
  1        A     A_PublicPower
  2        B     B_Industry
  3        C     C_OtherStationaryComb
  4        D     D_Fugitive
  5        E     E_Solvents
  6        F     F_RoadTransport
  7        G     G_Shipping
  8        H     H_Aviation
  9        I     I_Offroad
  10       J     J_Waste
  11       K     K_AgriLivestock
  12       L     L_AgriOther
  13       M     M_Other
  14      A1     A1_PublicPower_Point
  15      A2     A2_PublicPower_Area
  16      F1     F1_RoadTransportExhaustGasoline
  17      F2     F2_RoadTransportExhaustDiesel
  18      F3     F3_RoadTransportExhaustLPGgas
  19      F4     F4_RoadTransportNonExhaust
"""

def getCams2emep(table=cams3p1_table,dbg=False):
  cams2emepcode = dict()
  cams2name     = dict()
  for line in table.splitlines():
    if line.startswith('#'): continue
    a, b, c = line.split()
    cams2emepcode[ b ] = int(a)
    cams2name[ b ] = c
    #if dbg: print(a, cams2emep[b], c )
    if dbg: print( '\t'.join( [ b,  a, c ] ) )
  return cams2emepcode, cams2name

mapping, names =  getCams2emep(cams3p1_table,dbg=True)
if __name__ == '__main__':

  mapping, names =  getCams2emep(cams3p1_table,dbg=True)
  print('SHIPPING? ', mapping['G'], names['G'] )
