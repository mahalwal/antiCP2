import math
from collections import Counter
import collections
import pandas as pd
import numpy as np
import os
import csv
import sys
import getopt

def splitstring(string, length):#length should be greater than 0&1.
    leng=math.floor(len(string)/length)
    s={}
    V={}
    for i in range(0, len(string), leng):
        if i==((leng*(length-1))):
            s=(string[0+i:len(string)])
            V[i]=str(s)
            break;
        else: 
            s=(string[0+i:leng+i])
            V[i]=str(s)
             
    return (list(V.values()))

def entropy_single(seq):
    seq=seq.upper()
    num, length = Counter(seq), len(seq)
    return -sum( freq/length * math.log(freq/length, 2) for freq in num.values())

def se_st(filename,outt,length):
    Y=[]
    Z=[]
    x = 0
    #length=3
    df = pd.DataFrame(columns=['Sequence','Sub-sequence'])
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    for i in range(len(data)):
        data1=''
        data1=str(data[i])
        data1=data1.upper()
        allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
        is_data_invalid = set(data1).issubset(allowed)   
        if is_data_invalid==False:
            print("Error: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
            return
        df.at[i,'Sequence'] = data[i]
        Y.append(list(splitstring(str(data[i]),length)))
#     print(data)
    val2=[[]]
    for i in range(length):
        val2[0]=val2[0]+["SE_split_"+str(i+1)]
    for j in range(len(data)):
        val=[]
#         val.append(data[j])
        for k in range(len(Y[j])):
            val=val+[round(entropy_single(str(Y[j][k])),3)]
        val2.append(val)
#     print(val2)
    #file= open(sys.argv[3],'w', newline='')#output file
    file= open(outt,'w', newline='')#output file
    with file:
        writer=csv.writer(file);
        writer.writerows(val2);
#     print(df)
    return val2

