
# coding: utf-8

# In[ ]:


import pandas as pd
import csv
import math
import numpy as np
import sys
import getopt


# In[ ]:


# Secondary functions, move to next section

#Single function to calculate 30 physico che
#Finding physico-chemical property of a vector of polypeptides

#PCP= pd.read_csv('/Users/gaurav/Desktop/Prof_GPS_Raghava/Code/AAPcProp.csv', header=None) #Our reference table for properties
PCP = pd.read_csv('PhysicoChemical.csv',header=None);
headers = ['Positively charged',
'Negatively charged',
'Neutral charged',
'Polarity',
'Non polarity',
'Aliphaticity',
'Cyclic',
'Aromaticity',
'Acidicity',
'Basicity',
'Neutral (ph)',
'Hydrophobicity',
'Hydrophilicity',
'Neutral',
'Hydroxylic',
'Sulphur content',
'Secondary Structure(Helix)',
'Secondary Structure(Strands)',
'Secondary Structure(Coil)',
'Solvent Accessibilty (Buried)',
'Solvent Accesibilty(Exposed)',
'Solvent Accesibilty(Intermediate)',
'Tiny',
'Small',
'Large',
'z1',
'z2',
'z3',
'z4',
'z5'];


def encode(peptide):
    #letter = {'A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'};
    l=len(peptide);
    encoded=np.zeros(l);
    for i in range(l):
        if(peptide[i]=='A'):
            encoded[i] = 0;
        elif(peptide[i]=='C'):
            encoded[i] = 1;
        elif(peptide[i]=='D'):
            encoded[i] = 2;
        elif(peptide[i]=='E'):
            encoded[i] = 3;
        elif(peptide[i]=='F'):
            encoded[i] = 4;
        elif(peptide[i]=='G'):
            encoded[i] = 5;
        elif(peptide[i]=='H'):
            encoded[i] = 6;
        elif(peptide[i]=='I'):
            encoded[i] = 7;
        elif(peptide[i]=='K'):
            encoded[i] = 8;
        elif(peptide[i]=='L'):
            encoded[i] = 9;
        elif(peptide[i]=='M'):
            encoded[i] = 10;
        elif(peptide[i]=='N'):
            encoded[i] = 11;
        elif(peptide[i]=='P'):
            encoded[i] = 12;
        elif(peptide[i]=='Q'):
            encoded[i] = 13;
        elif(peptide[i]=='R'):
            encoded[i] = 14;
        elif(peptide[i]=='S'):
            encoded[i] = 15;
        elif(peptide[i]=='T'):
            encoded[i] = 16;
        elif(peptide[i]=='V'):
            encoded[i] = 17;
        elif(peptide[i]=='W'):
            encoded[i] = 18;
        elif(peptide[i]=='Y'):
            encoded[i] = 19;
        else:
            print('Wrong residue!');
    return encoded;


        
def lookup(peptide,featureNum):
    l=len(peptide);
    peptide = list(peptide);
    out=np.zeros(l);
    peptide_num = encode(peptide);
    
    for i in range(l):
        out[i] = PCP[peptide_num[i]][featureNum];
    return sum(out);


def pcp(file):
    
    if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    else:
        seq  = file;
    
    l = len(seq);

    rows = PCP.shape[0]; # Number of features in our reference table
    col = 20 ; # Denotes the 20 amino acids
    
    seq=[seq[i].upper() for i in range(l)]
    sequenceFeature = [];
    sequenceFeature.append(headers); #To put property name in output csv
    
    for i in range(l): # Loop to iterate over each sequence
        nfeatures = rows;
        sequenceFeatureTemp = [];
        for j in range(nfeatures): #Loop to iterate over each feature
            featureVal = lookup(seq[i],j)   
            if(len(seq[i])!=0):
                sequenceFeatureTemp.append(featureVal/len(seq[i]))
            else:
                sequenceFeatureTemp.append('NaN')
            
        sequenceFeature.append(sequenceFeatureTemp);
        
    out = pd.DataFrame(sequenceFeature);
    
    file = open('Output.csv','w')
    with file:
        writer = csv.writer(file);
        writer.writerows(sequenceFeature);
    return sequenceFeature;


# In[ ]:


'''

Function Name: phyChem
Description: Gives 30 physico-chemical properties of a sequence

Function prototype: phyChem(file,mode,m,n)

Input:
@file: an input csv file with multiple sequences
@mode(optional, default = 'all'):
    Values possible: 
        1) (default)'all' : to get features of entire protein
        2) 'NT' : to get the features of first n N-Terminal residues
        3) 'CT' : to get the features of last n C-Terminal residues
        4) 'rest' : to get the features of a sub-sequence from mth position to nth position(both inclusive)
@m(optional(mandatory if 'rest' is chosen, default=0): m is the start position of residue 
@n(optional, default = '0'): n is the number of residues you want from desired terminal or end point (if 'rest' is chosen)


Output: 
A matrix (csv file) of dimension (m x 30) containing sequences as rows and their 30 physico-chemical properties as columns
where m = number of sequences (each sequence separated by comma) 

'''


def split(seq, parts):

    l=len(seq);
    
    sublen = math.floor(l/parts);
    k=0;
    splits=['']*parts;
    for i in range(parts):
            
            if(i!=parts-1):
                splits[i] = seq[k:k+sublen];
                k+=sublen;
            else:
                
                splits[i] = seq[k:l];
    return splits;


# In[ ]:


'''
Function Name: phychem_split
Description: Splits each sequence into sub-parts and gives physico-chemical properties of each split part

Prototype: phychem_split(file,parts)

Input:

@file: Path to the csv file (each sequence is separated by a comma) or list of peptide sequences
@parts: Number of splits to make in each sequence, eg. if sequence is 'aaccddccae' and parts is 3, it will split it as 'aac','cdd', 'ccae'

Output:

A csv file, stored in the same path as 'Spit output.csv'

With each sequence represented as rows and its splits and properties as columns.

'''


def pcp_st(file,outt,parts):
     
    # Input the sequence
    
    if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
        
    else:
        seq  = file;
    
    # print(seq)
    # Find property of each big sequence(ith) and split it and then store property of each split(jth) in templist, add this templist to the final list
    l=len(seq);
    #print(l)
    
    
    # To store property of each subpart of all the sequences, this will be returned
    phychemProp = [None]*l;
    seq=[seq[i].upper() for i in range(l)];
    
    for i in range(l):
        splits = split(seq[i],parts);
        
        #print(splits)
        templist = [None]*(parts*2); # 31 = 30(number of properties)+1(to store the split sequence) [each for 1 big sequence]
        k=0;
        
        for j in range(parts):
            #print('i=',i,'j=',j)
            templist[k] = splits[j]
            temp = phyChem([splits[j]])
            templist[k+1]= temp[1][:]; # To remove header row
            k+=2;
        phychemProp[i] = templist;
        
    #print(templist)
    
    file = open(outt,'w')
    with file:
        writer = csv.writer(file);
        writer.writerows(phychemProp);
    return phychemProp;
