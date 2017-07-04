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
from kivy.uix.checkbox import CheckBox
#scilab.getd
import os
from datetime import datetime
import numpy as np
import pygame
import os
import subprocess
from cmd import Cmd
from threading import Thread
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
    tp1=''
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*11
        fcw.height = fcw.parent.height*11
        mainimg.source='no.gif'

    def showmainimg(self,mainimg,fcw,fchooser,submitbtn,imgname):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            imgname.text = mainimg.source
            submitbtn.disabled = False
        except:
            print fchooser.selection
    def SetMode(self,mode):
        self.tp1=mode
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
    def ButtonImage (self,mainimg,imgtodisp,otherimg1,otherimg2,otherimg3,otherimg4,otherimg5,otherimg6,otherimg7):
        mainimg.source = imgtodisp.source
        imgtodisp.opacity = 0.3
        otherimg1.opacity = 1
        otherimg2.opacity = 1
        otherimg3.opacity = 1
        otherimg4.opacity = 1
        otherimg5.opacity = 1
        otherimg6.opacity = 1
        otherimg7.opacity = 1

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

    def submit(self,s1,s2,s3,s4,s5,mainimg,img1,img2,img3,img4,img5,img6,img7,img8):

        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        var1 = 0
        var2 = 0
        var1 = float(s4.value)
        var2 = float(s5.value)
        try:
            now =datetime.now()
            folder="out_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)
            os.mkdir(folder)
        except Exception as ex:
            print("error"+str(ex))
        outpath = os.getcwd()+"/"+folder+"/"

        try:
            scilab.getd(os.getcwd()+"/")
            scilab.enhancement(self.fnm,rgb,self.tp1,var1,var2,outpath)
            img1.source = './'+folder+'/' +'EnhancedImage.jpg'
            img2.source = './'+folder+'/' +'out_original_img.jpg'
            m=set()
            m.add(s1.value)
            m.add(s2.value)
            m.add(s3.value)
            l=[img3,img4,img5,img6,img7,img8]
            for i in range(0,(len(m)*2),2):
                l[i].source='out_hist_afterenhancement band '+str(int(list(m)[int(math.floor(i/2))]))+'.jpg'
                l[i+1].source='out_hist_band '+str(int(list(m)[int(math.floor(i/2))]))+'.jpg'
                l[i].reload()
                l[i+1].reload()
            img3.source = './'+folder+'/' +'out_hist_afterenhancement band 1.jpg'
            img4.source = './'+folder+'/' +'out_hist_band 1.jpg'
            img5.source = './'+folder+'/' +'out_hist_afterenhancement band 2.jpg'
            img6.source = './'+folder+'/' +'out_hist_band 2.jpg'
            img7.source = './'+folder+'/' +'out_hist_afterenhancement band 3.jpg'
            img8.source = './'+folder+'/' +'out_hist_band 3.jpg'''
            img1.reload()
            img2.reload()
            img3.reload()
            img4.reload()
            img5.reload()
            img6.reload()
            img7.reload()
            img8.reload()
            mainimg.source = img1.source
            mainimg.reload()
            img1.opacity = 0.3

        except Exception as e:
            #d=subprocess.check_output("scialab",shell=True)
            res=Popup(title="Error",content=Label(text="" + str(e)),size_hint=(None, None), size=(600, 400))
            res.open()

    def mainMenu(self):
        App.get_running_app().stop()
        os.chdir("..")
        m.SiplabApp().run()
    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

#SimulatorApp().run()
#Thread(target=app.run).start()
#MyCmd(app).cmdloop()
