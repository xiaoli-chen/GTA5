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

        walking_along_straight_line(l)
        #cv2.circle(processed_img,(l[2],l[3]),10,[255,0,0])

            #last_time = time.time()
            #screen = cv2.resize(screen, (WIDTH,HEIGHT))



    

