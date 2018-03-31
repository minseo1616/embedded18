import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24

GPIO.setup(TRIG, GPIO.OUT) # LED setup
GPIO.setup(ECHO, GPIO.IN) # Raindrops Sensor setup
GPIO.setup(17, GPIO.OUT) # Servomotor setup
GPIO.setup(18, GPIO.IN) # Button setup

motor = GPIO.PWM(17, 50)
motor.start(7.5)

try:
    while True:
        time.sleep(0.1)

        # If Raindrops Sensor is detected
        if GPIO.input(ECHO) == 0:
            # Blink LED
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(0.1)

            # Window is open(Button is pressed)
            if GPIO.input(18) == True:
                print "Window Close"
                # Close the window using motor
                motor.ChangeDutyCycle(12.5)
                time.sleep(1)
                motor.ChangeDutyCycle(7.5)

        # If Raindrops Sensor is not detected
        else:
            GPIO.output(TRIG, GPIO.LOW) # LED off
            time.sleep(0.1)
            # Window is closed(Button is not pressed)
            if GPIO.input(18) == False:
                print "Window Open"
                # Open the window using motor
                motor.ChangeDutyCycle(2.5)
                time.sleep(1)
                motor.ChangeDutyCycle(7.5)
except KeyboardInterrupt:
    GPIO.cleanup()

