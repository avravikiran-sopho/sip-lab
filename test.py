from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from scilab2py import scilab
scilab.getd
import os
import numpy as np

class SimulatorApp(App):

    def submit(self,rvalue,bvalue,gvalue,rstart,rend,cstart,cend,mainimg,img1,img2,img3,img4,img5):
        print rvalue.text
        print bvalue.text
        print gvalue.text
        print rstart.text
        print rend.text
        print cstart.text
        print cend.text



        fnm = 'wallpaper.jpg'
        rgb = np.matrix("'"+(rvalue.text)+","+(gvalue.text)+","+(bvalue.text)+"'")
        subrow = np.matrix("'"+(rstart.text)+","+(rend.text)+"'")
        subcol = np.matrix("'"+(cstart.text)+","+(cend.text)+"'")
        outpath = os.getcwd()+"/"
        scilab.imgdisplay(fnm,rgb,subrow,subcol,'win4pix.txt',outpath)

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

    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

SimulatorApp().run()
