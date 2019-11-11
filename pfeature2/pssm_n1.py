#!/usr/bin/python

import sys, getopt
import numpy as np
import pandas as pd
import os
def pssm_n1(file,output):
   filename,file_ext=os.path.splitext(file)
   df=pd.read_csv(file,header=None)
   df1 = df.iloc[:,0:21]
   def pssm(x):
       # that, if x is a string,
       if type(x) is str:
           # just returns it untouched
           return x
       # but, if not, return it multiplied by 100
       elif x:
           return (1/(1+(2.7182)**(-x)))
        # and leave everything else
       else:
           return
   df2 = df1.applymap(pssm)
   df2.to_csv(output, encoding='utf-8', index=False, header=False)		 
