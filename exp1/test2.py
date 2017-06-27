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

import os
import numpy as np
import pygame
import os

#Window.fullscreen = 'auto'
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class SimulatorApp(App):
    fnm = ''
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*6.5
        fcw.height = fcw.parent.height*6.5
        mainimg.source='no.gif'

    def showmainimg(self,mainimg,fcw,fchooser,s4,s5,s6,s7,submitbtn):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            img = pygame.image.load(self.fnm)
            wid=img.get_width()
            hei=img.get_height()
            print wid,hei
            s4.max = hei-100
            s4.min = 1
            s5.max = hei
            s6.max = wid-100
            s6.min = 1
            s7.max = wid
            submitbtn.disabled = False
            s4.disabled = False
            s5.disabled = False
            s6.disabled = False
            s7.disabled = False
        except:
            print fchooser.selection




    def submit(self,s1,s2,s3,s4,s5,s6,s7,mainimg,img1,img2,img3,img4,img5):


        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        subrow = np.matrix("'"+str(s4.value)+","+str(s5.value)+"'")
        subcol = np.matrix("'"+str(s6.value)+","+str(s7.value)+"'")
        outpath = os.getcwd()+"/"
        print rgb,subrow,subcol
        scilab.getd(outpath)
        scilab.imgdisplay(self.fnm,rgb,subrow,subcol,'win4pix.txt',outpath)

        img1.source = 'out_subset_img.jpg'
        img2.source = 'out_original_img.jpg'
        img3.source = 'out_hist_band 1.jpg'
        img4.source = 'out_hist_band 2.jpg'
        img5.source = 'out_hist_band 3.jpg'
        mainimg.source = img2.source
        img1.reload()
        img2.reload()
        img3.reload()
        img4.reload()
        img5.reload()
        mainimg.reload()

    def ChangeVal(self,sl1,sl2):
    	sl2.min=int(sl1.value)+100

    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

#cSimulatorApp().run()
