from gpiozero import Servo, DigitalOutputDevice
from time import sleep
#gpizero is pre-installed on raspbian


class Ws4:
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
        pitch_servo = Servo(pitch_pin, initial_value=False)
        yaw_servo = Servo(yaw_pin, initial_value=False)
        fire_relay = DigitalOutputDevice(fire_pin, initial_value=False)


    def fire(duration=5):

        print("Fired!")
        fire_relay.on()
        sleep(duration)
        fire_relay.off()
