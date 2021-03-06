# Actuals Functions
import ctypes
from wheel import *
# C struct redefinitions 
import time
from config import GAME_WIDTH, GAME_HEIGHT, WIDTH,HEIGHT,LR,EPOCHS, TOP,DELTA_TIME_CONTROL
import numpy as np
from snapshot import grab_screen
import cv2
from image_recog import find_main_lanes

PUL = ctypes.POINTER(ctypes.c_ulong)

def walking_along_straight_line(paused = False):
    if not paused:
        screen = grab_screen(region=(0,TOP,GAME_WIDTH,GAME_HEIGHT))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        processed_img = cv2.Canny(screen, threshold1=200, threshold2=300)
        processed_img = cv2.GaussianBlur(processed_img, (3,3), 0 )  
        lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 120, 20, 35)
    try:
        l1, l2 = find_main_lanes(processed_img,lines,3)
        if abs(l1[2]-400)>abs(l2[2]-400):
          l = l2
        else:
          l = l1
        #cv2.circle(original_image,(l2[2],l2[3]),10,[0,255,0])
    except Exception as e:
        print('Error in find main lane',str(e))
        pass

            
    print('nearest point lane = ',l[2])
    #mouse_right(10)
    x1 = l[0]
    y1 = l[1]
    x2 = l[2]
    y2 = l[3]
    x_mid = x2+(x1-x2)*(y2-50)/(y2-y1)
    delta_x = (x2-x_mid)
    # if delta_x<-20:
    #     mouse_left(5)
    # elif delta_x>20:
    #     mouse_right(5)

    if abs(l[2]-400)>400:
        straight()
    elif abs(l[2]-400)>200:
        straight()
    elif l[2]-400<-20:
        forward_left()
    elif l[2]-400>20:
        forward_right()
    else:
        straight()

def walking_turn_200(paused = False):
    if not paused:
        screen = grab_screen(region=(0,TOP,GAME_WIDTH,GAME_HEIGHT))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        processed_img = cv2.Canny(screen, threshold1=200, threshold2=300)
        processed_img = cv2.GaussianBlur(processed_img, (3,3), 0 )  
        lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 120, 20, 35)
    try:
        l1, l2 = find_main_lanes(processed_img,lines,3)
        if abs(l1[2]-400)>abs(l2[2]-400):
          l = l2
        else:
          l = l1
        #cv2.circle(original_image,(l2[2],l2[3]),10,[0,255,0])
    except Exception as e:
        print('Error in find main lane',str(e))
        pass
            
    #print('nearest point lane = ',l[2])
    #mouse_right(10)  
    l_list=[l1,l2]  
    xtop1_frombottom200 = l_list[0][0]
    xtop2_frombottom200 = l_list[1][0]
    xbott1_frombottom000 = l_list[0][2]
    xbott2_frombottom000 = l_list[1][2]

    xtop1_frombottom600 = xbott1_frombottom000+3*(xtop1_frombottom200-xbott1_frombottom000)
    xtop2_frombottom600 = xbott2_frombottom000+3*(xtop2_frombottom200-xbott2_frombottom000)
    
    xmid_frombottom600 = 1/2*(xtop1_frombottom600+xtop2_frombottom600)
    if xmid_frombottom600<WIDTH*(0.5-0.5):
        mouse_left(10)
    elif xmid_frombottom600>WIDTH*(0.5+0.5):
        mouse_right(10)
    else:
        pass


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


