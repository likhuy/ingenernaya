import RPi.GPIO as GPIO
import time

dac=[8,11,7,1,0,5,12,6]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 13
comparator = 14


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule , GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def dec2bin(decimal):
    return [int(elem) for elem in bin(decimal)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal
def adc():
    for value in range(256):
        a = dec2bin(value)
        GPIO.output(dac, a)
        time.sleep(0.001)
        comparatorValue = GPIO.input(comparator)
        if comparatorValue == 1:
            return value
            break


try:
    while True:
        value = adc()
        if type(value) == int:
            voltage = value / levels * maxVoltage
            print("Digital = ", value, "Voltage = ", voltage)
        else:
            print("Error")
        

except KeyboardInterrupt:
    print('\nThe program was stoped by keyboard')
else:
    print('No exceptions')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troykaModule, GPIO.LOW)
    GPIO.cleanup(dac)
    print("cleanup complited")