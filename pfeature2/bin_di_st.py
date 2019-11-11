import os
import sys
import numpy as np
import pandas as pd
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
	
def bin_di_st(file,output,q,n):
    file1 = split(file,n)
    filename, file_extension = os.path.splitext(file)
    #df2=pd.read_csv(file,header=None)
    #df = pd.DataFrame(df2[0].str.upper())
    df = file1
    mat3 = pd.read_csv("bin_di.csv", header = None)
    mat3.set_index(0, inplace = True)
    mat3.index = pd.Series(mat3.index).replace(np.nan,'NA')
    f = open(filename+".bin_di", 'w')
    sys.stdout = f
    for i in range(0,len(df)):
        for j in range(0,(len(df[0][i])-(q+1))):
            temp1 = df[0][i][j:j+q+2:q+1]
            for each in (mat3.loc[temp1].values.ravel()):
                print("%.0f"%each, end = ",", flush = True)
        print("")
    f.truncate()
    ff1 = open(output,'w')
    sys.stdout=ff1
    with open(filename+".bin_di","r") as f:
        fob = f.readlines()
    for each in range(0,len(fob),n):
        print(','.join(fob[each:each+n]).replace(",\n,",",").replace("\n",""))
    ff1.truncate()
    os.remove(filename+".bin_di")
