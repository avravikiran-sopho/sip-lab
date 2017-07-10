#Experiment 6
#Experiment 6 name

#import all required kivy modules
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import BorderImage
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import mainthread
import pygame

#import scilab2py module
from scilab2py import scilab

#import other required modules
from datetime import datetime
import time
import os
import numpy as np
import threading
import sys
import os.path
import main as m
p=os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(p)
sys.path.remove(p)

#Background color
Window.clearcolor = (0.1, 0.1, 0.1, 1)

#define all functionality in this class
class Experiment6App(App):
    #initialize input file name
    fnm = ''

    #Displays file chooser when input image is clicked
    def show_filechooser(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*7
        fcw.height = fcw.parent.height*7
        mainimg.source='no.gif'

    #Displays preview of selected image from file chooser
    #Submit button is enabled
    def show_selected_img(self,mainimg,fcw,fchooser,submitbtn,imgname):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            imgname.text = mainimg.source
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            submitbtn.disabled = False
        except:
            pass

    #If input image is HDR,then bahd value is enabled
    #'No preview available' image is displayed
    #Submit button is enabled
    def enable_band(self,bandvalue,mainimg):
        if (self.fnm.find(".")==-1):
            bandvalue.readonly = False
            mainimg.source = "preview.jpg"
            bandvalue.hint_text = "Enter band value"

    #Sets max value of rgb when band value is given
    def set_max_rgb(self,bandvalue,s1,s2,s3,rvalue,gvalue,bvalue):
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
            pass

    #Displays image in mainimg when clicked on images in output panel
    #Blurs the image which is being displayed in mainimg
    def img_viewer (self,mainimg,imgtodisp,otherimg1,otherimg2,otherimg3,otherimg4,otherimg5,otherimg6,otherimg7,otherimg8,otherimg9,otherimg10,otherimg11):
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
        otherimg9.opacity = 1
        otherimg10opacity = 1
        otherimg11.opacity = 1

    #Change slider value when text value is given
    def change_slider (self,slider,textinput):
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
            pass

    #Calls scilab and images are processed
    def submit(self,s1,s2,s3,mainimg,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,btnimg10,btnimg11,btnimg12):
        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        folder=""

        #function to call scilab
        def exe():
            try:
                scilab.getd(os.getcwd()+"/")
                scilab.colourtransform(self.fnm,rgb,outpath)
                load_images()
            except Exception as e:
                mainimg.source = "noimg.jpg"
                res=Popup(title="Error",content=Label(text="" + str(e)),size_hint=(None, None), size=(600, 400))
                res.open()

        #create folder in format "out_day_month_year_hour_minute_second" to store output files
        try:
            now =datetime.now()
            folder="out_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)
            os.mkdir(folder)
        except Exception as ex:
            mainimg.source = self.fnm
            mainimg.reload()
            res=Popup(title="Error",content=Label(text="" + str(ex)),size_hint=(None, None), size=(600, 400))
            res.open()

        #show loadind gif when experiment is running
        outpath = os.getcwd()+"/"+folder+"/"
        mainimg.source = 'Loading.gif'
        imgname.text = "Loading..."
        mainimg.reload()
        #call scilab in another thread
        thread = threading.Thread(target=execute(),args=())
        thread.start()

        #load all the output images after scilab is executed
        @mainthread
        def load_images():
            #call test_img function for each image to check whether images are produced
            self.test_img(img1,btnimg1,outpath+'out_original_img.jpg')
            self.test_img(img2,btnimg2,outpath+'out_RGB.jpg')
            self.test_img(img3,btnimg3,outpath+'out_Red.jpg')
            self.test_img(img4,btnimg4,outpath+'out_Green.jpg')
            self.test_img(img5,btnimg5,outpath+'out_Blue.jpg')
            self.test_img(img6,btnimg6,outpath+'out_VALUE.jpg')
            self.test_img(img7,btnimg7,outpath+'out_SATURATION.jpg')
            self.test_img(img8,btnimg8,outpath+'out_HSV.jpg')
            self.test_img(img9,btnimg9,outpath+'out_HUE.jpg')
            self.test_img(img10,btnimg10,'./'+folder+'/'+'out_hist_band '+str(int(s1.value))+'.jpg')
            self.test_img(img11,btnimg11,'./'+folder+'/'+'out_hist_band '+str(int(s2.value))+'.jpg')
            self.test_img(img12,btnimg12,'./'+folder+'/'+'out_hist_band '+str(int(s3.value))+'.jpg')
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

    #Display main_menu when button is clicked
    def main_menu(self):
        App.get_running_app().stop()
        os.chdir("..")
        m.SiplabApp().run()

    #test if the ouput images are produced
    def test_img(self,img,btnimg,f):
        if(os.path.isfile(f)):
            img.source = f
            img.reload()
            btnimg.disabled = False
        else:
            img.source = "no.gif"
            btnimg.disabled = True

#uncomment the next line to run experiment1 directly
#Experiment6App().run()
