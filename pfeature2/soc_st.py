import os
import sys
import getopt
import numpy as np
import pandas as pd
from itertools import repeat
def split(file,v):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    k1 = []
    for e in range(0,len(df2)):
        s = 0
        k2 = []
        r = 0
        if len(df2[0][e])%v == 0:
            k2.extend(repeat(int(len(df2[0][e])/v),v))
        else:
            r = int(len(df2[0][e])%v)
            k2.extend(repeat(int(len(df2[0][e])/v),v-1))
            k2.append((int(len(df2[0][e])/v))+r)
        for j in k2:
            df3 = df2[0][e][s:j+s]
            k1.append(df3)
            s = j+s
    df4 = pd.DataFrame(k1)
    #df4.to_csv(filename+".split", index = None, header = False, encoding = 'utf-8')
    return df4

def soc_st(file,output,gap,v):
    file1 = split(file,v)
    ff = []
    filename, file_extension = os.path.splitext(file)
    #df = pd.read_csv(file, header = None)
    df2 = file1
    for i in range(0,len(df2)):
        ff.append(len(df2[0][i]))
    if min(ff) < gap:
        print("Error: All sequences' length should be higher than :", gap)
        return 0
    mat1 = pd.read_csv("Schneider-Wrede.csv", index_col = 'Name')
    mat2 = pd.read_csv("Grantham.csv", index_col = 'Name')
    h1 = []
    h2 = []
    for n in range(1, gap+1):
        h1.append('Schneider_gap' + str(n))
    for n in range(1, gap + 1):
        h2.append('Grantham_gap' + str(n))
    s1 = []
    s2 = []
    for i in range(0,len(df2)):
        for n in range(1, gap+1):
            sum = 0
            sum1 =0
            sum2 =0
            sum3 =0
            for j in range(0,(len(df2[0][i])-n)):
                sum = sum + (mat1[df2[0][i][j]][df2[0][i][j+n]])**2
                sum1 = sum/(len(df2[0][i])-n)
                sum2 = sum2 + (mat2[df2[0][i][j]][df2[0][i][j+n]])**2
                sum3 = sum2/(len(df2[0][i])-n)
            s1.append(sum1)
            s2.append(sum3)
    zz = np.array(s1).reshape(len(df2),gap)
    zz2 = np.array(s2).reshape(len(df2),gap)
    zz3 = round(pd.concat([pd.DataFrame(zz, columns = h1),pd.DataFrame(zz2,columns = h2)], axis = 1),4)
    header = []
    for i in range(1,v+1):
        for j in range(1,gap+1):
            header.append("Schneider_gap"+str(j)+"_s"+str(i))
        for j in range(1,gap+1):
            header.append("Grantham_gap"+str(j)+"_s"+str(i))
    bb = []
    for i in range(0,len(zz3),v):
        aa = []
        for j in range(v):
            aa.extend(zz3.loc[i+j])
        bb.append(aa)
    zz = pd.DataFrame(bb)
    zz.columns = header
    zz.to_csv(output, index = None, encoding = 'utf-8') 
