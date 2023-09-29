import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    
    return [int(elem) for elem in bin(n)[2:].zfill(8)]

try:
    while True:
        x = input('Введите число от 0 до 255:')
        if x == 'q':
            break
        elif int(x)>255:
            print('Вы ввели число больше допустимого')
        else:
            x = int(x)
            GPIO.output(dac, dec2bin(x))
            print((3.3 / 256) * x, "B")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
