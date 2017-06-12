from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from scilab2py import scilab
scilab.getd('~/Documents/foss/')
import os
import numpy as np

class CalcApp(App):
    def input(self):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

CalcApp().run()

