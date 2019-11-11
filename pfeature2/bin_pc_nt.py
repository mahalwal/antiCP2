
# coding: utf-8

# In[11]:


#!/usr/bin/env python
'''

This function gives binary profile of residues from C terminal sequence for the chosen feature


'''

'''

Total 3 Command Line arguments:

arg1 = sequence (Comma separated)

arg2 = n, number of residues to be taken(Example: if sequence is 'aaccdcdc' and n is 3, then CTerminal residue would be 'cdc')

arg3 = feature number (valid number, 0-24) against 

    FEATURE NAME                    FEATURE NUMBER

    'Positively charged' --                  0
    'Negatively charged' --                  1
    'Neutral charged' --                     2
    'Polarity' --                            3
    'Non polarity' --                        4
    'Aliphaticity' --                        5
    'Cyclic' --                              6
    'Aromaticity' --                         7
    'Acidicity'--                            8
    'Basicity'--                             9
    'Neutral (ph)' --                       10
    'Hydrophobicity' --                     11
    'Hydrophilicity' --                     12
    'Neutral' --                            13
    'Hydroxylic' --                         14
    'Sulphur content' -                     15
    'Secondary Structure(Helix)'            16 
    'Secondary Structure(Strands)',         17
    'Secondary Structure(Coil)',            18
    'Solvent Accessibilty (Buried)',        19
    'Solvent Accesibilty(Exposed)',         20
    'Solvent Accesibilty(Intermediate)',    21
    'Tiny',                                 22
    'Small',                                23 
    'Large'                                 24 

arg4 = output

'''

# coding: utf-8




# In[14]:


import sys
import pandas as pd
import numpy as np
import csv
import itertools
import math
import getopt

#Finding physico-chemical property of a vector of polypeptides

#PCP= pd.read_csv('/usr1/webserver/cgidocs/raghava/pfeature/files/PhysicoChemical.csv', header=None) #Our reference table for properties
#PCP = pd.read_csv('/Users/gaurav/Desktop/Prof_GPS_Raghava/Code/AAPcProp.csv',header=None)
PCP= pd.read_csv('PhysicoChemical.csv', header=None)

