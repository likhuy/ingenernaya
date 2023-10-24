import RPi.GPIO as GPIO
import time

dac=[8,11,7,1,0,5,12,6]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 13
comporator = 14


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule , GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comporator, GPIO.IN)

def dec2bin(decimal):
    return [int(elem) for elem in bin(decimal)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal


try:
    while True:
        for value in range(256):
            time.sleep(0.01)
            signal = num2dac(value)
            voltage = value / levels * maxVoltage
            comparatorValue = GPIO.input(comporator)
            if comparatorValue == 0:
                print("ADC value = ",value ," -> ",signal , ". input valtage = ", voltage)

except KeyboardInterrupt:
    print('\nThe program was stoped by keyboard')
else:
    print('No exceptions')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)