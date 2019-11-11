import os
import sys
import getopt
import pandas as pd 
import getopt
def atc_nt(file,outt,N):
    import pandas as pd
    atom=pd.read_csv("atom.csv",header=None)
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
    atom["H_atom"]=H_atom  
    atom["N_atom"]=N_atom 
    atom["O_atom"]=O_atom  
    atom["S_atom"]=S_atom 

##############read file ##########	    
    data = pd.read_csv(file,header=None)
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
    k1 = []
    for q in range(0,len(data)):
        kk = data[0][q][0:N].upper()
        k1.append(kk)
    test = pd.DataFrame(k1) 
    
    while i1 < len(test) :
        while j < len(test[0][i1]) :
            while k < len(atom) :
                if test.iloc[i1,0][j]==atom.iloc[k,0].replace(" ","") :
                    count_C = count_C + atom.iloc[k,2]
                    count_H = count_H + atom.iloc[k,3]
                    count_N = count_N + atom.iloc[k,4]
                    count_O = count_O + atom.iloc[k,5]
                    count_S = count_S + atom.iloc[k,6]
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

    (final.round(2)).to_csv(outt,index=None)
