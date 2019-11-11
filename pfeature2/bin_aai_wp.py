
# coding: utf-8

# In[64]:


#This code generates binary profile of all or multiple AA Indices 

import sys
import pandas as pd
import numpy as np
import csv
import math
import time
import getopt
import itertools 


# In[65]:


#AAIndex = pd.read_csv('/usr1/webserver/cgidocs/raghava/pfeature/files/z_aaindex.csv',index_col='INDEX');
#AAIndexNames = pd.read_csv('/usr1/webserver/cgidocs/raghava/pfeature/files/AAIndexNames.csv',header=None);

AAIndex = pd.read_csv('z_aaindex.csv',index_col='INDEX');
AAIndexNames = pd.read_csv('AAIndexNames.csv',header=None);

AAindices = 'aaind.txt'


# In[66]:


def searchAAIndex(AAIndex):
    found = -1;
    for i in range(len(AAIndexNames)):
        if(AAIndex == AAIndexNames.iloc[i][0]):
            found = i;
    return found;


# In[67]:


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


# In[72]:


def aaindex123(file,outt,AAI,mode):
    
    if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    else:
        seq = file;
    
    
    if(type(AAI) == str):
        AAI = pd.read_csv(AAI,header=None, sep=',');
        AAI=AAI.T
        AAI[0].values.tolist()
        AAI=AAI[0];
    else:
        AAI = AAI;
    seq=[seq[i].upper() for i in range(len(seq))];
    
    headers = 10*AAI;
    
    final = [];
    semifinal=[];
    final.append(headers);
    
    l1 = len(seq);
    l2 = len(AAI);
    
    for i in range(l1):# handles the sequence
        #inserted = 'Seq_'+str(i+1);
        #final.append([inserted])
        for j in range(len(seq[i])): # handles each amino acid of a sequence
            templist=[];
            #templist.extend([seq[i][j]]);
            for k in range(l2): # handles each AAIndex
                coded = encode(seq[i]);
                 #Add character to the first column
                
                pos = searchAAIndex(AAI[k]);
                
                AAValue = AAIndex.iloc[pos,int(coded[j])];
                
                if(AAValue<=0):
                    templist.extend([0]);
                else:
                    templist.extend([1]);
                
            semifinal.extend(templist);
        final.append(semifinal)
        print('Sequence',i+1,"Processed",l1-i-1,"remaining");
        semifinal=[];
    filenamee = outt
    file = open(filenamee,'w')
    #print('Success! Binary Profiling for all AA Indices completed.')
    with file:
        writer = csv.writer(file);
        writer.writerows(final);
    return final;

    

                
#aaindex_Bin(sys.argv[1],sys.argv[2]);


# In[73]:


def bin_aai_wp(filename,outt):
    
    #print('Beginning AAI Indices\' Binary Profiling, this might take some time');
    #time.sleep(1.5)
    mode = 'all'	
    seq = [];    
    if(type(filename) == str):
        seq1 = pd.read_csv(filename,header=None, sep=',');
        seq1 = pd.DataFrame(seq1[0].str.upper());
        [seq.append(seq1.iloc[i][0]) for i in range(len(seq1))];
    else:
        seq  = filename;
    AAIn = AAindices;
    if(type(AAIn) == str):
        AAI = pd.read_csv(AAIn,header=None, sep=',');
        l2 = AAI.shape[1]
        AAI = AAI.values.tolist()
        AAI  = list(itertools.chain.from_iterable(AAI))
    else:
        AAI = AAIn;
        
    l2 = len(AAI)
    l=len(seq)
    newseq=[];
    #print('m=',m,'n=',n)
    
    for i in range(0,l):
        
            l = len(seq[i]);

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

            
            #else:
                #print("Wrong Mode. Enter 'NT', 'CT','all' or 'rest'");
    if(mode=='split'):
        newseq  = list(itertools.chain.from_iterable(newseq));
    #print(newseq)           

    aaindex123(newseq,outt,AAI,mode);

