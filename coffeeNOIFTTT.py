import RPi.GPIO as GPIO
import time


#blinking function
def blinking(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.1)
	return
#to use board pin numbers
GPIO.setmode(GPIO.BOARD)

#set up the output channel
GPIO.setup(11,GPIO.OUT)

blinking(11)
#blink 50 times
#for i in range(0,50):
#	blink(11)
GPIO.cleanup()