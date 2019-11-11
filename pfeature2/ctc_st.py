#!/usr/bin/env python
# coding: utf-8

import math
from collections import Counter
import pandas as pd
import numpy as np
import os
import csv
import itertools
import re
import itertools
import sys
import getopt
x = [1, 2, 3, 4, 5, 6,7]
p=[]
Y=[]
LS=[]

def splitstring(filename,num):#length should be greater than 0.
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    v=[]
    for i in range(len(data)):
        leng=math.floor(len(data[i])/num)
        s=[]
        #print(data[i])
        for j in range(0, len(data[i]), leng):
            if j==((leng*(num-1))):
                s=s+[data[i][0+j:len(data[i])]]
                break;
            else: 
                s=s+[data[i][0+j:leng+j]]
        v.append(s)     
    return (v)

for i in range(len(x)):
    p=itertools.product(x,repeat=3)
    p=list(p)
    
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

for i in range(len(p)):
    LS.append(concatenate_list_data(p[i]))
    
def repstring(string):
    string=string.upper()
    char={"A":"1","G":"1","V":"1","I":"2","L":"2","F":"2","P":"2","Y":"3","M":"3","T":"3","S":"3","H":"4","N":"4","Q":"4","W":"4","R":"5","K":"5","D":"6","E":"6","C":"7"}
    string=list(string)
    for index,item in enumerate(string):
        for key,value in char.items():
            if item==key:
                string[index]=value
    return("".join(string))

def occurrences(string, sub_string):
    count=0
    beg=0
    while(string.find(sub_string,beg)!=-1) :
        count=count+1
        beg=string.find(sub_string,beg)
        beg=beg+1
    return count


def ctc_st(filename,out,num):
    df = pd.DataFrame(columns=['Sequence','Triad:Frequency'])
    data=splitstring(filename,num)
    for k in range(len(data)):
        for i in range(num):
            data1=''
            data1=str(data[k][i])
            data1=data1.upper()
            allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
            is_data_invalid = set(data1).issubset(allowed)   
            if is_data_invalid==False:
                print("Errror: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
                return
                df.at[i,'Sequence'] = data[k][i]
            Y.append((repstring(str(data[k][i]))))
    Z=[Y[i:i+3] for i in range(0, len(Y), num)] 
    val2=[[]]
    for h in range(num):
        for f in range(len(LS)):
            val2[0]=val2[0]+["triad_"+str(LS[f])+"_split_"+str(h+1)]
    for x in range(len(data)):
        Min_MMM=[]
        Max_MMM=[]
        Min_MM=0
        Max_MM=0
        for g in range(num):
            MM=[]
            for m in range(len(LS)):
                MM=MM+[occurrences(Z[x][g],LS[m])]
            Min_MM=min(MM)
            Max_MM=max(MM)
            if (Max_MM==0):
                print("Errror: Splits/ Sequence length should be greater than equal to 3")
                return
            Min_MMM=Min_MMM+[Min_MM]
            Max_MMM=Max_MMM+[Max_MM]
        val=[]
        for j in range(0,len(data[x])):
            for k in range(len(LS)):
                val=val+[round(((occurrences(Z[x][j],LS[k])-Min_MMM[j])/Max_MMM[j]),3)]
        val2.append(val)    
    file= open(out,'w', newline='')#output file
    with file:
        writer=csv.writer(file);
        writer.writerows(val2);
    return val2
