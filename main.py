# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 11:24:46 2025

@author: zshaf
"""

import argparse
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


from src.exercises.Lunges import Lunges
from src.exercises.Pushup import Pushup
from src.exercises.Plank import Plank
from src.exercises.ShoulderTap import ShoulderTap
from src.exercises.Squat import Squat

import sys

class WorkoutDetection:
    def __init__(self):
        self.pushup = Pushup()
        self.plank = Plank()
        self.squat = Squat()
        self.shoulderTap = ShoulderTap()
        self.lunges = Lunges()
        
    def rep(self,type,source):
        if type.lower() == str("pushup"):
            self.pushup.exercise(source)
        elif type.lower() == str("squat"):
            self.squat.exercise(source)
        elif type.lower() == str("plank"):
            self.plank.exercise(source)
        elif type.lower() == str("shouldertap"):
            self.shoulderTap.exercise(source)
        elif type.lower() == str("lunges"):
            self.lunges.exercise(source)
        else:
            raise ValueError(f"Input {type} and/or {source} is not correct. \n Kindly refer to the documentation")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-type', "--type", required=True, help="Type of exercise",
                        type=str)
    parser.add_argument('-source', "--source", required=True, help="Path to video source", type=str)
    
    #Test args parse
    sys.argv = ["main.py", "--type", "squat", "--source", "test_data\Squats\squat_input_test.mp4"]
    
    args = parser.parse_args()
    type = args.type
    source = args.source
    gym = WorkoutDetection()
    gym.rep(type, source)