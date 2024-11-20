import RPi.GPIO as GPIO

heater_on = GPIO.HIGH
heater_off = GPIO.LOW

class IO_CTRL(object):
    def __init__(self, heater_pins):
        self.heater_pins = heater_pins
        self.heater_states = [0] * len(heater_pins)

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)       
        GPIO.setup(self.heater_pins, GPIO.OUT, initial=heater_off) #setup the heater pins as outputs and initalize them as low

    def heat(self, tank_num, heater_state): #turn on associated heater
        if heater_state:
            GPIO.output(self.heater_pins[tank_num], heater_on)
        else:
            GPIO.output(self.heater_pins[tank_num], heater_off)
        self.heater_states[tank_num] = heater_state

    def cleanup(self): #cleanup
        GPIO.cleanup()
