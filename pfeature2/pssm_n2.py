#!/usr/bin/python

import sys, getopt
import numpy as np
import pandas as pd
import os
def pssm_n2(file,out):
   filename,file_ext=os.path.splitext(file)   
   df=pd.read_csv(file, sep=',',header=None)
   df1 = df.iloc[:,0:21]
   a = 1000
   b = -1000
   def pssm(x):
       # that, if x is a string,
       if type(x) is str:
           # just returns it untouched
           return x
       # but, if not, return it multiplied by 100
       elif x:
           return (x-a)/(b - a)
        # and leave everything else
       else:
           return
   df2 = df1.applymap(pssm)
   df2.to_csv(out, encoding='utf-8', index=False, header=False)
