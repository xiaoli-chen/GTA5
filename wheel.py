from directkeys import (PressKey,ReleaseKey, 
    KEY_W, KEY_A, KEY_S, KEY_D, mouse_move)

from getkeys import query_mouse_position

t_time = 0.25

def straight():
    PressKey(KEY_W)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_S)

def left():
    if random.randrange(0,3) == 1:
        PressKey(KEY_W)
    else:
        ReleaseKey(KEY_W)
    PressKey(KEY_A)
    ReleaseKey(KEY_S)
    ReleaseKey(KEY_D)
    #ReleaseKey(KEY_S)

def right():
    if random.randrange(0,3) == 1:
        PressKey(KEY_W)
    else:
        ReleaseKey(KEY_W)
    PressKey(KEY_D)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)
    
def reverse():
    PressKey(KEY_S)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_D)


def forward_left():
    PressKey(KEY_W)
    PressKey(KEY_A)
    ReleaseKey(KEY_D)
    ReleaseKey(KEY_S)
    
    
def forward_right():
    PressKey(KEY_W)
    PressKey(KEY_D)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)

    
def reverse_left():
    PressKey(KEY_S)
    PressKey(KEY_A)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_D)

    
def reverse_right():
    PressKey(KEY_S)
    PressKey(KEY_D)
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_A)

def no_keys():

    if random.randrange(0,3) == 1:
        PressKey(KEY_W)
    else:
        ReleaseKey(KEY_W)
    ReleaseKey(KEY_A)
    ReleaseKey(KEY_S)
    ReleaseKey(KEY_D)

def mouse_left(offset):
    cur_pos = query_mouse_position()
    mouse_move(cur_pos['x']-offset,cur_pos['y'])

def mouse_right(offset):
    cur_pos = query_mouse_position()
    mouse_move(cur_pos['x']+offset,cur_pos['y'])
