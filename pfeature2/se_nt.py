
import math
from collections import Counter
import pandas as pd
import numpy as np
import os
import sys
import csv
import getopt

def splitstring_N(filename, Nlength):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    s=[]
    for i in range(len(data)):
            s=s+[data[i][:Nlength]]
    return (s)

def entropy_single(seq):
    seq=seq.upper()
    num, length = Counter(seq), len(seq)
    return -sum( freq/length * math.log(freq/length, 2) for freq in num.values())

def se_nt(filename,outt,nt):
    data=splitstring_N(filename,nt)
#     print(data)
    Val=[]
    header=["Shannon-Entropy"]
    for i in range(len(data)):
        data1=''
        data1=str(data[i])
        data1=data1.upper()
        allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
        is_data_invalid = set(data1).issubset(allowed)   
        if is_data_invalid==False:
            print("Error: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
            return
        Val.append(round((entropy_single(str(data[i]))),3))
        #print(Val[i])
        file= open(outt,'w', newline='\n')#output file
        with file:
            writer=csv.writer(file,delimiter='\n');
            writer.writerow(header)
            writer.writerow(Val);
    return Val

