#!/usr/bin/python3
"""Run inference with a YOLOv5 model on images, videos, directories, streams

Usage:
    $ python path/to/detect.py --source path/to/img.jpg --weights yolov5s.pt --img 640
"""
import os
#import pdb;pdb.set_trace()

# Printer Library
import json
# from Adafruit_Thermal import *

# printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

#Sparkfun Barcode Library
import de2120_barcode_scanner
my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()

import random    
import argparse
import sys,os,glob
import time
from pathlib import Path
import cv2

# Daryl UI Changes
from tkinter import *
import tkinter.font as tkFont
from kivy.config import Config

Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 0)
Config.set('graphics', 'top',   0)
Config.set('graphics', 'resizable', 'False')
Config.set('graphics', 'borderless',  1)
Config.set('graphics','verify_gl_main_thread',0)
#1920x1080
#1280x780
# Config.set('graphics', 'width', 1920)
# Config.set('graphics', 'height', 1080)
#Horizontal Screen
#Config.set('graphics', 'width', 1366)
#Config.set('graphics', 'height', 768)
#Vertical Screen
Config.set('graphics', 'height', 1366)
Config.set('graphics', 'width', 768)

#Config.set('graphics','fullscreen','True')
#Config.set('graphics','window_state','maximised')
import requests, pyqrcode, os
os.environ['KIVY_NO_ARGS']="1"
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.app import MDApp