headerNT = ['Positively charged_NT_1', 'Positively charged_NT_2', 'Positively charged_NT_3', 'Positively charged_NT_4', 'Positively charged_NT_5', 'Positively charged_NT_6', 'Positively charged_NT_7', 'Positively charged_NT_8', 'Positively charged_NT_9', 'Positively charged_NT_10', 'Negatively charged_NT_1', 'Negatively charged_NT_2', 'Negatively charged_NT_3', 'Negatively charged_NT_4', 'Negatively charged_NT_5', 'Negatively charged_NT_6', 'Negatively charged_NT_7', 'Negatively charged_NT_8', 'Negatively charged_NT_9', 'Negatively charged_NT_10', 'Neutral charged_NT_1', 'Neutral charged_NT_2', 'Neutral charged_NT_3', 'Neutral charged_NT_4', 'Neutral charged_NT_5', 'Neutral charged_NT_6', 'Neutral charged_NT_7', 'Neutral charged_NT_8', 'Neutral charged_NT_9', 'Neutral charged_NT_10', 'Polarity_NT_1', 'Polarity_NT_2', 'Polarity_NT_3', 'Polarity_NT_4', 'Polarity_NT_5', 'Polarity_NT_6', 'Polarity_NT_7', 'Polarity_NT_8', 'Polarity_NT_9', 'Polarity_NT_10', 'Non polarity_NT_1', 'Non polarity_NT_2', 'Non polarity_NT_3', 'Non polarity_NT_4', 'Non polarity_NT_5', 'Non polarity_NT_6', 'Non polarity_NT_7', 'Non polarity_NT_8', 'Non polarity_NT_9', 'Non polarity_NT_10', 'Aliphaticity_NT_1', 'Aliphaticity_NT_2', 'Aliphaticity_NT_3', 'Aliphaticity_NT_4', 'Aliphaticity_NT_5', 'Aliphaticity_NT_6', 'Aliphaticity_NT_7', 'Aliphaticity_NT_8', 'Aliphaticity_NT_9', 'Aliphaticity_NT_10', 'Cyclic_NT_1', 'Cyclic_NT_2', 'Cyclic_NT_3', 'Cyclic_NT_4', 'Cyclic_NT_5', 'Cyclic_NT_6', 'Cyclic_NT_7', 'Cyclic_NT_8', 'Cyclic_NT_9', 'Cyclic_NT_10', 'Aromaticity_NT_1', 'Aromaticity_NT_2', 'Aromaticity_NT_3', 'Aromaticity_NT_4', 'Aromaticity_NT_5', 'Aromaticity_NT_6', 'Aromaticity_NT_7', 'Aromaticity_NT_8', 'Aromaticity_NT_9', 'Aromaticity_NT_10', 'Acidicity_NT_1', 'Acidicity_NT_2', 'Acidicity_NT_3', 'Acidicity_NT_4', 'Acidicity_NT_5', 'Acidicity_NT_6', 'Acidicity_NT_7', 'Acidicity_NT_8', 'Acidicity_NT_9', 'Acidicity_NT_10', 'Basicity_NT_1', 'Basicity_NT_2', 'Basicity_NT_3', 'Basicity_NT_4', 'Basicity_NT_5', 'Basicity_NT_6', 'Basicity_NT_7', 'Basicity_NT_8', 'Basicity_NT_9', 'Basicity_NT_10', 'Neutral (ph)_NT_1', 'Neutral (ph)_NT_2', 'Neutral (ph)_NT_3', 'Neutral (ph)_NT_4', 'Neutral (ph)_NT_5', 'Neutral (ph)_NT_6', 'Neutral (ph)_NT_7', 'Neutral (ph)_NT_8', 'Neutral (ph)_NT_9', 'Neutral (ph)_NT_10', 'Hydrophobicity_NT_1', 'Hydrophobicity_NT_2', 'Hydrophobicity_NT_3', 'Hydrophobicity_NT_4', 'Hydrophobicity_NT_5', 'Hydrophobicity_NT_6', 'Hydrophobicity_NT_7', 'Hydrophobicity_NT_8', 'Hydrophobicity_NT_9', 'Hydrophobicity_NT_10', 'Hydrophilicity_NT_1', 'Hydrophilicity_NT_2', 'Hydrophilicity_NT_3', 'Hydrophilicity_NT_4', 'Hydrophilicity_NT_5', 'Hydrophilicity_NT_6',
            'Hydrophilicity_NT_7', 'Hydrophilicity_NT_8', 'Hydrophilicity_NT_9', 'Hydrophilicity_NT_10', 'Neutral_NT_1', 'Neutral_NT_2', 'Neutral_NT_3', 'Neutral_NT_4', 'Neutral_NT_5', 'Neutral_NT_6', 'Neutral_NT_7', 'Neutral_NT_8', 'Neutral_NT_9', 'Neutral_NT_10', 'Hydroxylic_NT_1', 'Hydroxylic_NT_2', 'Hydroxylic_NT_3', 'Hydroxylic_NT_4', 'Hydroxylic_NT_5', 'Hydroxylic_NT_6', 'Hydroxylic_NT_7', 'Hydroxylic_NT_8', 'Hydroxylic_NT_9', 'Hydroxylic_NT_10', 'Sulphur content_NT_1', 
            'Sulphur content_NT_2', 'Sulphur content_NT_3', 'Sulphur content_NT_4', 'Sulphur content_NT_5', 'Sulphur content_NT_6', 'Sulphur content_NT_7', 'Sulphur content_NT_8', 'Sulphur content_NT_9', 'Sulphur content_NT_10', 'Secondary Structure(Helix)_NT_1', 'Secondary Structure(Helix)_NT_2', 'Secondary Structure(Helix)_NT_3', 'Secondary Structure(Helix)_NT_4', 'Secondary Structure(Helix)_NT_5', 'Secondary Structure(Helix)_NT_6', 'Secondary Structure(Helix)_NT_7', 'Secondary Structure(Helix)_NT_8', 'Secondary Structure(Helix)_NT_9', 'Secondary Structure(Helix)_NT_10', 'Secondary Structure(Strands)_NT_1', 'Secondary Structure(Strands)_NT_2', 'Secondary Structure(Strands)_NT_3', 'Secondary Structure(Strands)_NT_4', 'Secondary Structure(Strands)_NT_5', 'Secondary Structure(Strands)_NT_6', 'Secondary Structure(Strands)_NT_7', 'Secondary Structure(Strands)_NT_8', 'Secondary Structure(Strands)_NT_9', 'Secondary Structure(Strands)_NT_10', 'Secondary Structure(Coil)_NT_1', 'Secondary Structure(Coil)_NT_2', 'Secondary Structure(Coil)_NT_3', 'Secondary Structure(Coil)_NT_4', 'Secondary Structure(Coil)_NT_5', 'Secondary Structure(Coil)_NT_6', 'Secondary Structure(Coil)_NT_7', 'Secondary Structure(Coil)_NT_8', 'Secondary Structure(Coil)_NT_9', 'Secondary Structure(Coil)_NT_10', 'Solvent Accessibilty (Buried)_NT_1', 'Solvent Accessibilty (Buried)_NT_2', 'Solvent Accessibilty (Buried)_NT_3', 'Solvent Accessibilty (Buried)_NT_4', 'Solvent Accessibilty (Buried)_NT_5', 'Solvent Accessibilty (Buried)_NT_6', 'Solvent Accessibilty (Buried)_NT_7', 'Solvent Accessibilty (Buried)_NT_8', 'Solvent Accessibilty (Buried)_NT_9', 'Solvent Accessibilty (Buried)_NT_10', 'Solvent Accesibilty(Exposed)_NT_1', 'Solvent Accesibilty(Exposed)_NT_2', 'Solvent Accesibilty(Exposed)_NT_3', 'Solvent Accesibilty(Exposed)_NT_4', 'Solvent Accesibilty(Exposed)_NT_5', 'Solvent Accesibilty(Exposed)_NT_6', 'Solvent Accesibilty(Exposed)_NT_7', 'Solvent Accesibilty(Exposed)_NT_8', 'Solvent Accesibilty(Exposed)_NT_9', 'Solvent Accesibilty(Exposed)_NT_10', 'Solvent Accesibilty(Intermediate)_NT_1', 'Solvent Accesibilty(Intermediate)_NT_2', 'Solvent Accesibilty(Intermediate)_NT_3', 'Solvent Accesibilty(Intermediate)_NT_4', 'Solvent Accesibilty(Intermediate)_NT_5', 'Solvent Accesibilty(Intermediate)_NT_6', 'Solvent Accesibilty(Intermediate)_NT_7', 'Solvent Accesibilty(Intermediate)_NT_8', 'Solvent Accesibilty(Intermediate)_NT_9', 'Solvent Accesibilty(Intermediate)_NT_10', 'Tiny_NT_1', 'Tiny_NT_2', 'Tiny_NT_3', 'Tiny_NT_4', 'Tiny_NT_5', 'Tiny_NT_6', 'Tiny_NT_7', 'Tiny_NT_8', 'Tiny_NT_9', 'Tiny_NT_10', 'Small_NT_1', 'Small_NT_2', 'Small_NT_3', 'Small_NT_4', 'Small_NT_5', 'Small_NT_6', 'Small_NT_7', 'Small_NT_8', 'Small_NT_9', 'Small_NT_10', 'Large_NT_1', 'Large_NT_2', 'Large_NT_3', 'Large_NT_4', 'Large_NT_5', 'Large_NT_6', 'Large_NT_7', 'Large_NT_8', 'Large_NT_9', 'Large_NT_10'];



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
    out=[];
    peptide_num = encode(peptide);
    
    for i in range(l):
        #out[i] = PCP[peptide_num[i]][featureNum];
        out.append(PCP[peptide_num[i]][featureNum]);
    return out;



