from pynput.keyboard import Key, Controller
import time
import random
import string
#import winsound
import os
os.system('start notepad')
duration=1000
freq=300
time_elapse=0.10
kb=Controller()
s='YOU HAVE BEEN HACKED!'
c=0
#time.sleep(3)
while c!=len(s):
	time.sleep(time_elapse)
	#winsound.Beep(freq, duration)
	kb.press(s[c])
	kb.release(s[c])
	c+=1
c=0
r = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
while True:
	if (c==len(r)):
		c=0
		r = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
	time.sleep(time_elapse)
	kb.press(r[c])
	kb.release(r[c])
	c+=1
