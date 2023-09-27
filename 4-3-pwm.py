import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)


try:
    while true:
        x = int(input("Введите число от 0 до 100: "))
        p = GPIO.PWM(24, 1000)
        p.start(x)
        input("Enter чтобы завершить: ")
        p.stop()
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()