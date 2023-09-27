import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
dac=[]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    n=int(bin(n)[2::])
    if n>=100000000:
        n=str(n)[-8::]
    elif n<10000000:
        n='0'*(8-len(str(n)))+str(n)
    return n


try:
    t = int(input("введите период: "))
    n_t = int(input("введите число периодов: "))
    i = 0
    for j in range(n_t):
        while i < 255:
            GPIO.output(dac, dec2bin(int(i)))
            print(3.3 / 256 * int(i), " B")
            i += 1
            sleep(t)
        while i > 0:
            GPIO.output(dac, dec2bin(int(i)))
            print(3.3 / 256 * int(i), " B")
            i -= 1
            sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()




GPIO.output(23, 0)
GPIO.output(23, 1)



