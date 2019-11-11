
import math
from collections import Counter
import pandas as pd
import numpy as np
import os
import sys
import csv
import getopt

def ser_wp(filename,outt):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    data2=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    Val=np.zeros(len(data))
    GH=[]
    for i in range(len(data)):
        my_list={'A':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'V':0,'W':0,'Y':0}
        data1=''
        data1=str(data[i])
        data1=data1.upper()
        allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
        is_data_invalid = set(data1).issubset(allowed)   
        if is_data_invalid==False:
            print("Error: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
            return
        seq=data[i]
        seq=seq.upper()
        num, length = Counter(seq), len(seq)
        num=dict(sorted(num.items()))
        C=list(num.keys())
        F=list(num.values())
        for key, value in my_list.items():
             for j in range(len(C)):
                if key == C[j]:
                    my_list[key] = round(((F[j]/length)* math.log(F[j]/length, 2)),3)
        GH.append(list(my_list.values()))
    file= open(outt,'w', newline='')#output file
    with file:
        writer=csv.writer(file);
        writer.writerow(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'));		
        writer.writerows(GH);
    return(GH)

