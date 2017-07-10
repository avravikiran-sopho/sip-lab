
#Experiment 1
#VIEWING IMAGES IN DIFFERENT BANDS

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

#import scilab2py module
from scilab2py import scilab

#import other required modules
import pygame
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
class Experiment1App(App):
    #initialize input file name
    fnm = ''

    #Displays file chooser when input image is clicked
    def show_filechooser(self,mainimg,fcw,fchooser):
        if (fcw.height == 0):
            fchooser.height = fchooser.parent.height*8
            fcw.height = fcw.parent.height*8
            mainimg.source='no.gif'

    #Change slider value when text value is given
    def change_slider(self,slider,textinput):
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

    #Displays image in mainimg when clicked on images in bottom panel
    #Blurs the image which is being displayed in mainimg
    def img_viewer(self,mainimg,imgtodisp,otherimg1,otherimg2,otherimg3,otherimg4):
        mainimg.source = imgtodisp.source
        imgtodisp.opacity = 0.3
        otherimg1.opacity = 1
        otherimg2.opacity = 1
        otherimg3.opacity = 1
        otherimg4.opacity = 1

    #If input image is HDR,then bahd value is enabled
    #'No preview available' image is displayed
    #Submit button is enabled
    def enable_band(self,bandvalue,mainimg,submitbtn):
        print self.fnm.find(".")
        print self.fnm
        if (self.fnm.find(".")==-1):
            bandvalue.readonly = False
            bandvalue.hint_text= "Enter band value"
            mainimg.source = "preview.jpg"
            submitbtn.disabled = False


    #Displays preview of selected image from file chooser
    #Adjusts ranges of row start,end and column start,end
    #enables all the inputs
    def show_selected_img(self,mainimg,fcw,fchooser,s4,s5,s6,s7,rstart,rend,cstart,cend,submitbtn,imgname):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            self.fnm = fchooser.selection[0]
            mainimg.source=fchooser.selection[0]
            imgname.text = mainimg.source
            img = pygame.image.load(self.fnm)
            wid=img.get_width()
            hei=img.get_height()
            s4.max = hei-100
            s4.min = 1
            s5.max = hei
            s6.max = wid-100
            s6.min = 1
            s7.max = wid
            rstart.readonly = False
            rend.readonly = False
            cstart.readonly = False
            cend.readonly = False
            rstart.hint_text = "1 - " + str(hei-100)
            rend.hint_text = "100 - " + str(hei)
            cstart.hint_text = "1 - " + str(wid-100)
            cend.hint_text = "100 - " + str(wid)
            submitbtn.disabled = False
            s4.disabled = False
            s5.disabled = False
            s6.disabled = False
            s7.disabled = False
        except :
            pass

    #Calls scilab and images are processed
    def submit(self,s1,s2,s3,s4,s5,s6,s7,mainimg,img1,img2,img3,img4,img5,imgname,btnimg1,btnimg2,btnimg3,btnimg4,btnimg5):
        #matrices are defined to pass in scilab functions
        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        subrow = np.matrix("'"+str(s4.value)+","+str(s5.value)+"'")
        subcol = np.matrix("'"+str(s6.value)+","+str(s7.value)+"'")

        #function to call scilab
        def execute():
            try:
                scilab.getd(os.getcwd()+"/")
                #call imgdisplay functions
                scilab.imgdisplay(self.fnm,rgb,subrow,subcol,'win4pix.txt',outpath)
                #call load functions
                load_images()
            except Exception as e:
                mainimg.source = self.fnm
                res=Popup(title="Error",content=Label(text="" + str(e)),size_hint=(None, None), size=(600, 400))
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
        mainimg.source = 'Loading.gif'
        mainimg.reload()
        imgname.text = "Loading..."
        #call scilab in another thread
        thread = threading.Thread(target=exe,args=())
        thread.start()

        #load all the output images after scilab is executed
        @mainthread
        def load_images():
            #call test_img function for each image to check whether images are produced
            self.test_img(img1,btnimg1,'./'+folder+'/'+'out_original_img.jpg')
            self.test_img(img2,btnimg2,'./'+folder+'/'+'out_subset_img.jpg')
            self.test_img(img3,btnimg3,'./'+folder+'/'+'out_hist_band '+str(int(s1.value))+'.jpg')
            self.test_img(img4,btnimg4,'./'+folder+'/'+'out_hist_band '+str(int(s2.value))+'.jpg')
            self.test_img(img5,btnimg5,'./'+folder+'/'+'out_hist_band '+str(int(s3.value))+'.jpg')
            mainimg.source = img1.source
            img1.opacity = 0.3
            imgname.text = img1.source
            mainimg.reload()

    #Checking for images before display
    def test_img(self,img,btnimg,f):
        if(os.path.isfile(f)):
            img.source = f
            img.reload()
            btnimg.disabled = False
        else:
            img.source = "no.gif"
            btnimg.disabled = True

    #Adjusts end values of row and column when start values are given
    def adjust_end_value(self,sl1,sl2,hint):
    	sl2.min=int(sl1.value)+100
        sl2.value = sl2.min
        hint.hint_text = str(sl1.value)+" - " + str(sl1.max+100)

    #Display mainmenu when button is clicked
    def main_menu(self):
        App.get_running_app().stop()
        os.chdir("..")
        m.SiplabApp().run()

#uncomment the next line to run experiment1 directly
#SimulatorApp().run()
