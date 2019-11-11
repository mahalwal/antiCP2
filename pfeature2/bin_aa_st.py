import pandas as pd
import sys
import os
import numpy as np
import getopt
from itertools import repeat
def split(file,n):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    k1 = []
    for w in range(0,len(df2)):
        s = 0
        k2 = []
        r = 0
        if len(df2[0][w])%n == 0:
            k2.extend(repeat(int(len(df2[0][w])/n),n))
        else:
            r = int(len(df2[0][w])%n)
            k2.extend(repeat(int(len(df2[0][w])/n),n-1))
            k2.append((int(len(df2[0][w])/n))+r)
        for j in k2:
            df3 = df2[0][w][s:j+s]
            k1.append(df3)
            s = j+s
    df4 = pd.DataFrame(k1)
    #df4.to_csv(filename+".split", index = None, header = False, encoding = 'utf-8')
    return df4
		
def bin_aa_st(file,output,n):
    file1 = split(file,n)
    filename, file_extension = os.path.splitext(file)
    df=file1
    zz = df.iloc[:,0]
    f = open(filename+'.bin_split', 'w')
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
    ff1 = open(output,'w')
    sys.stdout=ff1
    with open(filename+".bin_split","r") as f:
        fob = f.readlines()
    for each in range(0,len(fob),n):
        print(','.join(fob[each:each+n]).replace(",\n,",",").replace("\n",""))
    ff1.truncate()

