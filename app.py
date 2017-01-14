import socketio
import eventlet
import serial
import json
import RPi.GPIO as GPIO
from time import sleep
import servodriver
import time
from flask import Flask, render_template


#arduinoSerial = serial.Serial('/dev/ttyACM0', 115200)
#servoDriverSerial  = servodriver.servoDriver('/dev/ttyUSB0')
sio = socketio.Server()
# servoDriverSerial.set_ch_pos_spd(4, 731, 20)
sleep(0.5)
# servoDriverSerial.set_ch_pos_spd(2, 731, 20)
sleep(0.5)
# servoDriverSerial.set_ch_pos_spd(3, 731, 20)
sleep(0.5)

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('yaxis')
def message(sid, data):
    servoDriverSerial.set_ch_pos_spd(5, (int(int(data['yaxis']) * 8.12)), 20);

@sio.on('xaxis')
def message(sid, data):
    print int(data['xaxis'])
    servoDriverSerial.set_ch_pos_spd(4, (int(int(data['xaxis']) * 8.12)), 30);
    time.sleep(0.5)
    servoDriverSerial.set_ch_pos_spd(2, (1462 - int(int(data['xaxis']) * 8.12)), 30);
    time.sleep(0.5)
    servoDriverSerial.set_ch_pos_spd(3, (1462 - int(int(data['xaxis']) * 8.12)), 30);
    time.sleep(0.5)

@sio.on('zaxis')
def message(sid, data):
    print int(data['zaxis'])
#    servoDriverSerial.set_ch_pos_spd(4, (int(int(data['zaxis']) * 8.12)), 30);
    servoDriverSerial.set_ch_pos_spd(2, (int(int(data['zaxis']) * 8.12)), 30);
    time.sleep(0.5)
    servoDriverSerial.set_ch_pos_spd(3, (1462 - int(int(data['zaxis']) * 8.12)), 30);
    time.sleep(0.5)

@sio.on('servo one')
def message(sid, data):
    print int(data['value'])
    servoDriverSerial.set_ch_pos_spd(4, (int(int(data['value']) * 8.12)), 30);
    time.sleep(0.5)

@sio.on('servo two')
def message(sid, data):
    print int(data['value'])
    servoDriverSerial.set_ch_pos_spd(2, (int(int(data['value']) * 8.12)), 30);
    time.sleep(0.5)

@sio.on('servo three')
def message(sid, data):
    print int(data['value'])
    servoDriverSerial.set_ch_pos_spd(3, (int(int(data['value']) * 8.12)), 30);
    time.sleep(0.5)

@sio.on('self mode direction')
def message(sid, data):
    if (int(data['value']) == 38):
    	arduinoSerial.write(str(8))
    if (int(data['value']) == 40):
        arduinoSerial.write(str(2))
    if (int(data['value']) == 37):
        arduinoSerial.write(str(4))
    if (int(data['value']) == 39):
        arduinoSerial.write(str(6))
    if (int(data['value']) == 0):
        arduinoSerial.write(str(5))
    print str(data['value'])

@sio.on('max drivespeed')
def message(sid, data):
    arduinoSerial.write('S' + str(data['value']))
    print 'changing max speed' + 'S' + str(data['value'])


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with socketio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8888)), app)

#
# GPIO.setmode(GPIO.BOARD)
#
# AN = 38
# DIG = 40
#
# GPIO.setup(AN, GPIO.OUT) # set pin as output
# GPIO.setup(DIG, GPIO.OUT) # set pin as output
#
# sleep(1) # delay for 1 seconds
#
# p1 = GPIO.PWM(AN, 500) # set pwm for M1
#
# while True:
#   GPIO.output(DIG, GPIO.HIGH)
#   p1.start(100)
#   #p1.ChangeDutyCycle(dc)

