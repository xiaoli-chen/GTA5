# Actuals Functions
import ctypes
from wheel import *
# C struct redefinitions 
import time
from config import GAME_WIDTH, GAME_HEIGHT, WIDTH,HEIGHT,LR,EPOCHS, TOP,DELTA_TIME_CONTROL

PUL = ctypes.POINTER(ctypes.c_ulong)

def walking_along_straight_line(l):
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
        PressKey(KEY_W)
        time.sleep(DELTA_TIME_CONTROL)
        ReleaseKey(KEY_W)
    elif abs(l[2]-400)>200:
        PressKey(KEY_W)
        time.sleep(DELTA_TIME_CONTROL)
        ReleaseKey(KEY_W)
    elif l[2]-400<-20:
        PressKey(KEY_A)
        PressKey(KEY_W)
        time.sleep(DELTA_TIME_CONTROL)
        ReleaseKey(KEY_A)
        ReleaseKey(KEY_W)
    elif l[2]-400>20:
        PressKey(KEY_D)
        PressKey(KEY_W)
        time.sleep(DELTA_TIME_CONTROL)
        ReleaseKey(KEY_D)
        ReleaseKey(KEY_W)
    else:
        PressKey(KEY_W)
        time.sleep(DELTA_TIME_CONTROL)
        ReleaseKey(KEY_W)

def walking_turn_200(l_list):
    x1_1 = l_list[0][0]
    x2_1 = l_list[1][0]
    x_top_mid = 1/2*(x1_1+x2_1)
    if x_top_mid<WIDTH*(0.5-0.12):
        mouse_left(5)
    elif x_top_mid>WIDTH*(0.5+0.2):
        mouse_right(5)

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


def straight():
    PressKey(KEY_W)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_S)

def left():
    PressKey(KEY_A)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)
    ReleaseKey(KEY_D)
    #ReleaseKey(KEY_S)

def right():
    PressKey(KEY_D)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)

def forward_left():
    PressKey(KEY_W)
    PressKey(KEY_A)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_S)
    
    
def forward_right():
    PressKey(KEY_W)
    PressKey(KEY_D)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)
