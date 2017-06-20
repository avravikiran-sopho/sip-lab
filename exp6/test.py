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
import math
#Window.fullscreen = 'auto'
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class BetaApp(App):
    fnm = ''
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*6.5
        fcw.height = fcw.parent.height*6.5
        mainimg.source='no.gif'

    def showmainimg(self,mainimg,fcw,fchooser,submitbtn):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            submitbtn.disabled = False
        except:
            print fchooser.selection




    def submit(self,s1,s2,s3,mainimg,img1,img2,img3,img4):


        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")

        folder=""
        try:
            now =datetime.now()
            folder="out_"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
            os.mkdir(folder)
        except Exception as ex:
            print("error"+str(ex))
        outpath = os.getcwd()+"/"+folder+"/"

        scilab.colourtransform(self.fnm,rgb,outpath)

        img1.source = outpath+'out_original_img.jpg'
        m=set()
        m.add(s1.value)
        m.add(s2.value)
        m.add(s3.value)
        l=[img2,img3,img4]
        for i in range(len(m)):
            l[i].source='out_hist_band '+str(int(list(m)[i]))+'.jpg'
            l[i].reload()
        mainimg.source = img1.source
        mainimg.reload()

    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

BetaApp().run()