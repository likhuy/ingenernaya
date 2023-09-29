import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    
    return [int(elem) for elem in bin(n)[2:].zfill(8)]


try:
    t = int(input("введите период: "))
    n_t = int(input("введите число периодов: "))
    i = 0
    for j in range(n_t):
        while i < 255:
            GPIO.output(dac, dec2bin(int(i)))
            print(3.3 / 256 * int(i), " B")
            i += 1
            sleep(t/500)
        while i > 0:
            GPIO.output(dac, dec2bin(int(i)))
            print(3.3 / 256 * int(i), " B")
            i -= 1
            sleep(t/500)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()







