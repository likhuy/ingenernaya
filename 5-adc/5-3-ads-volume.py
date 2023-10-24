import RPi.GPIO as GPIO
import time

dac=[8,11,7,1,0,5,12,6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 13
comparator = 14


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule , GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def dec2bin(decimal):
    decimal=bin(decimal)[2:]
    decimal = '1' * len(decimal)
    return [int(elem) for elem in decimal.zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    mediate = 0
    for i in range(7, -1, -1):
        value= 2**i+mediate
        signal = dec2bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        comparatorValue = GPIO.input(comparator)
        if comparatorValue == 0:
            mediate+=2**i
    return mediate



try:
    while True:
        value = adc()
        if type(value) == int:
            voltage = value / levels * maxVoltage
            print("Digital = ", value, "Voltage = ", voltage)
            GPIO.output(leds, dec2bin(int(value)))
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