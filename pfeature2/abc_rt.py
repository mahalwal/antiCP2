import os
import sys
import pandas as pd 
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

def bond(file,n,c) :
    df = rest(file,n,c)
    tota = []
    hy = []
    Si = []
    Du = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    bb = pd.DataFrame()
    filename, file_extension = os.path.splitext(file)
    #df12 = pd.read_csv(file, header = None)
    #df = pd.DataFrame(df12[0].str.upper())
    bonds=pd.read_csv("bonds.csv")
    for i in range(0,len(df)) :
        tot = 0
        h = 0
        S = 0
        D = 0
        tota.append([i])
        hy.append([i])
        Si.append([i])
        Du.append([i])
        for j in range(0,len(df[0][i])) :
            temp = df[0][i][j]
            for k in range(0,len(bonds)) :
                if bonds.iloc[:,0][k] == temp :
                    tot = tot + bonds.iloc[:,1][k]
                    h = h + bonds.iloc[:,2][k]
                    S = S + bonds.iloc[:,3][k]
                    D = D + bonds.iloc[:,3][k]
        tota[i].append(tot)
        hy[i].append(h)
        Si[i].append(S)
        Du[i].append(D)
    for m in range(0,len(df)) :
        b1.append(tota[m][1])
        b2.append(hy[m][1])
        b3.append(Si[m][1])
        b4.append(Du[m][1])
    
    bb["total_bonds"] = b1 
    bb["hydrogen_bonds"] = b2
    bb["single_bond"] = b3
    bb["double_bond"] = b4 
    
    #bb.to_csv(filename+".bonds_info")
    return bb

###########################atom###############
def atc(file,n,c) :
    test1 = rest(file,n,c)
    atom=pd.read_csv("atom.csv",header=None)
    filename, file_extension = os.path.splitext(file)
    at=pd.DataFrame()
    i = 0
    C_atom = []
    H_atom = []
    N_atom = []    
    O_atom = []
    S_atom = []
 
    while i < len(atom):
        C_atom.append(atom.iloc[i,1].count("C"))
        H_atom.append(atom.iloc[i,1].count("H"))
        N_atom.append(atom.iloc[i,1].count("N"))
        O_atom.append(atom.iloc[i,1].count("O"))
        S_atom.append(atom.iloc[i,1].count("S"))
        i += 1
    atom["C_atom"]=C_atom  
    atom["O_atom"]=O_atom  
    atom["H_atom"]=H_atom  
    atom["N_atom"]=N_atom 
    atom["S_atom"]=S_atom 
##############read file ##########	
    #df12 = pd.read_csv(file, header = None)
    #test1 = pd.DataFrame(df12[0].str.upper())
    #test1 = pd.read_csv(file,header=None)
    dd = []
    for i in range(0, len(test1)):
        dd.append(test1[0][i].upper())
    test = pd.DataFrame(dd)
    count_C = 0
    count_H = 0
    count_N = 0
    count_O = 0
    count_S = 0
    count = 0
    i1 = 0
    j = 0
    k = 0
    C_ct = []
    H_ct = []
    N_ct = []
    O_ct = []
    S_ct = []
    while i1 < len(test) :
        while j < len(test[0][i1]) :
            while k < len(atom) :
                if test.iloc[i1,0][j]==atom.iloc[k,0].replace(" ","") :
                    count_C = count_C + atom.iloc[k,2]
                    count_H = count_H + atom.iloc[k,3]
                    count_N = count_N + atom.iloc[k,4]
                    count_O = count_O + atom.iloc[k,5]
                    count_S = count_S + atom.iloc[k,6]
                #count = count_C + count_H + count_S + count_N + count_O
                k += 1
            k = 0
            j += 1
        C_ct.append(count_C)
        H_ct.append(count_H)
        N_ct.append(count_N)
        O_ct.append(count_O)
        S_ct.append(count_S)
        count_C = 0
        count_H = 0
        count_N = 0
        count_O = 0
        count_S = 0
        j = 0
        i1 += 1
    test["C_count"]=C_ct  
    test["H_count"]=H_ct  
    test["N_count"]=N_ct 
    test["O_count"]=O_ct  
    test["S_count"]=S_ct     

    ct_total = []
    m = 0
    while m < len(test) :
        ct_total.append(test.iloc[m,1] + test.iloc[m,2] + test.iloc[m,3] + test.iloc[m,4] + test.iloc[m,5])
        m += 1
    test["count"]=ct_total    
##########final output#####
    final = pd.DataFrame()
    n = 0
    p = 0
    C_p = []
    H_p = []
    N_p = []
    O_p = []
    S_p = []
    while n < len(test):
        C_p.append((test.iloc[n,1]/test.iloc[n,6])*100)
        H_p.append((test.iloc[n,2]/test.iloc[n,6])*100)
        N_p.append((test.iloc[n,3]/test.iloc[n,6])*100)
        O_p.append((test.iloc[n,4]/test.iloc[n,6])*100)
        S_p.append((test.iloc[n,5]/test.iloc[n,6])*100)
        n += 1
    final["C_perc"] = C_p
    final["H_perc"] = H_p
    final["N_perc"] = N_p
    final["O_perc"] = O_p
    final["S_perc"] = S_p

    #(final.round(2)).to_csv(filename+".atc")
    return final.round(2)

########################################atom_bond#################
def abc_rt(file,out,n,c) :
    filename, file_extension = os.path.splitext(file)
    file_atc=atc(file,n,c)
    file_bonds=bond(file,n,c)
    df1=file_atc.iloc[:,1:6]
    df2=file_bonds.iloc[:,0:5]
    df3 = pd.concat([df1,df2],axis=1)
    df3.to_csv(out, index=None)
