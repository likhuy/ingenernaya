import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(21, 20,16, 12, 17, 8, 25, GPIO.OUT, initial=1)# другие будут гореть как обычно

p = GPIO.PWM(24, 0.5)# второе значение это частота
p.start(50)# коэфицент сколько процентов от времени будет гореть
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()

# в 3 задании нужно будет подключить измерение нарпяжения к конденсатору и можно будет задавать на нем напряжение при
# большой частоте 1000 (если частота будет не большой 50 то конденсатор будет разряжаться)
# при изменении коэфицента можно будет регулировать напряжение (будет проценты*3.3
#https://ant-lab.mipt.ru/education/get/get-students/-/blob/master/4-dac/dac.md?ref_type=heads#%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0-3-%D1%88%D0%B8%D0%BC
#https://ant-lab.mipt.ru/education/get/get-students/-/blob/master/3-git/git.md?ref_type=heads#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-git
