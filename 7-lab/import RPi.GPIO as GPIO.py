import RPi.GPIO as GPIO

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
GPIO.setup(troykaModule , GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

GPIO.output(dac, GPIO.LOW)
GPIO.output(troykaModule, GPIO.LOW)
GPIO.cleanup(dac)
print("cleanup complited")