from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from scilab2py import scilab
scilab.getd
import os
import numpy as np
import pygame
import os

class SimulatorApp(App):
    fnm = ''
    #popup = Popup(content=Label(text='Hello world'))
    #popup.bind(on_dismiss=my_callback)
    #popup.open()
    class CustomPopup():
        pass
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*6.5
        fcw.height = fcw.parent.height*6.5
        mainimg.source='black.png'

    def showmainimg(self,mainimg,fcw,fchooser,s4,s5,s6,s7):

        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            print(self.fnm)
            img = pygame.image.load(self.fnm)
            wid=img.get_width()
            hei=img.get_height()
            s4.max=str(int(wid)-100)
            s5.max=wid
            s6.max=str(int(hei)-100)
            s7.max=hei
        except:
            print fchooser.selection



    def changeVal(sl1,sl2):
    	rstart.text = str(s4.value)
    	s5.min=int(s4.value)+100


    def submit(self,rvalue,bvalue,gvalue,rstart,rend,cstart,cend,mainimg,img1,img2,img3,img4,img5):
        print rvalue.text
        print bvalue.text
        print gvalue.text
        print rstart.text
        print rend.text
        print cstart.text
        print cend.text
        rgb = np.matrix("'"+(rvalue.text)+","+(gvalue.text)+","+(bvalue.text)+"'")
        subrow = np.matrix("'"+(rstart.text)+","+(rend.text)+"'")
        subcol = np.matrix("'"+(cstart.text)+","+(cend.text)+"'")
        outpath = os.getcwd()+"/"
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
    def show_popup(self):
        p = self.CustomPopup()
        p.open()
    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'
SimulatorApp().run()
