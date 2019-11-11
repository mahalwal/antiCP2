import pandas as pd
import sys
import os
import numpy as np
import getopt
def nt(file,n):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][0:n])
        df4 = pd.DataFrame(df3)
        #df4.to_csv(filename+".nt", index = None, header = False, encoding = 'utf-8')
    return df4
	
def bin_aa_nt(file,outt,n):
    file1 = nt(file,n)
    filename, file_extension = os.path.splitext(file)
    df=file1
    zz = df.iloc[:,0]
    f = open(outt, 'w')
    #print("B_N0,B_N0_1,B_N0_2,B_N0_3,B_N0_4,B_N0_5,B_N0_6,B_N0_7,B_N0_8,B_N0_9,B_N0_10,B_N0_11,B_N0_12,B_N0_13,B_N0_14,B_N0_15,B_N0_16,B_N0_17,B_N0_18,B_N0_19,B_N1,B_N1_1,B_N1_2,B_N1_3,B_N1_4,B_N1_5,B_N1_6,B_N1_7,B_N1_8,B_N1_9,B_N1_10,B_N1_11,B_N1_12,B_N1_13,B_N1_14,B_N1_15,B_N1_16,B_N1_17,B_N1_18,B_N1_19,B_N2,B_N2_1,B_N2_2,B_N2_3,B_N2_4,B_N2_5,B_N2_6,B_N2_7,B_N2_8,B_N2_9,B_N2_10,B_N2_11,B_N2_12,B_N2_13,B_N2_14,B_N2_15,B_N2_16,B_N2_17,B_N2_18,B_N2_19,B_N3,B_N3_1,B_N3_2,B_N3_3,B_N3_4,B_N3_5,B_N3_6,B_N3_7,B_N3_8,B_N3_9,B_N3_10,B_N3_11,B_N3_12,B_N3_13,B_N3_14,B_N3_15,B_N3_16,B_N3_17,B_N3_18,B_N3_19,B_N4,B_N4_1,B_N4_2,B_N4_3,B_N4_4,B_N4_5,B_N4_6,B_N4_7,B_N4_8,B_N4_9,B_N4_10,B_N4_11,B_N4_12,B_N4_13,B_N4_14,B_N4_15,B_N4_16,B_N4_17,B_N4_18,B_N4_19,B_N5,B_N5_1,B_N5_2,B_N5_3,B_N5_4,B_N5_5,B_N5_6,B_N5_7,B_N5_8,B_N5_9,B_N5_10,B_N5_11,B_N5_12,B_N5_13,B_N5_14,B_N5_15,B_N5_16,B_N5_17,B_N5_18,B_N5_19,B_N6,B_N6_1,B_N6_2,B_N6_3,B_N6_4,B_N6_5,B_N6_6,B_N6_7,B_N6_8,B_N6_9,B_N6_10,B_N6_11,B_N6_12,B_N6_13,B_N6_14,B_N6_15,B_N6_16,B_N6_17,B_N6_18,B_N6_19,B_N7,B_N7_1,B_N7_2,B_N7_3,B_N7_4,B_N7_5,B_N7_6,B_N7_7,B_N7_8,B_N7_9,B_N7_10,B_N7_11,B_N7_12,B_N7_13,B_N7_14,B_N7_15,B_N7_16,B_N7_17,B_N7_18,B_N7_19,B_N8,B_N8_1,B_N8_2,B_N8_3,B_N8_4,B_N8_5,B_N8_6,B_N8_7,B_N8_8,B_N8_9,B_N8_10,B_N8_11,B_N8_12,B_N8_13,B_N8_14,B_N8_15,B_N8_16,B_N8_17,B_N8_18,B_N8_19,B_N9,B_N9_1,B_N9_2,B_N9_3,B_N9_4,B_N9_5,B_N9_6,B_N9_7,B_N9_8,B_N9_9,B_N9_10,B_N9_11,B_N9_12,B_N9_13,B_N9_14,B_N9_15,B_N9_16,B_N9_17,B_N9_18,B_N9_19,")		
    sys.stdout = f
    A=('1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    C=('0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    D=('0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    E=('0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    F=('0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    G=('0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    H=('0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0')
    I=('0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0')
    K=('0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0')
    L=('0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0')
    M=('0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0')
    N=('0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0')
    P=('0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0')
    Q=('0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0')
    R=('0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0')
    S=('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0')
    T=('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0')
    V=('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0')
    W=('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0')
    Y=('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1')
    for i in range(0,len(zz)):
        for j in zz[i]:
            if j == "A":
                print(''.join(A), end = ',')
            if j == "C":
                print(''.join(C), end = ',')
            if j == "D":
                print(''.join(D), end = ',')
            if j == "E":
                print(''.join(E), end = ',')
            if j == "F":
                print(''.join(F), end = ',')
            if j == "G":
                print(''.join(G), end = ',')
            if j == "H":
                print(''.join(H), end = ',')
            if j == "I":
                print(''.join(I), end = ',')
            if j == "K":
                print(''.join(K), end = ',')
            if j == "L":
                print(''.join(L), end = ',')
            if j == "M":
                print(''.join(M), end = ',')
            if j == "N":
                print(''.join(N), end = ',')
            if j == "P":
                print(''.join(P), end = ',')
            if j == "Q":
                print(''.join(Q), end = ',')
            if j == "R":
                print(''.join(R), end = ',')
            if j == "S":
                print(''.join(S), end = ',')
            if j == "T":
                print(''.join(T), end = ',')
            if j == "V":
                print(''.join(V), end = ',')
            if j == "W":
                print(''.join(W), end = ',')
            if j == "Y":
                print(''.join(Y), end = ',')
        print("")
    f.truncate()
