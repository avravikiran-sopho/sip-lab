from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from scilab2py import scilab
from kivy.core.window import Window
from kivy.config import Config
scilab.getd
import os
import numpy as np
import pygame
import os
from datetime import datetime
#Window.fullscreen = 'auto'
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class SimulatorApp(App):
    fnm = ''
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*6.5
        fcw.height = fcw.parent.height*6.5
        mainimg.source='no.gif'

    def showmainimg(self,mainimg,fcw,fchooser,submitbtn):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        self.ftype=""
        self.ptype=""
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            submitbtn.disabled = False
        except:
            print fchooser.selection




    def submit(self,s1,s2,s3,mainimg,cutoff,order,img1,img2,img3,img4,img5,img6,img7,img8,img9):


        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        folder=""
        try:
            now =datetime.now()
            folder="out_"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
            os.mkdir(folder)
        except Exception as ex:
            print("error"+str(ex))
        outpath = os.getcwd()+"/"+folder+"/"
        
        dec=True
        try:
            print(self.fnm,rgb,self.ptype,cutoff,order,self.ftype,outpath)
            if(self.ftype==""):
                dec=False
            if(self.ptype==""):
                dec=False
            if(self.fnm==""):
                dec=False
        except:
            print("error in variable")
            dec=False

        if(dec):
        	scilab.fftfilter(self.fnm,rgb,self.ptype,cutoff,order,self.ftype,outpath)
        else:
        	print("fill all fields properly")

        img1.source = outpath+'out_original_img.jpg'
        img2.source = outpath+'Butterworthlowpass filteredimg 1.jpg'
        img3.source = outpath+'Butterworthlowpass filteredimg 2.jpg'
        img4.source = outpath+'Butterworthlowpass filteredimg 3.jpg'
        img5.source = outpath+'Butterworthlowpass filteredimg.jpg'
        img6.source = outpath+'out_mag_spectrum_All.jpg'
        img7.source = outpath+'out_magnitude_spectrum_1.jpg'
        img8.source = outpath+'out_magnitude_spectrum_2.jpg'
        img9.source = outpath+'out_magnitude_spectrum_3.jpg'
        mainimg.source = img1.source
        img1.reload()
        img2.reload()
        img3.reload()
        img4.reload()
        img5.reload()
        img6.reload()
        img7.reload()
        img8.reload()
        img9.reload()
        mainimg.reload()

    def setFilter(self,s):
    	print(s)
    	self.ftype=s
    def setPass(self,s):
    	print(s)
    	self.ptype=s
    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

SimulatorApp().run()
