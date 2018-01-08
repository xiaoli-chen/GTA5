from snapshot import grab_screen
from config import GAME_WIDTH,GAME_HEIGHT
from getkeys import key_check,keys_to_output, query_mouse_position
import cv2
import time
from wheel import mouse_left, mouse_right

def test_snapshot():
    screen = grab_screen(region=(0,400,GAME_WIDTH,GAME_HEIGHT))
    cv2.imwrite( "test.jpg", screen )

def test_list():
	a = []
	a.append('A')
	a.append('S')
	b = []
	b.append('S')
	b.append('A')

	print('a vs b', sorted(a,reverse=True), sorted(b))

def test_key_check():
	while True:
		keys = key_check()
		output = keys_to_output(keys)
		if 'T' in keys:
			print('Break!', keys)
			print('Break Out!', output)
			break
		else:
			print('Input!', keys)
			print('Input Out!', output)
			time.sleep(1)

def test_mouse_position():
	while True:
		keys = key_check()		
		cur_cursor = query_mouse_position()
		if 'T' in keys:
			print('Break!', cur_cursor)
			break
		else:
			print('Current Cursor!', cur_cursor)
			time.sleep(1)

def test_mouse_move():
	while True:
		keys = key_check()		
		mouse_right(35)
		time.sleep(0.5)
		mouse_left(35)
		time.sleep(0.5)
		mouse_left(35)
		time.sleep(0.5)
		mouse_right(35)

		if 'T' in keys:
			print('Break!')
			break
		else:
			print('Current Cursor!')
			time.sleep(1)

if __name__ == "__main__":
   #test_snapshot()
   #test_key_check()
   #test_mouse_position()
   test_mouse_move()
#   test_list()