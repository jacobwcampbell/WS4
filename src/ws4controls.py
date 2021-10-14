from _typeshed import Self
from gpiozero import AngularServo, DigitalOutputDevice
from time import sleep
#gpizero is pre-installed on raspbian


class Ws4(object):
    '''
    This is a class to control all GPIO, Physical aspects of the device
    
    Attributes:
        pitch_pin(int) - This is the BCM number of the GPIO pin connected to the 'pitch' servo
        yaw_pin(int) - This is the BCM number of the GPIO pin connected to the 'yaw' servo
        fire_pin(int) - This is the BCM number of the GPIO pin connected to the 'fire' relay, which closes the circuit for the device's firing mechanism
    '''

    def __init__(self,pitch_pin,yaw_pin,fire_pin):
        self.pitch_pin = pitch_pin
        self.yaw_pin = yaw_pin
        self.fire_pin = fire_pin
        self.pitch_servo = AngularServo(pitch_pin, min_angle=-90, max_angle=90, initial_value=False)
        self.yaw_servo = AngularServo(yaw_pin, min_angle=-90, max_angle=90,  initial_value=False)
        self.fire_relay = DigitalOutputDevice(fire_pin, initial_value=False)


    def fire(self,duration=5):
        print("Fired!")
        self.fire_relay.on()
        sleep(duration)
        self.fire_relay.off()


    def move_right(self,turn_amount=10):
        if self.yaw_servo.angle < 90:
            self.yaw_servo.angle +=turn_amount
    
    def move_left(self,turn_amount=10):
        if self.yaw_servo.angle > -90:
            self.yaw_servo.angle -=turn_amount

    def move_up(self,turn_amount=10):
        if self.pitch_servo.angle < 90:
            self.pitch_servo.angle +=turn_amount

    def move_down(self,turn_amount=10):
        if self.pitch_servo.angle > -90:
            self.pitch_servo.angle -=turn_amount

class Ws4dummy(object):
    
    def __init__(self):
        pass

    def fire(self):
        print("Fired!")
