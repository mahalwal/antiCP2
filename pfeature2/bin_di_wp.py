import os
import sys
import numpy as np
import pandas as pd
import getopt
def bin_di_wp(file,outt,q):
    filename, file_extension = os.path.splitext(file)
    df2=pd.read_csv(file,header=None)
    df = pd.DataFrame(df2[0].str.upper())
    mat3 = pd.read_csv("bin_di.csv", header = None)
    mat3.set_index(0, inplace = True)
    mat3.index = pd.Series(mat3.index).replace(np.nan,'NA')
    f = open(outt+"_"+str(q), 'w')
    sys.stdout = f
    for i in range(0,len(df)):
        for j in range(0,(len(df[0][i])-(q+1))):
            temp1 = df[0][i][j:j+q+2:q+1]
            for each in (mat3.loc[temp1].values.ravel()):
                print("%.0f"%each, end = ",", flush = True)
        print("")
    f.truncate()
