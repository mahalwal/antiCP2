import sys
import pandas as pd
import os
import getopt
std = list('ACDEFGHIKLMNPQRSTVWY')
def rri_rt(file,out,n,c):
    filename, file_extension = os.path.splitext(file)
    df = pd.read_csv(file, header = None)
    df1 = pd.DataFrame(df[0].str.upper())
    count = 0
    cc = []
    i = 0
    x = 0
    temp = pd.DataFrame()
    f = open(out,'w')
    sys.stdout = f
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    for q in range(0,len(df1)):
        mm = df1[0][q][n:-c]
        while i < len(std):
            cc = []
            for j in mm:
                if j == std[i]:
                    count += 1
                    cc.append(count)
                else:
                    count = 0
            while x < len(cc) :
                if x+1 < len(cc) :
                    if cc[x]!=cc[x+1] :
                        if cc[x] < cc[x+1] :
                            cc[x]=0
                x += 1
            cc1 = [e for e in cc if e!= 0]
            cc = [e*e for e in cc if e != 0]
            zz= sum(cc)
            zz1 = sum(cc1)
            if zz1 != 0:
                zz2 = zz/zz1
            else:
                zz2 = 0
            print("%.2f"%zz2,end=',')
            i += 1
        i = 0
        print(" ")
    f.truncate()
