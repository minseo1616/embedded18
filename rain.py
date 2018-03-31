import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

motor = GPIO.PWM(17, 50)
motor.start(7.5)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(ECHO) == 0:
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(0.1)
            if GPIO.input(18) == True:
                print "Window Close"
                motor.ChangeDutyCycle(12.5)
                time.sleep(1)
                motor.ChangeDutyCycle(7.5)

        else:
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(0.1)
            if GPIO.input(18) == False:
                print "Window Open"
                motor.ChangeDutyCycle(2.5)
                time.sleep(1)
                motor.ChangeDutyCycle(7.5)
except KeyboardInterrupt:
    GPIO.cleanup()

