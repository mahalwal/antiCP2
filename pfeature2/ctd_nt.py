import os
import sys
import pandas as pd
import math
from  more_itertools import unique_everseen
import getopt
def nt(file,n):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][0:n])
        df4 = pd.DataFrame(df3)
        #df4.to_csv(filename+".nt", index = None, header = False, encoding = 'utf-8')
    return df4

def ctd_nt(file,outt,n):
    df = nt(file,n)
    attr=pd.read_csv("aa_attr_group.csv")
    filename, file_extension = os.path.splitext(file)
    #df1 = pd.read_csv(file, header = None)
    #df = pd.DataFrame(df1[0].str.upper())
    n = 0
    stt1 = []
    m = 1
    for i in range(0,len(attr)) :
        st =[]
        stt1.append([])
        for j in range(0,len(df)) :
            stt1[i].append([])
            for k in range(0,len(df[0][j])) :        
                while m < 4 :
                    while n < len(attr.iloc[i,m]) :
                        if df[0][j][k] == attr.iloc[i,m][n] :
                            st.append(m)
                            stt1[i][j].append(m)
                        n += 2
                    n = 0  
                    m += 1
                m = 1 
#####################Composition######################     
    f = open(outt+".ctd_nt_comp", 'w')
    sys.stdout = f
    std = [1,2,3]
    print("1,2,3,")
    for ii in range(0,len(stt1)) :
        for p in range (0,len(df)) :
            #for jj in stt1[ii][p]:
            for pp in std :
                count = 0
                for kk in stt1[ii][p] :
                    temp1 = kk
                    if temp1 == pp :
                        count += 1
                    composition = (count/len(stt1[ii][p]))*100    
                print("%.2f"%composition, end = ",")
            print("")  
    f.truncate() 

