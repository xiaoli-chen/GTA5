# for people walking test
# First part: walking without feedback
# 1.1.walking straight forward
# 1.2.walking left/right
# 1.3.walking straight 3 second, left 1 second, right second
# Second part: walking with feedback
# 2.1. recognize the lane
# --todo use color to filter lane: ~yellow, ~white 
      #(~means around)

# 2.2. walking straing along the line
# 2.3. walking turning along the line
# --todo control mouse movement
# it will turn if walk slow

# 3.1 change work flow: move 'grabdata' into walkturn, walkstraight function'
# 3.1 need update: move 'grabdata and recognize lane' into one function grab_recog
# 3.2 turn with higher frequency than walk
# 3.3 show recognized lane and background, real-time
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
from config import GAME_WIDTH, GAME_HEIGHT, WIDTH,HEIGHT,LR,EPOCHS, TOP,DELTA_TIME_CONTROL
import ctypes

from image_recog import *
from control import *

SendInput = ctypes.windll.user32.SendInput

KEY_W = 0x11
KEY_A = 0x1E
KEY_S = 0x1F
KEY_D = 0x20


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


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

    paused = False
    mode_choice = 0
    # region=(x1,y1,x2,y2) # upleft, downright
    screen = grab_screen(region=(0,TOP,GAME_WIDTH,GAME_HEIGHT))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    #prev = cv2.resize(screen, (WIDTH,HEIGHT))

    # t_minus = prev
    # t_now = prev
    # t_plus = prev
    #l = [400,0,400,0]
    while(True):
        # region=(x1,y1,x2,y2)


        walking_turn_200(paused = False)
        walking_along_straight_line(paused = False)
        #cv2.circle(processed_img,(l[2],l[3]),10,[255,0,0])

            #last_time = time.time()
            #screen = cv2.resize(screen, (WIDTH,HEIGHT))



    

