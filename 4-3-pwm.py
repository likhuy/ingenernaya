import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)


try:
    while true:
        x = int(input("Введите число от 0 до 100: "))
        if x>100:
            print('Слишком большое значение.')
        else:
            p = GPIO.PWM(24, 1000)
            p.start(x)
            print('Предполагаемое напряжение ',3.3*x/100)
            input("Enter чтобы завершить: ")
            p.stop()
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()