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
import math

import sys
import os.path
p=os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(p)
import main as m
sys.path.remove(p)

#Window.fullscreen = 'auto'
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class SimulatorApp(App):
    fnm = ''
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*9.5
        fcw.height = fcw.parent.height*9.5
        mainimg.source='no.gif'

    def focus (self,slider,textinput):
        try:
            if (int(textinput.text)>slider.max):
                slider.value = slider.max
                textinput.text = slider.max
            elif (int(textinput.text)<slider.min):
                slider.value = slider.min
                textinput.text = slider.min
            else:
                slider.value = int(textinput.text)
        except:
            print ""
    def ButtonImage (self,mainimg,imgtodisp,otherimg1,otherimg2,otherimg3,otherimg4,otherimg5,otherimg6,otherimg7,otherimg8):
        mainimg.source = imgtodisp.source
        imgtodisp.opacity = 0.3
        otherimg1.opacity = 1
        otherimg2.opacity = 1
        otherimg3.opacity = 1
        otherimg4.opacity = 1
        otherimg5.opacity = 1
        otherimg6.opacity = 1
        otherimg7.opacity = 1
        otherimg8.opacity = 1

    def showmainimg(self,mainimg,fcw,fchooser,submitbtn,imgname):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        self.ftype=""
        self.ptype=""
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            submitbtn.disabled = False
            imgname.text = mainimg.source
        except:
            print fchooser.selection




    def submit(self,s1,s2,s3,mainimg,cutoff,order,img1,img2,img3,img4,img5,img6,img7,img8,img9,imgname):
        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        folder=""

        try:
            if(self.ftype==""):
                dec=False
            if(self.ptype==""):
                dec=False
            if(self.fnm==""):
                dec=False
        except:
            dec=False

        def exe():
            try:
                if(dec):
                    scilab.getd(os.getcwd()+"/")
                    scilab.fftfilter(self.fnm,rgb,self.ptype,cutoff,order,self.ftype,outpath)
                    load()
                else:
                    Popup(title="Error",content=Label(text="fill all fields properly") ,size_hint=(None, None), size=(600, 400)).open()
            except Exception as e:
                res=Popup(title="Error",content=Label(text="" + str(e)),size_hint=(None, None), size=(600, 400))
                res.open()

        #create folder in format "out_day_month_year_hour_minute_second" to store output files
        try:
            now =datetime.now()
            folder="out_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)
            os.mkdir(folder)
        except Exception as ex:
            print("error"+str(ex))
        outpath = os.getcwd()+"/"+folder+"/"

        #show loadind gif when experiment is running
        outpath = os.getcwd()+"/"+folder+"/"
        mainimg.source = 'Loading.gif'
        mainimg.reload()
        thread = threading.Thread(target=exe,args=())
        thread.start()

        @mainthread
        def load():
            img1.source = outpath+'out_original_img.jpg'
            img2.source = outpath+self.ftype+self.ptype+' filteredimg.jpg'
            img3.source = outpath+'out_mag_spectrum_All.jpg'
            mainimg.source = img1.source
            img1.opacity = 0.3
            imgname.text = img1.source
            img1.reload()
            img2.reload()
            img3.reload()
            mainimg.reload()

    def mainMenu(self):
        App.get_running_app().stop()
        os.chdir("..")
        m.SiplabApp().run()
    def EnableBand(self,bandvalue):
        if (self.fnm.find(".")==-1):
            print "band"
            bandvalue.disabled = False

    def SetMaxRGB(self,bandvalue,s1,s2,s3,rvalue,gvalue,bvalue):
        try:
            s1.max = int(bandvalue.text)
            s2.max = int(bandvalue.text)
            s3.max = int(bandvalue.text)
            s1.value = s1.min
            s2.value = s2.min
            s3.value = s3.min
            rvalue.hint_text = "1 - " + bandvalue.text
            gvalue.hint_text = "1 - " + bandvalue.text
            bvalue.hint_text = "1 - " + bandvalue.text
        except:
            print ""

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

#SimulatorApp().run()
