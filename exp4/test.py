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
#rgb=np.matrix("'"+str(int(input("Enter R value(1-3): ")))
#                      +","+str(int(input("Enter G value: (1-3)")))+","+str(int(input("Enter B value(1-3): ")))+"'")
rgb=input("Enter Band value(1-3 integer): ")
print("Enter Enhancement Type")
dec=str(input("1.sobel\n2.prewitt\n3.log\n4.canny\n5.roberts\n:"))
thresh=float(input("Enter Threshold value(>0.2): "))
d='horizontal' if (str(input("Enter Direction(1.horizontal    2.vertical): ")))=='1' else 'vertical'

if(dec=='1'):#for sobel
    egtype="sobel"   
elif(dec=='2'):#prewitt
    egtype="prewitt"
elif(dec=='3'):#log
    egtype="log"
elif(dec=='4'):#canny
    egtype="canny"
elif(dec=='5'):#roberts
    egtype="roberts"
else:
    print("invalid input")
    exit()
outpath=""
if(input("chose all file dir \n1.use current dirrector 2.other")==1):
    outpath=os.getcwd()
else:
    outpath=askdirectory()+'/'
#print(fnm+"\n"+str(rgb)+"\n"+str(egtype1)+"\n"+str(egtype2)+"\n"+str(var1)+"\n"+str(var2)+"\n"+str(outpath))

scilab.test(fnm,rgb,egtype,thresh,d,outpath)
