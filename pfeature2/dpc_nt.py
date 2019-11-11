import pandas as pd
import sys
import os
import numpy as np
import getopt
std = list("ACDEFGHIKLMNPQRSTVWY")
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
def dpc_nt(file,out,n,q):
    filename, file_extension = os.path.splitext(file)
    df = nt(file,n)    	
    f = open(out+"_"+str(q), 'w')
    sys.stdout = f
    #df = pd.read_csv(file, header = None)
    df1 = pd.DataFrame(df[0].str.upper())
    zz = df1.iloc[:,0]
    print("AA,AC,AD,AE,AF,AG,AH,AI,AK,AL,AM,AN,AP,AQ,AR,AS,AT,AV,AW,AY,CA,CC,CD,CE,CF,CG,CH,CI,CK,CL,CM,CN,CP,CQ,CR,CS,CT,CV,CW,CY,DA,DC,DD,DE,DF,DG,DH,DI,DK,DL,DM,DN,DP,DQ,DR,DS,DT,DV,DW,DY,EA,EC,ED,EE,EF,EG,EH,EI,EK,EL,EM,EN,EP,EQ,ER,ES,ET,EV,EW,EY,FA,FC,FD,FE,FF,FG,FH,FI,FK,FL,FM,FN,FP,FQ,FR,FS,FT,FV,FW,FY,GA,GC,GD,GE,GF,GG,GH,GI,GK,GL,GM,GN,GP,GQ,GR,GS,GT,GV,GW,GY,HA,HC,HD,HE,HF,HG,HH,HI,HK,HL,HM,HN,HP,HQ,HR,HS,HT,HV,HW,HY,IA,IC,ID,IE,IF,IG,IH,II,IK,IL,IM,IN,IP,IQ,IR,IS,IT,IV,IW,IY,KA,KC,KD,KE,KF,KG,KH,KI,KK,KL,KM,KN,KP,KQ,KR,KS,KT,KV,KW,KY,LA,LC,LD,LE,LF,LG,LH,LI,LK,LL,LM,LN,LP,LQ,LR,LS,LT,LV,LW,LY,MA,MC,MD,ME,MF,MG,MH,MI,MK,ML,MM,MN,MP,MQ,MR,MS,MT,MV,MW,MY,NA,NC,ND,NE,NF,NG,NH,NI,NK,NL,NM,NN,NP,NQ,NR,NS,NT,NV,NW,NY,PA,PC,PD,PE,PF,PG,PH,PI,PK,PL,PM,PN,PP,PQ,PR,PS,PT,PV,PW,PY,QA,QC,QD,QE,QF,QG,QH,QI,QK,QL,QM,QN,QP,QQ,QR,QS,QT,QV,QW,QY,RA,RC,RD,RE,RF,RG,RH,RI,RK,RL,RM,RN,RP,RQ,RR,RS,RT,RV,RW,RY,SA,SC,SD,SE,SF,SG,SH,SI,SK,SL,SM,SN,SP,SQ,SR,SS,ST,SV,SW,SY,TA,TC,TD,TE,TF,TG,TH,TI,TK,TL,TM,TN,TP,TQ,TR,TS,TT,TV,TW,TY,VA,VC,VD,VE,VF,VG,VH,VI,VK,VL,VM,VN,VP,VQ,VR,VS,VT,VV,VW,VY,WA,WC,WD,WE,WF,WG,WH,WI,WK,WL,WM,WN,WP,WQ,WR,WS,WT,WV,WW,WY,YA,YC,YD,YE,YF,YG,YH,YI,YK,YL,YM,YN,YP,YQ,YR,YS,YT,YV,YW,YY,")
    for i in range(0,len(zz)):
        for j in std:
            for k in std:
                count = 0
                temp = j+k
                for m3 in range(0,len(zz[i])):
                    b = zz[i][m3:m3+q+2:q+1]
                    b.upper()
                    if b == temp:
                        count += 1
                    composition = (count/(len(zz[i])-(q+1)))*100
                print("%.2f" %composition, end = ',')
        print("")
    f.truncate()
