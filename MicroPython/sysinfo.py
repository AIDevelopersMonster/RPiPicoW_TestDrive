# Video https://youtu.be/I917spS4878
# http://kontakts.ru/showthread.php/40899?p=86259#post86259
import machine
import time
import os
import sys
import gc
from machine import ADC, Pin
print(f"Hello user!")
print(f"============")
# Информация о системе
print("System Info os.uname():")
print(f"============")
sys_info = os.uname()
print(f"OS: {sys_info.sysname}")
print(f"Machine: {sys_info.machine}")
print(f"Release: {sys_info.release}")
print(f"Version: {sys_info.version}")
print(f"Node Name: {sys_info.nodename}")
print(f"Python version: {sys.version}\n")
# Получаем информацию о реализации интерпретатора
implementation_info = sys.implementation
# Печатаем информацию
print("System Info sys.implementation:")
print(f"============")
print("Interpreter Name:", implementation_info.name)  # 'micropython'
print("Version:", ".".join(map(str, implementation_info.version[:3])))  # '1.24.1'
print("Machine Description:", implementation_info._machine)  # 'Raspberry Pi Pico W with RP2040'
print("MPY Version:", implementation_info._mpy)  # '4870'
print(f"============")
# Память
gc.collect()
print("Memory Info:")
print(f"============")
print(f"Free memory: {gc.mem_free()} bytes")
print(f"Total memory: {gc.mem_alloc() + gc.mem_free()} bytes\n")
print(f"============")
# Информация о чипе
chip_id = machine.unique_id()
print(f"Chip ID: {chip_id.hex()}")
print(f"============")
# Чтение температуры с встроенного датчика на RP2040
# Встроенный датчик температуры подключен к ADC4
sensor_temp = ADC(4)  # Встроенный датчик температуры на ADC4
conversion_factor = 3.3 / (65535)  # Преобразователь, чтобы привести значение ADC к реальному напряжению

# Считывание данных с датчика температуры и расчет реальной температуры
reading = sensor_temp.read_u16() * conversion_factor  # Считывание значения с датчика и преобразование
temperature = 27 - (reading - 0.706) / 0.001721  # Преобразование показаний в температуру (формула для RP2040)
print("CPU Temperature: %.2f C" % temperature)
print(f"            ")
print(f"============")

# Проверка, если это Raspberry Pi Pico W
# Проверяем, является ли устройство Raspberry Pi Pico W с чипом RP2040
if implementation_info._machine == 'Raspberry Pi Pico W with RP2040':
    # Настроим пин GPIO для светодиода (например, GP15)
    led = machine.Pin(15, machine.Pin.OUT)
    
    # Включим светодиод
    led.value(1)  # Включение (1) или выключение (0) светодиода
else:
    # В случае, если это не Raspberry Pi Pico W, выключаем светодиод
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(0)  # Выключаем светодиод