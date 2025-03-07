# Video https://youtu.be/EC6h8g2WtJ8
# Post http://kontakts.ru/showthread.php/40902?p=86265#post86265
# Telega https://t.me/MrMicroPython
#

import wifi_init
import socket
from machine import Pin

# Инициализация встроенного светодиода
led = Pin("LED", Pin.OUT)

# Подключаемся к Wi-Fi
wlan = wifi_init.connect_wifi()

# Настройка веб-сервера
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()

print("Сервер запущен, слушает по адресу", addr)

# Основной цикл обработки HTTP-запросов
while True:
    try:
        conn, addr = s.accept()
        print("Новое подключение от", addr)

        # Читаем запрос
        request = conn.recv(1024).decode()
        print("Запрос:", request)

        # Обрабатываем команды
        if "/lighton" in request:
            led.value(1)
        elif "/lightoff" in request:
            led.value(0)

        # Формируем HTML-страницу
        response = """\
HTTP/1.0 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Pico Web Server</title>
</head>
<body>
    <h1>LED Control</h1>
    <form action="/lighton">
        <button>Turn On</button>
    </form>
    <br>
    <form action="/lightoff">
        <button>Turn Off</button>
    </form>
</body>
</html>
"""
        conn.sendall(response.encode())
        conn.close()

    except OSError:
        conn.close()
        print("Соединение закрыто")

