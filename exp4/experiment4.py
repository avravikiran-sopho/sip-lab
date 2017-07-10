#Experiment 4
#EDGE DETECTION

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
class Experiment4App(App):
    #initialize input file name
    fnm = ''

    #Display main_menu when button is clicked
    def main_menu(self):
        App.get_running_app().stop()
        os.chdir("..")
        m.SiplabApp().run()

    #Displays file chooser when input image is clicked
    def show_filechooser(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*8.5
        fcw.height = fcw.parent.height*8.5
        mainimg.source='no.gif'

    #Displays preview of selected image from file chooser
    #submit button is enabled
    def show_selected_img(self,mainimg,fcw,fchooser,submitbtn,imgname):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            imgname.text = mainimg.source
            submitbtn.disabled = False
        except:
            pass

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

    #set type
    def set_type(self,eg):
        self.egtype=eg

    #set direction
    def set_dir(self,d):
        self.direction=d

    #Calls scilab and images are processed
    def submit(self,rgbslider,slider,mainimg,img1,img2,img3,imgname):
        folder=""

        #validating inputs
        dec=True
        try:
            print self.egtype,"   ",self.direction,"  ",self.fnm
            if(self.egtype==""):
                dec=False
                Popup(title="Error",content=Label(text="Please select edge type"),size_hint=(None, None), size=(600, 200)).open()
            if(self.direction==""):
                Popup(title="Error",content=Label(text="Please select direction type"),size_hint=(None, None), size=(600, 200)).open()
                dec=False
            if(self.fnm==""):
                Popup(title="Error",content=Label(text="Please select file type"),size_hint=(None, None), size=(600, 200)).open()
                dec=False
        except:
            dec=False

        #function to call scilab
        def execute():
            try:
                scilab.getd(os.getcwd()+"/")
                #call scilab test function
                scilab.test(self.fnm,rgbslider.value,self.egtype,slider.value,self.direction,outpath)
                load_images()
            except Exception as e:
                res=Popup(title="Error",content=Label(text="" + str(e)),size_hint=(None, None), size=(600, 400))
                mainimg.source = self.fnm
                mainimg.reload()
                res.open()

        #create folder in format "out_day_month_year_hour_minute_second" to store output files
        try:
            now =datetime.now()
            folder="out_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)
            os.mkdir(folder)
        except Exception as ex:
            mainimg.source = self.fnm
            res=Popup(title="Error",content=Label(text="" + str(ex)),size_hint=(None, None), size=(600, 400))
            res.open()

        #show loadind gif when experiment is running
        outpath = os.getcwd()+"/"+folder+"/"
        if(dec):
            imgname.text = "Loading..."
            mainimg.source = 'Loading.gif'
            mainimg.reload()
            #call scilab in another thread
            thread = threading.Thread(target=execute,args=())
            thread.start()
        else:
            pass

        #load all the output images after scilab is executed
        @mainthread
        def load_images():
            #call test_img function for each image to check whether images are produced
            self.test_img(img1,btnimg1,self.fnm)
            self.test_img(img2,btnimg2,outpath+'out_original_img.jpg')
            self.test_img(img3,outpath+'edgeimg.jpg')
            mainimg.source = img1.source
            img1.reload()
            img2.reload()
            img3.reload()
            mainimg.reload()
            img1.opacity = 1
            imgname.text = mainimg.source

    #test if the ouput images are produced
    def test_img(self,img,btnimg,f):
        if(os.path.isfile(f)):
            img.source = f
            img.reload()
            btnimg.disabled = False
        else:
            img.source = "no.gif"
            btnimg.disabled = True

    #Displays image in mainimg when clicked on images in output panel
    #Blurs the image which is being displayed in mainimg
    def img_viewer  (self,mainimg,imgtodisp,otherimg1,otherimg2):
        mainimg.source = imgtodisp.source
        imgtodisp.opacity = 1
        otherimg1.opacity = 0.3
        otherimg2.opacity = 0.3

#uncomment the next line to run experiment4 directly
#Experiment4App().run()
