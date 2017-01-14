import serial

class servoDriver:
    def __init__(self, port):
        self.serialPort = serial.Serial(
                            port=port,
                            baudrate=9600,
                            )

    def set_ch_pos_spd(self, channel, position, velocity):
        first_byte = 0b01000000 | channel
        high_byte = (position >> 6) & 0b00011111
        low_byte = position & 0b00111111
        self.serialPort.write(chr(first_byte) + chr(high_byte) + chr(low_byte) + chr(velocity))



