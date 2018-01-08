# -*- coding: utf-8; -*-

"""Start to make our car fly~
Source:  Sentdex/pygta5 (https://github.com/Sentdex/pygta5)
Contributor:  Angelapper
Python Version: 3.6+
Changes:
--------



"""
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

how_far_remove = 800
rs = (20,15)
log_len = 25

motion_req = 800
motion_log = deque(maxlen=log_len)

choices = deque([], maxlen=5)
hl_hist = 250
choice_hist = deque([], maxlen=hl_hist)

model = googlenet(WIDTH, HEIGHT, 3, LR, output=9)
#we should change the model name 
MODEL_NAME = 'gtafly-0.001-googlenet-30-epochs-8-data.model'
model.load(MODEL_NAME)

print('Model ',MODEL_NAME,' is ready to go~!')

def main():
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

    screen = grab_screen(region=(0,TOP,GAME_WIDTH,GAME_HEIGHT))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    prev = cv2.resize(screen, (WIDTH,HEIGHT))

    t_minus = prev
    t_now = prev
    t_plus = prev

    while(True):
        
        if not paused:
            screen = grab_screen(region=(0,TOP,GAME_WIDTH,GAME_HEIGHT))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

            last_time = time.time()
            screen = cv2.resize(screen, (WIDTH,HEIGHT))

            delta_count_last = motion_detection(screen,t_minus, t_now, t_plus)

            t_minus = t_now
            t_now = t_plus
            t_plus = screen
            t_plus = cv2.blur(t_plus,(4,4))

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,3)])[0]
           
            print("prediction:",prediction)

            prediction = np.array(prediction) * np.array([1.7, 0.1, 0.1, 0.1,  1.8,   1.8, 0.5, 0.5, 0.2])
            
           # print("prediction mul:",prediction,"\n")

            mode_choice = np.argmax(prediction)

            if mode_choice == 0:
                straight()
                choice_picked = 'straight'
                
            elif mode_choice == 1:
                reverse()
                choice_picked = 'reverse'
                
            elif mode_choice == 2:
                left()
                choice_picked = 'left'
            elif mode_choice == 3:
                right()
                choice_picked = 'right'
            elif mode_choice == 4:
                forward_left()
                choice_picked = 'forward+left'
            elif mode_choice == 5:
                forward_right()
                choice_picked = 'forward+right'
            elif mode_choice == 6:
                reverse_left()
                choice_picked = 'reverse+left'
            elif mode_choice == 7:
                reverse_right()
                choice_picked = 'reverse+right'
            elif mode_choice == 8:
                no_keys()
                choice_picked = 'nokeys'

            motion_log.append(delta_count_last)
            motion_avg = round(mean(motion_log),3)
            print('loop took {} seconds. Motion: {}. Choice: {}'.format( round(time.time()-last_time, 3) , motion_avg, choice_picked))
            
            if motion_avg < motion_req and len(motion_log) >= log_len:
                print('WERE PROBABLY STUCK FFS, initiating some evasive maneuvers.')

                # 0 = reverse straight, turn left out
                # 1 = reverse straight, turn right out
                # 2 = reverse left, turn right out
                # 3 = reverse right, turn left out

                quick_choice = random.randrange(0,4)
                
                if quick_choice == 0:
                    reverse()
                    time.sleep(random.uniform(1,2))
                    forward_left()
                    time.sleep(random.uniform(1,2))

                elif quick_choice == 1:
                    reverse()
                    time.sleep(random.uniform(1,2))
                    forward_right()
                    time.sleep(random.uniform(1,2))

                elif quick_choice == 2:
                    reverse_left()
                    time.sleep(random.uniform(1,2))
                    forward_right()
                    time.sleep(random.uniform(1,2))

                elif quick_choice == 3:
                    reverse_right()
                    time.sleep(random.uniform(1,2))
                    forward_left()
                    time.sleep(random.uniform(1,2))

                for i in range(log_len-2):
                    del motion_log[0]
    
        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                time.sleep(1)


if __name__ == '__main__':
    main()       










