import pandas as pd
import sys
import os
import numpy as np
import getopt
std = list("ACDEFGHIKLMNPQRSTVWY")
def aac_wp(file,out):
    filename, file_extension = os.path.splitext(file)
    f = open(out, 'w')
    sys.stdout = f
    df1 = pd.read_csv(file, header = None)
    df = pd.DataFrame(df1[0].str.upper())	
    zz = df.iloc[:,0]
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    for j in zz:
        for i in std:
            count = 0
            for k in j:
                temp1 = k
                if temp1 == i:
                    count += 1
                composition = (count/len(j))*100
            print("%.2f"%composition, end = ",")
        print("")
    f.truncate()
    f.close()