# In[17]:
def split(file,mode='all',m=0,n=0):
    
    '''
    file = sys.argv[1];
    mode = sys.argv[2];
    m = int(sys.argv[3]);
    n  = int(sys.argv[4]);
    '''
    '''if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    #elif(type(file)==str && len(file))
    else:'''
    seq  = file;
    
    l = len(seq);

    newseq = [""]*l; # To store the n-terminal sequence
    #print('Original Sequence');
    #print(seq)
    
    
    for i in range(0,l):
    
        #if(n<len(seq[i])):
        l = len(seq[i]);
        
        if(mode=='NT'):
            n=m;
            if(n!=0):
                newseq[i] = seq[i][0:n];

            elif(n>l):
                print('Warning! Sequence',i,"'s size is less than n. The output table would have NaN for this sequence");


            else:
                print('Value of n is mandatory, it cannot be 0')
                break;

        elif(mode=='CT'):
            n=m;
            if(n!=0):
                newseq[i] = seq[i][(len(seq[i])-n):]
                
            elif(n>l):
                print('WARNING: Sequence',i+1,"'s size is less than the value of n given. The output table would have NaN for this sequence");


            else:
                print('Value of n is mandatory, it cannot be 0')
                break;

        elif(mode=='all'):
            newseq = seq;

        elif(mode=='rest'):
            if(m==0):
                print('Kindly provide start index for rest, it cannot be 0');
                break;

            else:
                if(n<=len(seq[i])):
                    newseq[i] = seq[i][m-1:n+1]
                elif(n>len(seq[i])):
                    newseq[i] = seq[i][m-1:len(seq[i])]
                    print('WARNING: Since input value of n for sequence',i+1,'is greater than length of the protein, entire sequence starting from m has been considered')

        else:
            print("Wrong Mode. Enter 'NT', 'CT','all' or 'rest'");        
        
    #print('NEW SEQUENCE IS',newseq)
    return newseq;


