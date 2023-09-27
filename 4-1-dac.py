import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac=[1,1,2]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    n=int(bin(n)[2::])
    if n>=100000000:
        n=str(n)[-8::]
    elif n<10000000:
        n='0'*(8-len(str(n)))+str(n)
    return n

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




GPIO.output(23, 0)
GPIO.output(23, 1)
