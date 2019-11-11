import os
import sys
import pandas as pd
import math
import getopt
from itertools import repeat
from  more_itertools import unique_everseen
from pandas.io.common import EmptyDataError
def split(file,v):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    k1 = []
    for w in range(0,len(df2)):
        s = 0
        k2 = []
        r = 0
        if len(df2[0][w])%v == 0:
            k2.extend(repeat(int(len(df2[0][w])/v),v))
        else:
            r = int(len(df2[0][w])%v)
            k2.extend(repeat(int(len(df2[0][w])/v),v-1))
            k2.append((int(len(df2[0][w])/v))+r)
        for j in k2:
            df3 = df2[0][w][s:j+s] 
            k1.append(df3)
            s = j+s
    df4 = pd.DataFrame(k1)
    #df4.to_csv(filename+".split", index = None, header = False, encoding = 'utf-8')
    return df4
    
def ctd_st(file,output,v):
    file1 = split(file,v)
    attr=pd.read_csv("aa_attr_group.csv", sep = "\t")
    filename, file_extension = os.path.splitext(file)
    #df1 = pd.read_csv(file, header = None)
    #df = pd.DataFrame(df1[0].str.upper())
    df = file1  
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
    f = open(filename+".comp_ctd_split", 'w')
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

    f1 = open(filename+'.trans_ctd_split', 'w')
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
    f2 = open(filename+'.dist_ctd_split', 'w')
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
    head1 = []
    header1 = ['Hydrophobicity','NVWV','Polarity','Polarizability','Charge','SS','SA']
    for i in range(1,v+1):
        for j in header1:
            for k in range(1,4):
                head1.append("gp"+str(k)+"_"+j+"_s"+str(i))
    df11 = pd.read_csv(filename+".comp_ctd_split")
    df_1 = df11.iloc[:,:-1]
    bb = []
    for i in range(0,len(df_1),v*7):
        aa = []
        for j in range(v*7):
            aa.extend(df_1.loc[i+j])
        bb.append(aa)
    zz = pd.DataFrame(bb)
    zz.columns = head1
    zz.to_csv(output+".ctd_comp_st", index = None)
    head2 = []
    header1 = ['Hydrophobicity','NVWV','Polarity','Polarizability','Charge','SS','SA']
    header2 = ['1->1','1->2','1->3','2->1','2->2','2->3','3->1','3->2','3->3']
    for k in range(1,v+1):    
        for i in header1:
            for j in header2:
                head2.append(j+'_'+i+"_s"+str(k))
    df12 = pd.read_csv(filename+".trans_ctd_split")
    df_2 = df12.iloc[:,:-1]
    qq = []
    for i in range(0,len(df_2),v*7):
        ww = []
        for j in range(v*7):
            ww.extend(df_2.loc[i+j])
        qq.append(ww)
    ss = pd.DataFrame(qq)
    ss.columns = head2
    ss.to_csv(output+".ctd_trans_st", index = None)
    head3 = []
    header3 = ['0%','25%','50%','75%','100%']
    header1 = ['Hydrophobicity','NVWV','Polarity','Polarizability','Charge','SS','SA']
    for l in range(1,v+1):
        for k in header1:
            for i in range(1,4):
                for j in header3:
                    head3.append("gp_"+str(i)+"_"+j+"_"+k+"_s"+str(l))
    df_3 = pd.read_csv(filename+".dist_ctd_split", sep = " ")
    tt = []
    for i in range(0,len(df_3),v*21):
        yy = []
        for j in range(v*21):
            yy.extend(df_3.loc[i+j])
        tt.append(yy)
    rr = pd.DataFrame(tt)
    rr.columns = head3
    rr.to_csv(output+".ctd_dist_st", index = None)
    os.remove(filename+".comp_ctd_split")
    os.remove(filename+".trans_ctd_split")
    os.remove(filename+".dist_ctd_split")
