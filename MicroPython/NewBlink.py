# Video https://youtu.be/mq8XYwWEfO8
# Post http://kontakts.ru/showthread.php/40902?p=86264#post86264
# Telega https://t.me/MrMicroPython
# Импорт только нужных частей
from machine import Pin
from time import sleep

# Доступные пины (можно поменять под свою схему)
available_pins = [0,1,2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19]

# Выбор GPIO
while True:
    try:
        pin_num = int(input(f"Выберите GPIO из списка {available_pins}: "))
        if pin_num in available_pins:
            break
        else:
            print("Ошибка: Выбранный пин недоступен. Попробуйте снова.")
    except ValueError:
        print("Ошибка: Введите целое число.")

# Создаём объект для управления светодиодом
led = Pin(pin_num, Pin.OUT)

# Выбор времени задержки
while True:
    try:
        delay = float(input("Введите задержку мигания (от 0.5 до 10 сек): "))
        if 0.5 <= delay <= 10:
            break
        else:
            print("Ошибка: Введите число в диапазоне от 0.5 до 10 секунд.")
    except ValueError:
        print("Ошибка: Введите число.")

print(f"Светодиод на GPIO{pin_num} будет мигать с задержкой {delay} секунд.")

# Основной цикл мигания
try:
    while True:
        led.value(1)  # Включить светодиод
        sleep(delay)
        led.value(0)  # Выключить
        sleep(delay)
except KeyboardInterrupt:
    print("\nВыход из программы.")
