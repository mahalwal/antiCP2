import sys
import os
import pandas as pd
import getopt
def bin_bo_wp(file,outt) :
    filename, file_extension = os.path.splitext(file)
    df=pd.read_csv(file,header=None)
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

    f2 = open(outt, 'w')
    sys.stdout = f2
    for i in range(0,len(xx)) :
        for row in xx[i]:
            print("".join(map(str,row)), end=",")
        print("")
    f2.truncate()  
    os.remove("matrix_can_pat.out")
    os.remove("bin_bond") 	
