import pandas as pd
import os
import sys
import getopt
def pat_csv(file,n,out):
    filename,file_ext = os.path.splitext(file)
    df3 = pd.read_csv(file, header=None)
    ss = []
    f = open(out, 'w')
    sys.stdout = f
    for i in range(0,len(df3)):
        ss.append([i])
        for j in range(0,(len(df3.loc[i])-n+1)):
            ss[i].append(df3.loc[i][j:j+n].values)
    for i in range(0,len(ss)) :
        for j in range(1,len(ss[i])) :
            for each in ss[i][j][0:len(ss[i][j])] :
                print(each, end=",")
        print("")
    f.truncate()
