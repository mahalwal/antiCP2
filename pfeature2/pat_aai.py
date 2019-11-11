
# coding: utf-8

# In[219]:



# coding: utf-8

# In[203]:

#!/usr/bin/env python


import sys
import pandas as pd
import numpy as np
import csv
import itertools
import math
import getopt
# In[198]:

# Generating patterns

def pat_str(file,w):
    if w%2==0:
        raise Exception('window size should be an odd number. The value of window size provided: {}'.format(w))
        sys.exit()
    df1 = pd.read_csv(file, header =None)
    ext = str('X')*int((w-1)/2)
    aa = []
    for i in range(0,len(df1)):
        new_str = ext+df1[0][i]+ext
        aa.append(new_str)
    df2 = pd.DataFrame(aa)
    bb = []
    for j in range(0,len(df2)):
        for k in range(0,len(df2[0][j])):
            cc = df2[0][j][k:k+w]
            if len(cc) == w:
                bb.append(cc)
#         df3 = pd.DataFrame(bb)
    return pd.DataFrame(bb)

AAIndex = pd.read_csv('aaindex_X.csv',index_col='INDEX');
AAIndexNames = pd.read_csv('aaind.txt',header=None);


# In[199]:


'''
argv[1]: File

argv[2]: AAIndex Value

argv[3]: Output

'''

def searchAAIndex(AAIndex):
    found = -1;
    for i in range(len(AAIndexNames)):
        if(str(AAIndex) == AAIndexNames.iloc[i][0]):
            found = i;
    return found;


# In[200]:


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
        elif(peptide[i]=='X'):
            encoded[i] = 20;
        else:
            print('Wrong residue!');
    return encoded;


# In[201]:
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


def phychem_AAI(file,AAIn,outt): 
    if(type(file) == str):
        seq = pd.read_csv(file,header=None);
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    else:
        seq = file;
    
    if(type(AAIn) == str):
        AAI = pd.read_csv(AAIn,header=None, sep=',');
#        print (AAI.shape)
        #AAI=seq.T;
        l2 = AAI.shape[1]
        AAI.values.tolist()
        
#        print(AAI)
    else:
        AAI = AAIn;
    l2 = AAI.shape[1]
    
#    print('lengtg is',l2)
    #print(AAI[0][0],AAI[1][0])
    #print ('Position found at',pos)
    #print(AAI[0:l2]);
    header =['Sequence'];
    header.extend(i for i in AAIn.loc[0])
    #print(header);
    final=[];
    final.append(header);
    #if(pos!=-1):
    l1 = len(seq);
    seq=[seq[0][i].upper() for i in range(l1)];
    for i in range(l1):

        coded = encode(seq[i]);
        temp=[];
        for j in range(l2):
            pos = searchAAIndex(AAI[j][0]);
            #print(pos)
            if(j==0):
                temp.append(seq[i]);
            sum=0;
            for k in range(len(coded)):
                val = AAIndex.iloc[pos,int(coded[k])]
                sum=sum+val;
            avg = round(sum/len(coded),3);    
            temp.append(avg);
        final.append(temp);
        
        
    file = open(outt,'w')
    with file:
        writer = csv.writer(file);
        writer.writerows(final);
    return final;
#phychem_AAI(sys.argv[1],sys.argv[2]);



def pat_aai(file,AAIn,w,outt):
    file = pat_str(file,w)
    mode = 'all'
    m = 0
    n = 0
    if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    else:
        seq = file;
        
    if(type(AAIn) == str):
        AAI = pd.read_csv(AAIn,header=None, sep=',');
        #print (AAI.shape)
        #AAI=seq.T;
        l2 = AAI.shape[1]
        AAI.values.tolist()
        
        #print(AAI)
    else:
        AAI = AAIn;
    l2 = AAI.shape[1]
    l=len(seq)
    #print(l)
    newseq=[];
    #print('m=',m,'n=',n)
    for i in range(0,l):

            #if(n<len(seq[i])):
            l = len(seq[0][i]);

            if(mode=='NT'):
                n=m;
                #print('Inside NT, m=',m,'n=',n)
                if(n!=0):
                    new = seq[i][0:n];
                    newseq.append(new);

                elif(n>l):
                    print('Warning! Sequence',i,"'s size is less than n. The output table would have NaN for this sequence");


                else:
                    print('Value of n is mandatory, it cannot be 0')
                    break;

            elif(mode=='CT'):
                n=m;
                if(n!=0):
                    new = seq[i][(len(seq[i])-n):]
                    newseq.append(new);
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
                    #if(n<=len(seq[i])):
                    new = seq[i][m:len(seq[i])-n]
                    newseq.append(new)
                    '''elif(n>len(seq[i])):
                        newseq[i] = seq[i][m-1:len(seq[i])]
                        print('WARNING: Since input value of n for sequence',i+1,'is greater than length of the protein, entire sequence starting from m has been considered')'''

            elif(mode=='split'):
                n=m;
                new = split(seq[i],m);
                newseq.append(new);
                #
            
            else:
                print("Wrong Mode. Enter 'NT', 'CT','all' or 'rest'");
    if(mode=='split'):
        newseq  = list(itertools.chain.from_iterable(newseq));
    #print(newseq)           
    phychem_AAI(newseq,AAI,outt);
