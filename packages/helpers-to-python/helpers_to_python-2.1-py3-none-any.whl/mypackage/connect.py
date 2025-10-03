import logging
import socket
import colorama

def connect(host, MessageConnect, TEST):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, 80))
    print(MessageConnect)
    if TEST == 'TEST':
        print(colorama.Fore.RED + 'тестовая версия подключения запущена!')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, 80))
        print('тестовая версия подключения выключена подключение хорошее')
        exit(TEST)
    if TEST == 'NOTEST':
        print('подключено!\n')
    if TEST != 'NOTEST':
        print(colorama.Fore.RED + 'введите корректное значение!')
        exit('error')
    return s

def unconnect(MessageUnconnect):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()
    print(colorama.Fore.RED + MessageUnconnect)

def send(MessageSend, HostToSend, accepct):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostToSend, 8080))
    s.send(MessageSend.encode('utf-8'))
    if accepct == 'ACCEPCT':
        response = s.recv(1024).decode('utf-8')
        print(f"in accepct: \n{response}\b")
    if accepct == 'NO':
        print(colorama.Fore.RED + 'не сформулирован запрос на получение данных из-за отказа получения\n')