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

def splitstring_res(filename,Nlength,Clength):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    s=[]
    s1=[]
    for i in range(len(data)):
        s=data[i][Nlength:]
        s1=s1+[s[:-Clength]] 
    return (s1)

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


def ctc_rt(filename,outt,num1,num2):
    #num1=5
    #num2=5
    df = pd.DataFrame(columns=['Sequence','Triad:Frequency'])
    data=splitstring_res(filename,num1,num2)
    for i in range(len(data)):
        data1=''
        data1=str(data[i])
        data1=data1.upper()
        allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
        is_data_invalid = set(data1).issubset(allowed)   
        if is_data_invalid==False:
            print("Errror: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
            return
        df.at[i,'Sequence'] = data[i]
        Y.append("".join(repstring(str(data[i]))))
    val2=[[]]
    for f in range(len(LS)):
        val2[0]=val2[0]+["triad_"+str(LS[f])]
    for j in range(len(data)):
        MM=[]
        for m in range(len(LS)):
            MM=MM+[occurrences(Y[j],LS[m])]
        Min_MM=min(MM)
        Max_MM=max(MM)
        if (Max_MM==0):
            print("Errror: Splits/ Sequence length should be greater than equal to 3")
            return
        val=[]
#         val.append(data[j])
        for k in range(len(LS)):
            val=val+[round(((occurrences(Y[j],LS[k])-Min_MM)/Max_MM),3)]
        val2.append(val)    
#     print(val2)
    #file= open(sys.argv[2],'w', newline='')#output file
    file= open(outt,'w', newline='')
    with file:
        writer=csv.writer(file);
        writer.writerows(val2);
    return val2
