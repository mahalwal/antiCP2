import sys, getopt
#from Bio import SeqIO

def pat_str(inputfile,windowfile,extensionfile,outputfile):
  with open(inputfile,'r') as f:
    g = list(f)
    #temp = f.readlines()

#  print (g)
 
  orig_stdout = sys.stdout
  n = open(outputfile,'w')  
  sys.stdout = n

  

  aa =('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y')
#  print("Program to create motifs by sliding window\n")
#  print("A , C , D , E , F , G , H , I , K , L , M , N , P , Q , R , S , T , V , W , Y\n")

  k= (int(windowfile)-1)/2
  new_str = "X" * int(k)


  for i in g:
#        print("Original sequence: ",i)
#        print (new_str)
#        a = i.readlines()
#        print(a)
#        print (a[0])
#        b = a
        c = i.replace('\n','')
#        c.upper()
        if (extensionfile == 'y'):
#
        	c =new_str+c+new_str
        for j in range(0,len(c)):
            d = c[j:j+int(windowfile)]
            if len(d)==int(windowfile):
#                print("sequence number: ",j+1)
                print(d.upper())
        print("")