# In[12]:


def binary_profile_nt(file,n,featureNumb):
    
    '''if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    #elif(type(file)==str && len(file))
    else:
    '''
    
    
    
    seq=file;
    seq = split(seq,'NT',n);
    #print(seq)
    l = len(seq);
    #print('length is',l)
    seq=[seq[i].upper() for i in range(l)]
    bin_prof = [];
    for i in range(0,l):
        temp = lookup(seq[i],featureNumb);
        
        [int(i) for i in temp]
        bin_prof.append(temp);
    out = pd.DataFrame(bin_prof);
    
    
    return bin_prof;


def bin_pc_nt(filename,outt,n):
    
    out = [];
    out.append(headerNT);
    seq = [];    
    if(type(filename) == str):
        seq1 = pd.read_csv(filename,header=None, sep=',');
        seq1 = pd.DataFrame(seq1[0].str.upper());
        [seq.append(seq1.iloc[i][0]) for i in range(len(seq1))];
    else:
        seq  = filename;
    out1=[];
    k=0;
    for i in range(len(seq)):
        
        for j in range(25):
            
            binprof=[];
            
            binprof = binary_profile_nt([seq[i]],10,j);
            out1.extend(binprof)
            k=k+1;
        out.append(out1);
        out1=[];
    temp=[];
    final=[];
    
    filen = open(outt,'w')
    sys.stdout=filen
    for ii in range(1,len(out)) :
        for jj in range(1,len(out[ii])) :
            for kk in range(len(out[ii][jj])):
                print('{0:g}'.format(out[ii][jj][kk]),end=',');            
        print("\t");        
    filen.truncate();
    
    return out;
