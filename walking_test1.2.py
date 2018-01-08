# for people walking test
# First part: walking without feedback
# 1.1.walking straight forward
# 1.2.walking left/right
# 1.3.walking straight 3 second, left 1 second, right second
# Second part: walking with feedback
# 2.1. recognize the line
# 2.2. walking straing along the line
# 2.3. walking turning along the line

import numpy as np
from snapshot import grab_screen
import cv2
import time
from models import otherception3 as googlenet
from getkeys import key_check
from collections import deque, Counter
import random
from statistics import mode,mean
import numpy as np
from motion import motion_detection
from wheel import *
from config import GAME_WIDTH, GAME_HEIGHT, WIDTH,HEIGHT,LR,EPOCHS, TOP
import ctypes


SendInput = ctypes.windll.user32.SendInput

KEY_W = 0x11
KEY_A = 0x1E
KEY_S = 0x1F
KEY_D = 0x20


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

if __name__ == '__main__':
    print('Please Press T to Start Fly ....!!!')
    while True:
        keys = key_check()
        if 'T' in keys:
            break
        else:
            time.sleep(2)

    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)    
    while True:
        # for i in range(3*3):
        #     PressKey(KEY_W)
        #     time.sleep(0.3)
        for i in range(3):
             PressKey(KEY_A)
             ReleaseKey(KEY_A)
             time.sleep(0.3)
       # for i in range(10):
       #      PressKey(KEY_W)
       #      time.sleep(1)        
       # for i in range(10):
       #      PressKey(KEY_S)
       #      time.slAAAAAAAAAeep(1)  
       # for i in range(5):
       #      PressKey(KEY_D)
       #      time.sleep(1)  
       # for i in range(10):
       #      PressKey(KEY_S)
       #      time.sleep(1)                