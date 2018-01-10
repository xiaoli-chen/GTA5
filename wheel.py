from directkeys import (PressKey,ReleaseKey, 
    KEY_W, KEY_A, KEY_S, KEY_D, mouse_move)
from config import DELTA_TIME_CONTROL
from getkeys import query_mouse_position
import time

def straight():
    PressKey(KEY_W)
    time.sleep(DELTA_TIME_CONTROL)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_S)

def left():
    PressKey(KEY_A)
    time.sleep(DELTA_TIME_CONTROL)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_S)

def right():
    PressKey(KEY_D)
    time.sleep(DELTA_TIME_CONTROL)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)

def forward_left():
    PressKey(KEY_W)
    PressKey(KEY_A)
    time.sleep(DELTA_TIME_CONTROL)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_S)
    
    
def forward_right():
    PressKey(KEY_W)
    PressKey(KEY_D)
    time.sleep(DELTA_TIME_CONTROL)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)

def mouse_left(offset):
    #cur_pos = query_mouse_position()
    mouse_move(-1*offset,0)

def mouse_right(offset):
    #cur_pos = query_mouse_position()
    mouse_move(offset,0)    
# t_time = 0.25

# def straight():
#     PressKey(KEY_W)
#     ReleaseKey(KEY_A)
#     ReleaseKey(KEY_D)
#     ReleaseKey(KEY_S)

# def left():
#     if random.randrange(0,3) == 1:
#         PressKey(KEY_W)
#     else:
#         ReleaseKey(KEY_W)
#     PressKey(KEY_A)
#     ReleaseKey(KEY_S)
#     ReleaseKey(KEY_D)
#     #ReleaseKey(KEY_S)

# def right():
#     if random.randrange(0,3) == 1:
#         PressKey(KEY_W)
#     else:
#         ReleaseKey(KEY_W)
#     PressKey(KEY_D)
#     ReleaseKey(KEY_A)
#     ReleaseKey(KEY_S)
    
# def reverse():
#     PressKey(KEY_S)
#     ReleaseKey(KEY_A)
#     ReleaseKey(KEY_W)
#     ReleaseKey(KEY_D)


# def forward_left():
#     PressKey(KEY_W)
#     PressKey(KEY_A)
#     ReleaseKey(KEY_D)
#     ReleaseKey(KEY_S)
    
    
# def forward_right():
#     PressKey(KEY_W)
#     PressKey(KEY_D)
#     ReleaseKey(KEY_A)
#     ReleaseKey(KEY_S)

    
# def reverse_left():
#     PressKey(KEY_S)
#     PressKey(KEY_A)
#     ReleaseKey(KEY_W)
#     ReleaseKey(KEY_D)

    
# def reverse_right():
#     PressKey(KEY_S)
#     PressKey(KEY_D)
#     ReleaseKey(KEY_W)
#     ReleaseKey(KEY_A)

# def no_keys():

#     if random.randrange(0,3) == 1:
#         PressKey(KEY_W)
#     else:
#         ReleaseKey(KEY_W)
#     ReleaseKey(KEY_A)
#     ReleaseKey(KEY_S)
#     ReleaseKey(KEY_D)


