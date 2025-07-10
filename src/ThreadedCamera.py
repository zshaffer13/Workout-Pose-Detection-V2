# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:25:37 2025

@author: zshaf
"""

from threading import Thread
import cv2, time

class ThreadedCamera(object):
    def __init__(self, src = 0):
        #Default to webcam
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE,2)
        self.FPS = 1/60
        self.FPS_MS = int(self.FPS *1000)
        self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        
        #Start frame retrieval thread
        self.thread = Thread(target = self.update, args =())
        self.frame = None
        self.thread.daemon = True
        self.thread.start()
        
    
    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(self.FPS)
            
    def show_frame(self):
        return self.FPS_MS, self.frame
    
    def create_writer(self):
        #Add video writing for testing
        out = cv2.VideoWriter("test.avi", self.fourcc, self.FPS,(self.width, self.height))

        