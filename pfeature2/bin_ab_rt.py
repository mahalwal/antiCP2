import os
from itertools import repeat
import pandas as pd
import sys
import getopt
def rest(file,n,c):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][n:-c])
        df4 = pd.DataFrame(df3)
        #df4.to_csv(filename+".rest", index = None, header = False, encoding = 'utf-8') 
    return df4
		
def atom_bin_rest(file,outt,n,c) :
    file1 = rest(file,n,c)
    filename, file_extension = os.path.splitext(file)
    df=file1
    ############binary matrix for atoms
    f = open('matrix_atom.out', 'w')
    sys.stdout = f
    print("C,H,N,O,S,")
    x = []
    for i in range(0,5) :
        x.append([])
        for j in range(0,5) :
            if i == j :
                x[i].append(1)
            else :
                x[i].append(0)
            
            print(x[i][j], end=",") 
        print("") 
    f.close() 
##############associate binary values to atoms    
    mat = pd.read_csv("matrix_atom.out")
    mat1 = mat.iloc[:,:-1]
    mat2 = mat1.transpose()
    #df1 = pd.read_csv("atom.csv",header=None)
    zz = []
    kk = pd.DataFrame()
    df1 = pd.read_csv("atom.csv",header=None)
    for i in range(0,len(df1)) :
        zz.append([])
        for j in range(0,len(df1[1][i])) :
            temp = df1[1][i][j]
            zz[i].append(mat2.loc[temp])
            
    f1 = open('bin_atom', 'w')
    sys.stdout = f1
    for i in range(0,len(zz)) :
        for row in zz[i]:
            print(",".join(map(str,row)), end=",")
        print("")
    
    f1.close()    
    
    with open('bin_atom', 'r') as f:
        g = list(f)
        
    for i in range(0,len(g)) :
        g[i] = g[i].replace(",\n","")    
        
    df1["bin"]=g
    
    #########binary atom values for given file
    xx=[]
    jj = 0
    for i in range(0,len(df)) :
        xx.append([])
        while jj < len(df[0][i]) :
            temp=df[0][i][jj]
            for k in range(0,len(df1)) :
                if temp == df1[0][k][0] :
                    xx[i].append(df1.iloc[k,2])
            jj += 1
        jj = 0 
        
        
    f2 = open(outt+"_atom", 'w')
    sys.stdout = f2
    for i in range(0,len(xx)) :
        for row in xx[i]:
            print("".join(map(str,row)), end=",")
        print("")
    f2.close() 
	
    os.remove("matrix_atom.out")
    os.remove("bin_atom") 
	
def bond_bin_rest(file,outt,n,c) :
    df = rest(file,n,c)
    filename, file_extension = os.path.splitext(file)
    #df=pd.read_csv(file,header=None)
    ############binary matrix for atoms
    f = open('matrix_can_pat.out', 'w')
    sys.stdout = f
    print("-,=,c,b,")
    x = []
    for i in range(0,4) :
        x.append([])
        for j in range(0,4) :
            if i == j :
                x[i].append(1)
            else :
                x[i].append(0)
            
            print(x[i][j], end=",") 
        print("") 
    f.close() 

##############associate binary values to bonds   
    mat = pd.read_csv("matrix_can_pat.out")
    mat1 = mat.iloc[:,:-1]
    mat2 = mat1.transpose()
    df1 = pd.read_csv("can_pat.csv")
    zz = []
    kk = pd.DataFrame()
    
    for i in range(0,len(df1)) :
        zz.append([])
        for j in range(0,len(df1.iloc[:,1][i])) :
            temp = str(df1.iloc[:,1][i][j])
            zz[i].append(mat2.loc[temp])

    f1 = open('bin_bond', 'w')
    sys.stdout = f1
    for i in range(0,len(zz)) :
        for row in zz[i]:
            print(",".join(map(str,row)), end=",")
        print("")
    
    f1.close() 

    with open('bin_bond', 'r') as f:
        g = list(f)
        
    for i in range(0,len(g)) :
        g[i] = g[i].replace(",\n","")
        
    df1["bin"] = g    

    xx=[]
    jj = 0
    for i in range(0,len(df)) :
        xx.append([])
        while jj < len(df[0][i]) :
            temp=df[0][i][jj]
            for k in range(0,len(df1)) :
                if temp == df1.iloc[k,0][0] :
                    xx[i].append(df1.iloc[k,2])
            jj += 1
        jj = 0 

    f2 = open(outt+"_bond", 'w')
    sys.stdout = f2
    for i in range(0,len(xx)) :
        for row in xx[i]:
            print("".join(map(str,row)), end=",")
        print("")
    f2.close()  
	
    os.remove("matrix_can_pat.out")
    os.remove("bin_bond")	
	
def bin_ab_rt(file,outt,n,c):
    atom_bin_rest(sys.argv[2],sys.argv[4],n,c)
    bond_bin_rest(sys.argv[2],sys.argv[4],n,c)	
    with open(outt+"_atom",'r') as f1:
        g1 = list(f1)
    with open(outt+"_bond",'r') as f2:
        g2 = list(f2)		
		
    i = 0
    j = 0
    h = 0	
    while i < len(g1) :
        g1[i] = g1[i].replace("\n","")
        i += 1
    
    while j < len(g2) :
        g2[j] = g2[j].replace("\n","")
        j += 1 
    
	
    orig_stdout = sys.stdout
    n12 = open(outt,'w')	
    sys.stdout = n12
   
   #g1[2] = g1[2].split(",")
   #g2[2] = g2[2].split(",")
 
    while h < len(g2) : 
        print ("{0}".format(g1[h]+g2[h]))
        h += 1	
    n12.truncate()		
    os.remove(outt+"_atom")
    os.remove(outt+"_bond")	 	
