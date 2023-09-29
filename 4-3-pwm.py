import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)


try:
    while True:
        x = input("Введите число от 0 до 100: ")
        if x=='q':
            break
        elif int(x)>100:
            print('Слишком большое значение.')
        
        else:
            p = GPIO.PWM(19, 1000)
            p.start(int(x))
            print('Предполагаемое напряжение ',3.3*int(x)/100)
            input("Enter чтобы завершить: ")
            p.stop()
finally:
    GPIO.output(19, 0)
    GPIO.cleanup()