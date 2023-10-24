import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

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


def dec2bin(decimal):
    return [int(elem) for elem in bin(decimal)[2:].zfill(8)]


# изменение напряжения на тройка модуля
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

#вывод
def leds_out(out_value):
    GPIO.output(leds, dec2bin(out_value))
    return 0



try:
    memory = [] # переменная для записи результатов напряжения на конденсаторе
    time_start = time.time()
    # Начало измерения напряжения на повышении
    GPIO.output(troykaModule, 1)
    while True:
        value = adc()
        voltage = value / levels * maxVoltage
        print("Digital = ", value, "Voltage = ", voltage)
        memory.append(voltage)
        if value/levels > 0.80:
            break
    # Меняем выход тройка модуля на 0 и продолжаеем измерения
    GPIO.output(troykaModule, 0)
    while True:
        
        value = adc()
        voltage = value / levels * maxVoltage
        print("Digital = ", value, "Voltage = ", voltage)
        memory.append(voltage)
        if value / levels < 0.1:
            break
        if memory[-10 : -1: 1] == [voltage for i in range(9)]:
            break
    # Измерение времени
    time_finish = time.time()
    time_work = time_finish-time_start

    # Рисуем график
    plt.plot(memory)
    # plt.show()

    #запись в файл значений
    memory_str = [str(item) for item in memory]
    with open("data_1.txt", "w") as outfile:
        outfile.write("\n".join(memory_str))
    #Запись в файл данные измерения
    settings_str = ["Частота дискретизации: "+str(time_work/490) , "Шаг квантования: "+str(maxVoltage/levels)]
    with open("settings_1.txt", "w") as file:
        file.write("\n".join(settings_str))

    # Вывод в терминал
    print("Продолжительность эксперимента: " + str(time_work))
    print("Период одного измерения: " + str(time_work/490))#?
    print("Частота дискретизации: " + str(time_work / 490))
    print("Шаг квантования: "+str(maxVoltage/levels))


except KeyboardInterrupt:
    print('\nThe program was stoped by keyboard')
else:
    print('No exceptions')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troykaModule, GPIO.LOW)
    GPIO.cleanup(dac)
    print("cleanup complited")