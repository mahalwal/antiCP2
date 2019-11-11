
# coding: utf-8

# In[5]:


# autocorr('filepath','aaindex',d)
#input: csv of sequences, aaindex of property for which autocorrelation descriptors are to be estimated, d is the lag (<=30)
#output: for every sequence (with aaindex and d fixed) three autocorrelation values - NMB,Moran and Geary

import math
import pandas as pd
import numpy as np
import os
import csv
import sys
import getopt
import warnings
warnings.filterwarnings("ignore") 
def splitstring_N(filename, Nlength):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    s=[]
    for i in range(len(data)):
            s=s+[data[i][:Nlength]]
    return (s)
def p_aa(prop,a):
    if ((a.upper()=='A') or (a.upper()=='C') or (a.upper()=='D') or (a.upper()=='E') or (a.upper()=='F') or (a.upper()=='G') or (a.upper()=='H') or (a.upper()=='I') or (a.upper()=='K') or (a.upper()=='L') or (a.upper()=='M') or (a.upper()=='N') or (a.upper()=='P') or (a.upper()=='Q') or (a.upper()=='R') or (a.upper()=='S') or (a.upper()=='T') or (a.upper()=='V') or (a.upper()=='W') or (a.upper()=='Y')):
        data=pd.read_table('z_aaindex.csv',sep=',',index_col='INDEX' )
        p=data.loc[prop][a.upper()]
        return p
    else:
        print("Error!: Invalid sequence. Special character(s)/invalid amino acid letter(s) present in input.")
        return  
def NMB(prop,seq,d):
    if (d<=30):
        sum=0
        for i in range(len(seq)-d):
            sum=sum+p_aa(prop,seq[i])*p_aa(prop,seq[i+d])
        ats=sum/(len(seq)-d)
        return ats
    else:
        print("Error!: d should be less than equal to 30")
        return
def pav(prop,seq):
    av=0
    for i in range(len(seq)):
        av=av+p_aa(prop,seq[i])
    av=av/len(seq)
    return av
def moran(prop,seq,d):
    if (d<=30):
        s1=0
        s2=0
        p_bar=pav(prop,seq)
        for i in range(len(seq)-d):
            s1=s1+(p_aa(prop,seq[i])-p_bar)*(p_aa(prop,seq[i+d])-p_bar)
        for i in range(len(seq)):
            s2=s2+(p_aa(prop,seq[i])-p_bar)*(p_aa(prop,seq[i])-p_bar)
        return (s1/(len(seq)-d))/(s2/len(seq))
    else:
        print("Error!: d should be less than equal to 30")
        return
def geary(prop,seq,d):
    if (d<=30):
        s1=0
        s2=0
        p_bar=pav(prop,seq)
        for i in range(len(seq)-d):
            s1=s1+(p_aa(prop,seq[i])-p_aa(prop,seq[i+d]))*(p_aa(prop,seq[i])-p_aa(prop,seq[i+d]))
        for i in range(len(seq)):
            s2=s2+(p_aa(prop,seq[i])-p_bar)*(p_aa(prop,seq[i])-p_bar)
        return (s1/(2*(len(seq)-d)))/(s2/(len(seq)-1))
    else:
        print("Error!: d should be less than equal to 30")
        return
def acr_nt(filename,outt,n,d):
    if (d<=30):
        seq_data=splitstring_N(filename, n)
        prop=list((pd.read_csv('aaindices.csv',sep=',',header=None)).iloc[0,:])
        output=[[]]
        for k in range(len(prop)):
            output[0]=output[0]+['NMB_ac','Moran_ac','Geary_ac']
        temp=[]
        #header=['Sequence','aaindex','Normalized Moreau-Broto','Moran','Geary']
        #output.append(header)
        for i in range(len(seq_data)):
            for j in range(len(prop)):
                temp=temp+[round(NMB(prop[j],seq_data[i],d),3),round(moran(prop[j],seq_data[i],d),3),round(geary(prop[j],seq_data[i],d),3)]
            output.append(temp)
            temp=[]
        file = open(outt,'w')
        with file:
            writer = csv.writer(file);
            writer.writerows(output);
        return output
    else:
        print("Error!: d should be less than equal to 30")
        return
