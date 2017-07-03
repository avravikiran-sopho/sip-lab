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
#scilab.getd
import os
import numpy as np
import pygame
import os
from datetime import datetime
#Window.fullscreen = 'auto'
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class betaApp(App):
    fnm = ''

    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*6.5
        fcw.height = fcw.parent.height*6.5
        mainimg.source='no.gif'

    def showmainimg(self,mainimg,fcw,fchooser,bandvalue,submitbtn,imgname):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            imgname.text = mainimg.source
            #band_slider.max = 1
            #band_slider.min = 3s
            submitbtn.disabled = False

        except:
            print fchooser.selection



    def setType(self,eg):
        self.egtype=eg
    def setDir(self,d):
        self.direction=d
    def Set_Slider (self,slider,tlabel):
        if (int(tlabel.text)>slider.max):
            slider.value = slider.max
            tlabel.text = slider.max
        elif (int(tlabel.text)<slider.min):
            slider.value = slider.min
            tlabel.text = slider.min
        else:
            slider.value = int(tlabel.text)

    def submit(self,bval,slider,mainimg,img1,img2,img3,imgname):


        #rgb = np.matrix("'"+str(bval.value)+","+str(bval.value)+","+str(bval.value)+"'")
        #subrow = np.matrix("'"+str(s4.value)+","+str(s5.value)+"'")
        #subcol = np.matrix("'"+str(s6.value)+","+str(s7.value)+"'")
        folder=""
        try:
            now =datetime.now()
            folder="out_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)
            os.mkdir(folder)
        except Exception as ex:
            print("error"+str(ex))
        outpath = os.getcwd()+"/"+folder+"/"

        dec=True
        try:
            print(self.fnm,bval.value,self.egtype,slider.value,self.direction,outpath)
            if(self.egtype==""):
                dec=False
                Popup(title="Error",content=Label(text="Please select edge type"),size_hint=(None, None), size=(600, 200)).open()
            if(self.direction==""):
                Popup(title="Error",content=Label(text="Please select edge type"),size_hint=(None, None), size=(600, 200)).open()
                dec=False
            if(self.fnm==""):
                Popup(title="Error",content=Label(text="Please select edge type"),size_hint=(None, None), size=(600, 200)).open()
                dec=False
        except:

            dec=False
        if(dec):
	    scilab.getd(os.getcwd()+"/")
            scilab.test(self.fnm,bval.value,self.egtype,slider.value,self.direction,outpath)
            img1.source = self.fnm
            img2.source = outpath+'out_original_img.jpg'
            img3.source = outpath+'edgeimg.jpg'
            mainimg.source = img1.source
            img1.reload()
            img2.reload()
            img3.reload()
            mainimg.reload()
            img1.opacity = 1
            imgname.text = mainimg.source
        else:
            Popup(title="Error",content=Label(text="Please fill all fields properly"),size_hint=(None, None), size=(400, 200)).open()
    def ButtonImage (self,mainimg,imgtodisp,otherimg1,otherimg2):
        mainimg.source = imgtodisp.source
        imgtodisp.opacity = 1
        otherimg1.opacity = 0.3
        otherimg2.opacity = 0.3

    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

#betaApp().run()
