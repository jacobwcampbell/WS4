from gpiozero import AngularServo, DigitalOutputDevice
from time import sleep
from random import randint
#gpizero is pre-installed on raspbian

class Ws4(object):
    '''
    This is a class to control all GPIO, Physical aspects of the device
    
    Attributes:
        pitch_pin(int) - This is the BCM number of the GPIO pin connected to the 'pitch' servo
        yaw_pin(int) - This is the BCM number of the GPIO pin connected to the 'yaw' servo
        fire_pin(int) - This is the BCM number of the GPIO pin connected to the 'fire' relay, which closes the circuit for the device's firing mechanism
    '''

    def __init__(self, pitch_pin, yaw_pin, fire_pin):
        '''Sets up the physical GPIO pins that the device uses to control the motors and relays'''
        self.pitch_pin = pitch_pin
        self.yaw_pin = yaw_pin        
        self.fire_pin = fire_pin
        self.pitch_servo = AngularServo(pitch_pin, min_angle=-90, max_angle=90, initial_value=False)
        self.yaw_servo = AngularServo(yaw_pin, min_angle=-90, max_angle=90, initial_value=False)
        self.fire_relay = DigitalOutputDevice(fire_pin, initial_value=False)
        self.calibrate()

    def calibrate(self):
        '''Moves each servo to it's minimum and maximum positions, before returning to it's neutral position (0 degrees relative)'''
        self.yaw_servo.min()
        sleep(1)
        self.yaw_servo.max()
        sleep(1)
        self.yaw_servo.mid()
        sleep(1)
        self.pitch_servo.min()
        sleep(1)
        self.pitch_servo.max()
        sleep(1)
        self.pitch_servo.mid()
    

    def fire(self, duration=5):
        '''Activates the relay, which is connected to the fire mechanism. The duration determines how long the device will fire for'''
        print("Fired!")
        self.fire_relay.on()
        sleep(duration)
        self.fire_relay.off()


    def move_right(self, turn_amount=10):
        '''Moves the yaw (L/R) motor by a relative amount, which is the turn_amount parameter. The if statement stops the Servo.angle value from increasing beyond it's maximum '''
        if self.yaw_servo.angle < 90:
            self.yaw_servo.angle += turn_amount
    
    def move_left(self, turn_amount=10):
        if self.yaw_servo.angle > -90:
            self.yaw_servo.angle -= turn_amount

    def move_up(self, turn_amount=10):
        if self.pitch_servo.angle < 90:
            self.pitch_servo.angle += turn_amount

    def move_down(self, turn_amount=10):
        if self.pitch_servo.angle > -90:
            self.pitch_servo.angle -= turn_amount

    def move_to(self, yaw_position, pitch_position):
        '''Takes a yaw and pitch position between -90 and 90 degrees and sets the Servo.angle values to that, instead of increasing by pre-defined 'steps' '''
        self.yaw_servo.angle = yaw_position
        self.pitch_servo.angle = pitch_position

    def location(self):
        '''Returns the current yaw and pitch position of both servo's'''
        return "Yaw:"+self.yaw_servo.angle+"  Pitch:"+self.pitch_servo.angle


class Ws4dummy(object):
    '''A Dummy version of the main class, used to initially test the web interface, via printing statements instead of activating servos'''
    def __init__(self):
        pass

    def fire(self):
        print("Fired!")

    def move_right(self):
        print("Turned Right!")

    def move_left(self):
        print("Turned Left!")

    def move_up(self):
        print("Turned Up!")        

    def move_down(self):
        print("Turned Down!")

    def location(self):
        return "Yaw:"+randint(0,90)+" Pitch"+randint(0,90)