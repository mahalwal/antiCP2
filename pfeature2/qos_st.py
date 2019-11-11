import os
import sys
import numpy as np
import pandas as pd
import getopt
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
	
std = list('ACDEFGHIKLMNPQRSTVWY')
def qos_st(file,output,gap,v,w):
    file1 = split(file,v)
    ff = []
    filename, file_extension = os.path.splitext(file)
    df2=file1
    #df = pd.read_csv(file, header = None)
    #df2 = pd.DataFrame(df[0].str.upper())
    for i in range(0,len(df2)):
        ff.append(len(df2[0][i]))
    if min(ff) < gap:
        print("Error: All sequences' length should be higher than :", gap)
    else:
        mat1 = pd.read_csv("Schneider-Wrede.csv", index_col = 'Name')
        mat2 = pd.read_csv("Grantham.csv", index_col = 'Name')
        s1 = []
        s2 = []
        for i in range(0,len(df2)):
            for n in range(1, gap+1):
                sum1 = 0
                sum2 = 0
                for j in range(0,(len(df2[0][i])-n)):
                    sum1 = sum1 + (mat1[df2[0][i][j]][df2[0][i][j+n]])**2
                    sum2 = sum2 + (mat2[df2[0][i][j]][df2[0][i][j+n]])**2
                s1.append(sum1)
                s2.append(sum2)
        zz = pd.DataFrame(np.array(s1).reshape(len(df2),gap))
        zz["sum"] = zz.sum(axis=1)
        zz2 = pd.DataFrame(np.array(s2).reshape(len(df2),gap))
        zz2["sum"] = zz2.sum(axis=1)
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        h1 = []
        h2 = []
        h3 = []
        h4 = []
        for aa in std:
            h1.append('SC_' + aa)
        for aa in std:
            h2.append('G_' + aa)
        for n in range(1, gap+1):
            h3.append('SC_' + str(n))
        for n in range(1, gap+1):
            h4.append('G_' + str(n))
        for i in range(0,len(df2)):
            AA = {}
            for j in std:
                AA[j] = df2[0][i].count(j)
                c1.append(AA[j] / (1 + w * zz['sum'][i]))
                c2.append(AA[j] / (1 + w * zz2['sum'][i]))
            for k in range(0,gap):
                c3.append((w * zz[k][i]) / (1 + w * zz['sum'][i]))
                c4.append((w * zz[k][i]) / (1 + w * zz['sum'][i]))
        pp1 = np.array(c1).reshape(len(df2),len(std))
        pp2 = np.array(c2).reshape(len(df2),len(std))
        pp3 = np.array(c3).reshape(len(df2),gap)
        pp4 = np.array(c4).reshape(len(df2),gap)
        zz5 = round(pd.concat([pd.DataFrame(pp1, columns = h1),pd.DataFrame(pp2,columns = h2),pd.DataFrame(pp3, columns = h3),pd.DataFrame(pp4, columns = h4)], axis = 1),4)
        head_qos = []
        header_qos = ['SC_A','SC_C','SC_D','SC_E','SC_F','SC_G','SC_H','SC_I','SC_K','SC_L','SC_M','SC_N','SC_P','SC_Q','SC_R','SC_S','SC_T','SC_V','SC_W','SC_Y','G_A','G_C','G_D','G_E','G_F','G_G','G_H','G_I','G_K','G_L','G_M','G_N','G_P','G_Q','G_R','G_S','G_T','G_V','G_W','G_Y']
        for i in range(1,v+1):
            for j in header_qos:
                head_qos.append(j+'_s'+str(i))
            for k in range(1,gap+1):
                head_qos.append("SC_"+str(k)+'_s'+str(i))
            for k in range(1,gap+1):    
                head_qos.append("G_"+str(k)+'_s'+str(i))
        bb = []
        for c in range(0,len(zz5),v):
            aa = []
            for j in range(v):
                aa.extend(zz5.loc[c+j])
            bb.append(aa)
        zz = pd.DataFrame(bb)
        zz.columns = head_qos
        zz.to_csv(output, index = None)