#################################Transition#############
    tt = []
    tr=[]
    for ii in range(0,len(stt1)) :
        tt = []
        tr.append([])
        for p in range (0,len(df)) :
            tr[ii].append([])
            while kk < len(stt1[ii][p]) :
                if kk+1 <len(stt1[ii][p]):
                #if  stt1[ii][p][kk] < stt1[ii][p][kk+1] or stt1[ii][p][kk] > stt1[ii][p][kk+1]: # condition for adjacent values
                    tt.append(stt1[ii][p][kk])
                    tt.append(stt1[ii][p][kk+1])
                    tr[ii][p].append(stt1[ii][p][kk])
                    tr[ii][p].append(stt1[ii][p][kk+1])
                    
                kk += 1
            kk = 0    
        
    pp = 0
    xx = []
    xxx = []
    for mm in range(0,len(tr)) :
        xx = []
        xxx.append([])
        for nn in range(0,len(tr[mm])):
            xxx[mm].append([])
            while pp < len(tr[mm][nn]) :
                xx .append(tr[mm][nn][pp:pp+2])
                xxx[mm][nn].append(tr[mm][nn][pp:pp+2])
                pp+=2
            pp = 0
        
    f1 = open(outt+'.ctd_nt_trans', 'w')
    sys.stdout = f1
    std1 = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    print("1->1,1->2,1->3,2->1,2->2,2->3,3->1,3->2,3->3,")
    for qq in range(0,len(xxx)):
        for rr in range(0,len(xxx[qq])) :
            for tt in std1 :
                count = 0
                for ss in xxx[qq][rr] :
                    temp2 = ss
                    if temp2 == tt :
                        count += 1
                print(count, end = ",")  
            print("")
    f1.truncate()       
   
    #################################Distribution#############
    f2 = open(outt+'.ctd_nt_dist', 'w')
    sys.stdout = f2
    c_11 = []
    c_22 = []
    c_33 = []
    zz = []
    print("0% 25% 50% 75% 100%")
    for x in range(0,len(stt1)) :
        #c_11.append([])
        c_22.append([])
        #c_33.append([])
        yy_c_1 = []
        yy_c_2 = []
        yy_c_3 = []
        ccc = []
    
        k = 0
        j = 0
        for y in range(0,len(stt1[x])):
            #c_11[x].append([])
            c_22[x].append([])
            for i in range(1,4) :
                cc = []
                c1 = [index for index,value in enumerate(stt1[x][y]) if value == i]
                c_22[x][y].append(c1)
           
    for x1 in range(0,len(c_22)) :
        cc.append([])
        ccc.append([])
        for y1 in range(0,len(c_22[x1])) :
            cc[x1].append([])
            ccc[x1].append([])
            for z1 in range(0,3) :
                cc[x1][y1].append([])
                ccc[x1][y1].append([])
                for jjj in range(0,101,25) :
                    k = (jjj*(len(c_22[x1][y1][z1])))/100
                    cc[x1][y1][z1].append(math.floor(k))
                    #ccc[x1][y1][z1] = list(unique_everseen(cc[x1][y1][z1]))
                
                print(*cc[x1][y1][z1], end ="\n")    
            print("")
        print("")   

    f2.truncate()
    head = []
    header1 = ['Hydrophobicity','NVWV','Polarity','Polarizability','Charge','SS','SA']
    for i in header1:
        for j in range(1,4):
            head.append(i+'_'+str(j))
    df11 = pd.read_csv(outt+".ctd_nt_comp")
    df_1 = df11.iloc[:,:-1]
    zz = pd.DataFrame()
    for i in range(0,len(df_1),7):
        zz = zz.append(pd.DataFrame(pd.concat([df_1.loc[i],df_1.loc[i+1],df_1.loc[i+2],df_1.loc[i+3],df_1.loc[i+4],df_1.loc[i+5],df_1.loc[i+6]],axis=0)).transpose()).reset_index(drop=True)
    zz.columns = head
    zz.to_csv(outt+".ctd_comp_nt", index=None, encoding='utf-8')
    head2 = []
    header2 = ['1->1','1->2','1->3','2->1','2->2','2->3','3->1','3->2','3->3']
    header1 = ['Hydrophobicity','NVWV','Polarity','Polarizability','Charge','SS','SA']
    for i in header2:
        for j in header1:
            head2.append(i+'_'+str(j))
    df12 = pd.read_csv(outt+".ctd_nt_trans")
    df_2 = df12.iloc[:,:-1]
    ss = pd.DataFrame()
    for i in range(0,len(df_2),7):
        ss = ss.append(pd.DataFrame(pd.concat([df_2.loc[i],df_2.loc[i+1],df_2.loc[i+2],df_2.loc[i+3],df_2.loc[i+4],df_2.loc[i+5],df_2.loc[i+6]],axis=0)).transpose()).reset_index(drop=True)
    ss.columns = head2
    ss.to_csv(outt+".ctd_trans_nt", index=None, encoding='utf-8')
    head3 = []
    header3 = ['0%','25%','50%','75%','100%']
    header4 = ['Hydrophobicity','NVWV','Polarity','Polarizability','Charge','SS','SA']
    for j in range(1,4):
        for k in header4:
            for i in header3:
                head3.append(i+'_'+str(j)+'_'+k)
    df_3 = pd.read_csv(outt+".ctd_nt_dist", sep=" ")
    rr = pd.DataFrame()
    for i in range(0,len(df_3),21):
        rr = rr.append(pd.DataFrame(pd.concat([df_3.loc[i],df_3.loc[i+1],df_3.loc[i+2],df_3.loc[i+3],df_3.loc[i+4],df_3.loc[i+5],df_3.loc[i+6],df_3.loc[i+7],df_3.loc[i+8],df_3.loc[i+9],df_3.loc[i+10],df_3.loc[i+11],df_3.loc[i+12],df_3.loc[i+13],df_3.loc[i+14],df_3.loc[i+15],df_3.loc[i+16],df_3.loc[i+17],df_3.loc[i+18],df_3.loc[i+19],df_3.loc[i+20]],axis=0)).transpose()).reset_index(drop=True)
    rr.columns = head3
    rr.to_csv(outt+".ctd_dist_nt", index=None, encoding='utf-8')
    os.remove(outt+".ctd_nt_comp")	
    os.remove(outt+".ctd_nt_trans")	
    os.remove(outt+".ctd_nt_dist")	
