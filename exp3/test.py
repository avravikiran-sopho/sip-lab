import os
from scilab2py import scilab
import numpy as np
from Tkinter import Tk
from tkFileDialog import askopenfilename,askdirectory
Tk().withdraw()
if(input("chose all file dir \n1.use current dirrector 2.other:")==1):
    scilab.getd(str(os.getcwd()))
else:
    scilab.getd(str(askdirectory()))
#out=scilab.test(5,6)
#print("this is in test "+ str(out))
#exec('~/usr/share/scilab/contrib/sivp/loader.sce')
#fnm=str(askopenfilename(filetypes = [("Image Files", ("*.jpg", "*.gif")),("JPEG",'*.jpg'),("GIF",'*.gif')]))
fnm=str(askopenfilename())
rgb=np.matrix("'"+str(int(input("Enter R value(1-3): ")))
                      +","+str(int(input("Enter G value: (1-3)")))+","+str(int(input("Enter B value(1-3): ")))+"'")
tp1=""
tp11=0
tp12=0
var1=0
var2=0
ws1=0
ws2=0
sigma=0.0
print("Enter Enhancement Type")
dec=str(input("1.Average\n2.Circular\n3.Gaussian\n4.Median\n5.Weighted Average\n:"))
ws1=input("Enter Window1 size(3 or 5 or 7): ")
ws2=input("Enter Window2 size(3 or 5 or 7): ")
if(dec=='1'):#for Average
    tp1="Average"
    tp11=65
elif(dec=='2'):#Circular
    tp11=67
    tp1="Circular"
elif(dec=='3'):#Gaussian
    sigma=float(input("Enter Sigma value in decimal(0.5-3.0):"))
    tp11=71
    tp1="Gaussian"
elif(dec=='4'):#Median
    tp11=77
    tp12=101
    tp1="Median"
elif(dec=='5'):#Weighted Average
    tp11=87
    tp1="Weighted"
else:
    print("invalid input")
outpath=""
if(input("chose all file dir \n1.use current dirrector 2.other")==1):
    outpath=os.getcwd()
else:
    outpath=askdirectory()+'/'
#print(fnm+"\n"+str(rgb)+"\n"+str(tp11)+"\n"+str(tp12)+"\n"+str(var1)+"\n"+str(var2)+"\n"+str(outpath))

scilab.filternew(fnm,rgb,tp1,tp11,tp12,ws1,ws2,sigma,outpath)
