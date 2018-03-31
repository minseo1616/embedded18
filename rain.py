import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24

GPIO.setup(TRIG, GPIO.OUT) # LED setup
GPIO.setup(ECHO, GPIO.IN) # 빗물 감지 센서 setup
GPIO.setup(17, GPIO.OUT) # servomotor setup
GPIO.setup(18, GPIO.IN) # Button setup

motor = GPIO.PWM(17, 50)
motor.start(7.5)

try:
    while True:
        time.sleep(0.1)

        # 빗물이 감지되면
        if GPIO.input(ECHO) == 0:
            # LED를 깜빡깜빡
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(0.1)

            # 창문이 열려있으면(버튼이 눌려있으면)
            if GPIO.input(18) == True:
                print "Window Close"
                # 모터를 이용해 창문을 닫아줌
                motor.ChangeDutyCycle(12.5)
                time.sleep(1)
                motor.ChangeDutyCycle(7.5)

        # 빗물이 감지 되지 않으면
        else:
            GPIO.output(TRIG, GPIO.LOW) # LED off
            time.sleep(0.1)
            # 창문이 닫혀있으면(버튼이 눌려있지 않으면)
            if GPIO.input(18) == False:
                print "Window Open"
                # 창문을 열어줌
                motor.ChangeDutyCycle(2.5)
                time.sleep(1)
                motor.ChangeDutyCycle(7.5)
except KeyboardInterrupt:
    GPIO.cleanup()

