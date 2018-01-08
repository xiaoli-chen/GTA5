# Actuals Functions
import ctypes
from wheel import *
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
