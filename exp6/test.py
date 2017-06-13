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
                      +","+str(int(input("Enter G value(1-3): ")))+","+str(int(input("Enter B value(1-3): ")))+"'")

outpath=""
if(input("chose all file dir \n1.use current dirrector 2.other")==1):
    outpath=os.getcwd()
else:
    outpath=askdirectory()+'/'


scilab.colourtransform(fnm,rgb,outpath)
