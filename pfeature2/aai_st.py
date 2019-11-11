import itertools
import sys
import pandas as pd
import numpy as np
import csv
import time
import math
import getopt

# In[198]:


#AAIndex = pd.read_csv('/usr1/webserver/cgidocs/raghava/pfeature/files/aaindex.csv',index_col='INDEX');
#AAIndexNames = pd.read_csv('/usr1/webserver/cgidocs/raghava/pfeature/files/AAIndexNames.csv',header=None);

AAindices = 'aaind.txt'
AAIndex = pd.read_csv('aaindex.csv',index_col='INDEX');

AAIndexNames = pd.read_csv('AAIndexNames.csv',header=None);



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
        else:
            print('Wrong residue!');
    return encoded;
def splittt(seq, parts):

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


def phychem_AAI2(file,AAIn,outt): 
    
    if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
        print('EEEEELELELELEELEELLEE')
    else:
        seq = file;
        
        
    if(type(AAIn) == str):
        AAI = pd.read_csv(AAIn,header=None, sep=',');
        print (AAI.shape)
        
        AAI = AAI.values.tolist()
        
        print(AAI)
    else:
        AAI = AAIn;
    
    l2 = len(AAI)
    #print('lengtg is',l2)
    #print(AAI[0][0])
    #print ('Position found at',pos)
    #header  = AAI[0:l2];
    #print(header);
    final=[];
    header = AAI+AAI+AAI;
    final.append(header);
    semifinal=[]
    #if(pos!=-1):
    l1 = len(seq);
    seq=[seq[i].upper() for i in range(l1)];
    for i in range(l1):

        coded = encode(seq[i]);
        #print(seq[i],"\t",coded)
        temp=[];
        for j in range(l2):
            pos = searchAAIndex(AAI[j]);
            #print(pos)
            sum=0;
            for k in range(len(coded)):
                
                val = AAIndex.iloc[pos,int(coded[k])]
                #print(AAI[j],"\t",val,"\t",coded[k])
                sum=sum+val;
            avg = round(sum/len(seq[i]),3);
            #print("Average for AAIndex",AAI[j],"for",seq[i],"is",avg)
            temp.append(avg);
        semifinal.extend(temp);
        if((i+1)%3==0):
            final.append(semifinal);
            semifinal=[];
            if((i+1)/3==1.0):
                print('Processed',int((i+1)/3),'sequence.',int((l1-(i+1))/3),'remaining');
            else:
                print('Processed',int((i+1)/3),'sequences.',int((l1-(i+1))/3),'remaining');
    #filenamee = "AAindexSplit";  
    file = open(outt,'w')
    #print('Success. AAIndex Profile generated for 3 splits')
    
    #print(final);
    with file:
        writer = csv.writer(file);
        writer.writerows(final);
    return final;


# In[115]:


def aai_stSplit(filename,outt,p):
    
    #print('Beginning AAI Index, this might take some time');
    time.sleep(1.5)
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
    tempseq=[]
    
    for i in range(0,l):
        
            l = len(seq[i]);
            tempseq = splittt(seq[i],p);
            newseq.extend(tempseq);
    #print(newseq)           
    phychem_AAI2(newseq,AAI,outt);
