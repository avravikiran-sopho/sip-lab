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
scilab.getd
import os
import numpy as np
import pygame
import os
import subprocess
from cmd import Cmd
from threading import Thread

#Window.fullscreen = 'auto'
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class SimulatorApp(App):
    fnm = ''
    tp1=''
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*9.5
        fcw.height = fcw.parent.height*9.5
        mainimg.source='no.gif'

    def showmainimg(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
        except:
            print fchooser.selection
    def SetMode(self,mode):
        self.tp1=mode
    def submit(self,s1,s2,s3,s4,s5,mainimg,img1,img2,img3,img4,img5,img6,img7,img8):
        array = [s1,s2,s3]
        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        var1 = 0
        var2 = 0
        var1 = float(s4.value)
        var2 = float(s5.value)
        path = os.getcwd()+"/"
        try:
            scilab.enhancement(self.fnm,rgb,self.tp1,var1,var2,path)
        except Exception as e:
            #d=subprocess.check_output("scialab",shell=True)
            res=Popup(title="Error",content=Label(text="" + str(e)),size_hint=(None, None), size=(600, 400))
            res.open()

        img1.source = 'EnhancedImage.jpg'
        img2.source = 'out_original_img.jpg'
        img3.source = 'out_hist_afterenhancement band 1.jpg'
        img4.source = 'out_hist_band 1.jpg'
        img5.source = 'out_hist_afterenhancement band 2.jpg'
        img6.source = 'out_hist_band 2.jpg'
        img7.source = 'out_hist_afterenhancement band 3.jpg'
        img8.source = 'out_hist_band 3.jpg'
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



    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

SimulatorApp().run()
#Thread(target=app.run).start()
#MyCmd(app).cmdloop()
