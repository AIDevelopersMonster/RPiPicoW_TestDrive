# Video https://youtu.be/fqqyaIz4dtU
# Post http://kontakts.ru/showthread.php/40902?p=86265#post86265
# Telega https://t.me/MrMicroPython

import network
import time

wifi_config = {
    'ssid': 'your-ssid',
    'password': 'your-password'
}

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    # Получаем данные о Wi-Fi из config.py
    ssid = wifi_config['ssid']
    password = wifi_config['password']
    
    if not wlan.isconnected():
        print('Подключение к сети Wi-Fi...')
        wlan.connect(ssid, password)
        
        while not wlan.isconnected():
            time.sleep(1)  # Ждём подключения
            print("Ожидаем подключения...")
    
    print('Подключено к Wi-Fi:', wlan.ifconfig())
    return wlan

wlan =  connect_wifi()
