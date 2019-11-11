import os
import pandas as pd
import sys
import getopt
std = list("ACDEFGHIKLMNPQRSTVWY")
def ddor_wp(file,out) :
    filename, file_extension = os.path.splitext(file)
    df = pd.read_csv(file, header = None)
    df1 = pd.DataFrame(df[0].str.upper())
    f = open(out,'w')
    sys.stdout = f
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    for i in range(0,len(df1)):
        s = df1[0][i]
        p = s[::-1]
        for j in std:
            zz = ([pos for pos, char in enumerate(s) if char == j])
            pp = ([pos for pos, char in enumerate(p) if char == j])
            ss = []
            for i in range(0,(len(zz)-1)):
                ss.append(zz[i+1] - zz[i]-1)
            if zz == []:
                ss = []
            else:
                ss.insert(0,zz[0])
                ss.insert(len(ss),pp[0])
            cc1=  (sum([e for e in ss])+1)
            cc = sum([e*e for e in ss])
            zz2 = cc/cc1
            print("%.2f"%zz2,end=",")
        print("")
    f.truncate()
