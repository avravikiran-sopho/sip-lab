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
#print("Enter Enhancement Type")
#dec=str(input("1.Linear\n2.Standard Deviation\n3.Histogram\n4.Logarithmic\n5.Exponential\n5.Decorrelation \n:"))

fil='Butterworth' if (str(input("Choose Filter(1.Butterworth    2.Gaussian(default)): ")))=='1' else 'Gaussian'
pss='highpass' if (str(input("Enter Direction(1.highpass    2.lowpass(Defult)): ")))=='1' else 'lowpass'
cutoff=float(input("Enter cutoff value(>.1):"))
order=int(input("Enter Order Number: "))

outpath=""
if(input("chose all file dir \n1.use current dirrector 2.other")==1):
    outpath=os.getcwd()
else:
    outpath=askdirectory()+'/'


scilab.fftfilter(fnm,rgb,pss,cutoff,order,fil,outpath)
