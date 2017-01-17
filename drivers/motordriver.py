import RPi.GPIO as GPIO
from time import sleep


class motorDriver:
    def __init__(self, AN, DIG):
        GPIO.setmode(GPIO.BOARD)
        self.AN = AN
        self.DIG = DIG
        GPIO.setup(self.AN, GPIO.OUT) # set pin as output
        GPIO.setup(self.DIG, GPIO.OUT) # set pin as output
        self.p = GPIO.PWM(AN, 500) # set pwm for M1
        self.p.start(0)

    def forward()
        GPIO.output(self.DIG,GPIO.HIGH)

    def backward()
        GPIO.output(self.DIG, GPIO.LOW))

    def stop()
        self.p.ChangeDutyCycle(0)

    def DutyCycle(val)
        self.p.ChangeDutyCycle(val)

    def cleanup()
        GPIO.cleanup()  

