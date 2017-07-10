from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.core.window import WindowBase
from exp1 import experiment1 as t1
import os
from exp2 import experiment2 as t2
from exp3 import experiment3 as t3
from exp4 import experiment4 as t4
from exp5 import experiment5 as t5
from exp6 import experiment6 as t6
#Window.ful
Window.clearcolor = (0.1, 0.1, 0.1, 1)
from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.core.window import Window
Window.size = (1920, 1080)
#import pymysql
#import hashlib



class SiplabApp(App):
	
	#uncomment these for login functionality.
	"""
	s = ""
    role = ""
    def active(self,exp):
        self.s = exp

    def setrole(self,roles):
        self.role = roles

    def siplab(self,username,password):
        conn = pymysql.connect(host='localhost',user='root',password='avrkiran',db='siplab')
        print self.role,self.s
        a = conn.cursor()
        hash_password = hashlib.md5(password.text).hexdigest()
        sql1 = "INSERT INTO  `siplab`.`users` (`id` ,`name` ,`password` ,`category`) VALUES (NULL,%s,%s,%s);"
        sql2 = "INSERT INTO  `siplab`.`experiments` (`id` ,`name` ,`experiment`)VALUES (NULL,%s,%s);"
        try:
            role = self.role
            s = self.s
            a.execute(sql1,(username.text,hash_password,role))
            conn.commit()
            a.execute(sql2,(username.text,s))
            conn.commit()
        except Exception as e:
            print e
            conn.rollback()"""

    def siplab(self,experiment):

        App.get_running_app().stop()
        if(experiment=="exp1"):
            os.chdir("./exp1/")
            print(os.getcwd())
            t1.Experiment1App().run()
        elif(experiment=="exp2"):
            os.chdir("./exp2/")
            print(os.getcwd())
            t2.Experiment2App().run()
        elif(experiment=="exp3"):
            os.chdir("./exp3/")
            print(os.getcwd())
            t3.Experiment3App().run()
        elif(experiment=="exp4"):
            os.chdir("./exp4/")
            print(os.getcwd())
            t4.Experiment4App().run()
        elif(experiment=="exp5"):
            os.chdir("./exp5/")
            print(os.getcwd())
            t5.Experiment5App().run()
        elif(experiment=="exp6"):
            os.chdir("./exp6/")
            print(os.getcwd())
            t6.Experiment6App().run()

#SiplabApp().run()
