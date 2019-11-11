
import math
from collections import Counter
import pandas as pd
import numpy as np
import os
import sys
import csv
import getopt
def splitstring(filename, num):#length should be greater than 0.
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    v=[]
    for i in range(len(data)):
        leng=math.floor(len(data[i])/num)
        s=[]
        for j in range(0, len(data[i]), leng):
            if j==((leng*(num-1))):
                s=s+[data[i][0+j:len(data[i])]]
                break;
            else: 
                s=s+[data[i][0+j:leng+j]]
        v.append(s)      
    return (v)

def ser_st(filename,output,num):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    LS=splitstring(filename,num)
    GH=[[]]
    for i in range(num):
        GH[0]=GH[0]+list(('A_split_'+str(i+1),'C_split_'+str(i+1),'D_split_'+str(i+1),'E_split_'+str(i+1),'F_split_'+str(i+1),'G_split_'+str(i+1),'H_split_'+str(i+1),'I_split_'+str(i+1),'K_split_'+str(i+1),'L_split_'+str(i+1),'M_split_'+str(i+1),'N_split_'+str(i+1),'P_split_'+str(i+1),'Q_split_'+str(i+1),'R_split_'+str(i+1),'S_split_'+str(i+1),'T_split_'+str(i+1),'V_split_'+str(i+1),'W_split_'+str(i+1),'Y_split_'+str(i+1)))
    for i in range(len(LS)):
        SE=[]
        for k in range(len(LS[i])):
            my_list={'A':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'V':0,'W':0,'Y':0}
            data1=''
            data1=str(LS[i][k])
            data1=data1.upper()
            allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
            is_data_invalid = set(data1).issubset(allowed)   
            if is_data_invalid==False:
                print("Error: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
                return
            seq=LS[i][k]
            seq=seq.upper()
            num, length = Counter(seq), len(seq)
            num=dict(sorted(num.items()))
            C=list(num.keys())
            F=list(num.values())
            for key, value in my_list.items():
                for j in range(len(C)):
                    if key == C[j]:
                        my_list[key] = round(((F[j]/length)* math.log(F[j]/length, 2)),3)
            SE=SE+list(my_list.values())
        GH.append(SE)
    file= open(output,'w', newline='')#output file
    with file:
        writer=csv.writer(file);
        writer.writerows(GH);
    return GH

# Example
#ser_st("C:/Users/anjali/Desktop/Python_scripts/shannon.csv")# Input file
