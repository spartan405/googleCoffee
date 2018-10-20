import RPi.GPIO as GPIO
import time
import sys

#str_num = sys.argv[3]
#num = int(str_num)


#blinking function
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	return
#to use board pin numbers
GPIO.setmode(GPIO.BOARD)

#set up the output channel
GPIO.setup(11,GPIO.OUT)

#blink 50 times
for i in range(0,int(sys.argv[1])):
	blink(11)
print('done')
GPIO.cleanup()