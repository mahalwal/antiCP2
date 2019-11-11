import os
import sys
import numpy as np
import pandas as pd
import getopt
def soc_wp(file,outt,gap):
    ff = []
    filename, file_extension = os.path.splitext(file)
    df = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df[0].str.upper())
    for i in range(0,len(df2)):
        ff.append(len(df2[0][i]))
    if min(ff) < gap:
        print("Error: All sequences' length should be higher than :", gap)
        return 0
    mat1 = pd.read_csv("Data\Schneider-Wrede.csv", index_col = 'Name')
    mat2 = pd.read_csv("Data\Grantham.csv", index_col = 'Name')
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
    zz3.to_csv(outt, index = None, encoding = 'utf-8') 
