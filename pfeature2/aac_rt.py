import pandas as pd
import sys
import os
import numpy as np
import getopt
std = list("ACDEFGHIKLMNPQRSTVWY")
def aac_rt(file,out,m,n):
    filename, file_extension = os.path.splitext(file)
    f = open(out, 'w')
    sys.stdout = f
    df = pd.read_csv(file, header = None)
    zz = df.iloc[:,0]
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    for j in range(0,len(zz)):
        str = zz[j][m:-n]
        q = str.upper()
        if len(q)>=1:
            for i in std:
                count = 0
                for k in q:
                    temp1 = k
                    if temp1 == i:
                        count += 1
                    composition = (count/len(q))*100
                print("%.2f"%composition, end = ",")
            print("")
            f.truncate()
        else:
            print("Warning: Peptide length is small")
