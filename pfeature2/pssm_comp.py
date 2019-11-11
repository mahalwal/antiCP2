import sys, getopt
import numpy as np
import pandas as pd
import os
def pssm_comp(file,out):
   filename, file_ext = os.path.splitext(file)
   aa = list("ACDEFGHIKLMNPQRSTVWY")
   df=pd.read_csv(file, header=None)
   df.set_index(0,inplace=True)
   Matrix = [[0 for x in range(0,20)] for y in range(0,20)]
   j = 0
   df2 = []
   for i in aa:
      if i in df.index[:]:
         df1 = df.loc[i]
         df2 = (df1.sum(axis=0)/len(df))
         Matrix[j] =np.asarray(df2)
         j = j+1
      else:
         j = j+1
   f = open(out, 'w')
   sys.stdout = f
   for each in Matrix:
       for j in each:
           print("%.4f"%j,end=",")
   f.close()
