import os
import time
def startinstall():
	print('''
──────╔═══╗╔═══╗╔═══╗──╔╗╔═══╗╔═══╗╔════╗
──────║╔═╗║║╔═╗║║╔═╗║──║║║╔══╝║╔═╗║║╔╗╔╗║
╔╗╔╗╔╗║╚═╝║║╚═╝║║║─║║──║║║╚══╗║║─╚╝╚╝║║╚╝
║╚╝╚╝║║╔══╝║╔╗╔╝║║─║║╔╗║║║╔══╝║║─╔╗──║║──
╚╗╔╗╔╝║║───║║║╚╗║╚═╝║║╚╝║║╚══╗║╚═╝║──║║──
─╚╝╚╝─╚╝───╚╝╚═╝╚═══╝╚══╝╚═══╝╚═══╝──╚╝── 
Project: https://t.me/www_project
Author: https://t.me/os_people\n''')
	print('''Выберите нужную цифру:
1) Полная автоматическая установка (Для Debian и Ubuntu based дистрибутивов)
2) Базовая установка (без запуска бота)
3) Запуск бота в фоне.
4) Инструкция по установке.''')
	setinstall = input('Выберите: ')
	if setinstall == '1':
		print('Полная установка бота.\n')
		os.system('mkdir Logs')
		print('Папка с логами создана.\n')
		os.system('chmod +x bot.py')
		print('Все зависимости установлены.\n')
		os.system('sudo apt install screen python3-pip -y')
		print('Screen и python3-pip утсановлены.\n')
		os.system('pip3 install pyTelegramBotAPI')
		print('Модуль pyTelegramBotAPI установлен\n.')
		os.system('screen python3 bot.py')
		print('Бот успешно установлен!\nУдачного использования!')
	elif setinstall == '2':
		print('Базовая установка бота.\n')
		os.system('mkdir Logs')
		print('Папка с логами создана.\n')
		os.system('chmod +x bot.py')
		print('Все зависимости установлены.\n')
		os.system('sudo apt install python3-pip')
		print('python3-pip установлен.\n')
		os.system('pip3 install pyTelegramBotAPI')
		print('Модуль pyTelegramBotAPI установлен.\n')
		print('Чтобы запустить бота напишите python3 bot.py')
	elif setinstall == '3':
		print('Запуск бота....')
		time.sleep(2)
		os.system('screen python3 bot.py')
		print('\n!!!!!Если бот упал - надо создать папку Logs.\nЕсли все еще падает - сделайте полную установку выбрав пункт 1. !!!!!')
	elif setinstall == '4':
		print('''Привет! Ты выбрал режим ручной установки бота WBot для телеграм.
Открой второе окно терминала и делай все по инструкции! 
Удачи)

Для Termux:
1) pkg update
2) apt update && apt upgrade
3) pkg install python nano git -y
4) pip3 install pyTelegramBotAPI
5) cd WBot-TelegramBot
6) chmod +x bot.py
7) mkdir Logs
8) python3 bot.py

Для Ubuntu/Debian:
1) sudo apt update && sudo apt upgrade
2) sudo apt install python git nano -y
3) sudo apt install python3-pip -y
4) pip3 instal pyTelegramBotAPI
5) chmod +x bot.py
6) mkdir Logs
7) python3 bot.py

Для ArchLinux
1) sudo pacman -y
2) sudo pacman -S python git nano
3) sudo pacman -S python3-pip
4) pip3 install pyTelegramBotAPI
5) cd WBot-TelegramBot
6) chmod +x bot.py
7) mkdir Logs
8) python3 bot.py

Вот и все!''')
startinstall()