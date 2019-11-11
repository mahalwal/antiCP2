import pandas as pd
import os
import math
import sys
import getopt
import glob
import time
import numpy as np
from time import sleep
def rest(file,n,c):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][n:-c])
        df4 = pd.DataFrame(df3)
        #df4.to_csv(filename+".rest", index = None, header = False, encoding = 'utf-8')
    return df4
data1 = pd.read_csv("data", sep = "\t")
std = list('ACDEFGHIKLMNPQRSTVWY')
def val(AA_1, AA_2, aa, mat):
    return sum([(mat[i][aa[AA_1]] - mat[i][aa[AA_2]]) ** 2 for i in range(len(mat))]) / len(mat)
def paac_1(file,lambdaval,v,u,w):
    filename, file_extension = os.path.splitext(file)
    df = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][v:-u])
        df4 = pd.DataFrame(df3)
        df4.to_csv(filename+".rest", index = None, header = False, encoding = 'utf-8')
    df1 = pd.read_csv(filename+".rest", header = None)
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
    head = []
    for n in range(1, lambdaval + 1):
        head.append('lam_' + str(n))
    pp = pd.DataFrame()
    ee = []
    tt = []
    for k in range(0,len(df1)):
        cc = []
        pseudo1 = []
        for n in range(1,lambdaval+1):
            cc.append(sum([val(df1[0][k][p], df1[0][k][p + n], aa, dd) for p in range(len(df1[0][k]) - n)]) / (len(df1[0][k]) - n))
            qq = pd.DataFrame(cc)
        tt.append(cc)
        np.savetxt(filename+".more", tt, delimiter=",")
        pseudo = pseudo1 + [(w * p) / (1 + w * sum(cc)) for p in cc]
        ee.append(pseudo)
        ii = round(pd.DataFrame(ee, columns = head),4)
        ii.to_csv(filename+".lam_rest",index = None)
def aac_comp(file,v,u,w):
    filename, file_extension = os.path.splitext(file)
    df31 = pd.read_csv(filename+".more", header=None)
    df31["sum"] = df31.sum(axis=1)
    f = open(filename+".aac_paac_rest", 'w')
    sys.stdout = f
    df = rest(file,v,u)
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
def paac_rt(file,outt,lambdaval,v,u,w=0.05):
    filename, file_extension = os.path.splitext(file)
    paac_1(file,lambdaval,v,u,w=0.05)
    aac_comp(file,v,u,w)
    data1 = pd.read_csv(filename+".aac_paac_rest")
    data2 = pd.read_csv(filename+".lam_rest")
    data3 = pd.concat([data1.iloc[:,:-1],data2], axis = 1).reset_index(drop=True)
    data3.to_csv(outt, index = None)
    os.remove(filename+".more")
    os.remove(filename+".lam_rest")
    os.remove(filename+".aac_paac_rest")
    os.remove(filename+".rest")	
