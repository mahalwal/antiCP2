import pandas as pd
import os
import math
import sys
import getopt
import numpy as np
data1 = pd.read_csv("data", sep = "\t")
from itertools import repeat

def split(file,v):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    k1 = []
    for w in range(0,len(df2)):
        s = 0
        k2 = []
        r = 0
        if len(df2[0][w])%v == 0:
            k2.extend(repeat(int(len(df2[0][w])/v),v))
        else:
            r = int(len(df2[0][w])%v)
            k2.extend(repeat(int(len(df2[0][w])/v),v-1))
            k2.append((int(len(df2[0][w])/v))+r)
        for j in k2:
            df3 = df2[0][w][s:j+s]
            k1.append(df3)
            s = j+s
    df4 = pd.DataFrame(k1)
    #df4.to_csv(filename+".split", index = None, header = False, encoding = 'utf-8')
    return df4	
std = list('ACDEFGHIKLMNPQRSTVWY')
def apaac_1_split(file,lambdaval,v):
    w=0.05
    df1 = split(file,v)
    filename, file_extension = os.path.splitext(file)
    #df = pd.read_csv(file, header = None)
    #df1 = pd.DataFrame(df[0].str.upper())
    dd = []
    cc = []
    pseudo = []
    aa = {}
    for i in range(len(std)):
        aa[std[i]] = i
    for i in range(0,3):
        mean = sum(data1.iloc[i][1:])/20
        rr = math.sqrt(sum([(p-mean)**2 for p in data1.iloc[i][1:]])/20)
        dd.append([(p-mean)/rr for p in data1.iloc[i][1:]])
        zz = pd.DataFrame(dd)
        #print(zz)
    head = []
    for n in range(1, lambdaval + 1):
        for e in ('hydrphobicity','hydrophilicity','sidechainmass'):
            head.append('lam_' + str(n)+"_"+str(e))
    pp = pd.DataFrame()
    ee = []
    tt = []
    for k in range(0,len(df1)):
        cc = []
        for n in range(1,lambdaval+1):
            for b in range(0,len(zz)):
                cc.append(sum([zz.loc[b][aa[df1[0][k][p]]] * zz.loc[b][aa[df1[0][k][p + n]]] for p in range(len(df1[0][k]) - n)]) / (len(df1[0][k]) - n))
                qq = pd.DataFrame(cc)
        tt.append(cc)
        np.savetxt(filename+".more", tt, delimiter=",")
        pseudo = [(w * p) / (1 + w * sum(cc)) for p in cc]
        ee.append(pseudo)
        ii = round(pd.DataFrame(ee, columns = head),4)
        ii.to_csv(filename+".plam",index = None)
def aac_comp(file,v):
    w = 0.05
    df = split(file,v)
    filename, file_extension = os.path.splitext(file)
    df31 = pd.read_csv(filename+".more", header=None)
    df31["sum"] = df31.sum(axis=1)
    f = open(filename+".aac", 'w')
    sys.stdout = f
    zz = df.iloc[:,0]
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    c = 0
    for j in zz:
        for i in std:
            count = 0
            for k in j:
                temp1 = k
                if temp1 == i:
                    count += 1
                composition = (count/(1+(w*df31['sum'][c])))
            print("%.4f"%composition, end = ",")
        print("")
        c = c+1
    f.truncate()
def apaac_st(file,output,lambdaval,v):
    filename, file_extension = os.path.splitext(file)
    apaac_1_split(file,lambdaval,v)
    aac_comp(file,v)
    data1 = pd.read_csv(filename+".aac")
    data2 = pd.read_csv(filename+".plam")
    df3 = pd.concat([data1.iloc[:,:-1],data2], axis = 1).reset_index(drop=True)
    header = []
    header1 = ('hydrphobicity','hydrophilicity','sidechainmass')
    for h in range(1,v+1):
        for e in std:
            header.append(e+"_s"+str(h))
        for r in range(1,lambdaval+1):
            for s in header1:
                header.append("lam_"+str(r)+"_"+s+"_s"+str(h))
    bb = []
    for i in range(0,len(df3),v):
        aa = []
        for j in range(v):
            aa.extend(df3.loc[i+j])
        bb.append(aa)
    zz = pd.DataFrame(bb)
    zz.columns = header
    zz.to_csv(output, index = None)    
    zz.columns=header
    zz.to_csv(output, index = None)
    os.remove(filename+".plam")
    os.remove(filename+".aac")
    os.remove(filename+".more")
