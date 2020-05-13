import os
import time
import configparser

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
4) Установка бота в Termux.
5) Инструкция по установке.
Other:
a) Установка BotToken и TelegramID''')
	setinstall = input('Выберите: ')
	if setinstall == '1':
		print('\nПолная установка бота.\n')
		os.system('mkdir Logs')
		print('\nПапка с логами создана.\n')
		os.system('chmod +x bot.py')
		os.system('mkdir Other')
		print('\nПапка Other создана\n')
		os.system('touch Other/base.txt Other/links.txt Other/idlist.txt Other/friends.txt')
		os.system('mkdir Config')
		print('\nПапка Config создана\n')
		print('\nВсе зависимости установлены.\n')
		os.system('sudo apt install screen python3-pip -y')
		print('\nScreen и python3-pip установлен.\n')
		os.system('pip3 install pyTelegramBotAPI')
		print('\nМодуль pyTelegramBotAPI установлен\n.')
		os.system('pip3 install configparser')
		print('\nConfigParser установлен!\n')
		os.system('mkdir Config')
		print('\nПапка с конфигами создана!\n')
		tokenfilev = input('Введите свой токен бота: ')
		print('\nТокен установлен!\n')
		adminfile = input('Введите свой TelegramID: ')
		os.system('touch Config/config.ini')
		configfile = open('Config/config.ini', 'w+')
		configfile.write('''[Bot]
token=''' +str(tokenfilev)+ '''
adminid='''+str(adminfile))
		print('\nКонфиг файл создан и настроен!\n')
		os.system('screen python3 bot.py')
		print('\nБот успешно установлен!\nУдачного использования!')
	elif setinstall == '2':
		print('\nБазовая установка бота.\n')
		os.system('mkdir Logs')
		print('\nПапка с логами создана.\n')
		os.system('mkdir Other')
		print('\nПапка Other создана\n')
		os.system('touch Other/base.txt Other/links.txt Other/idlist.txt Other/friends.txt')
		os.system('mkdir Config')
		print('\nПапка Config создана\n')
		os.system('chmod +x bot.py')
		print('\nВсе зависимости установлены.\n')
		os.system('sudo apt install python3-pip')
		print('python3-pip установлен.\n')
		os.system('pip3 install pyTelegramBotAPI')
		print('\nМодуль pyTelegramBotAPI установлен.\n')
		os.system('pip3 install configparser')
		print('\nConfigParser установлен!\n')
		tokenfilev = input('Введите свой токен бота: ')
		print('\nТокен установлен!\n')
		adminfile = input('Введите свой TelegramID: ')
		os.system('touch Config/config.ini')
		configfile = open('Config/config.ini', 'w+')
		configfile.write('''[Bot]
token=''' +str(tokenfilev)+ '''
adminid='''+str(adminfile))
		print('\nКонфиг файл создан и настроен!\n')
		print('\nЧтобы запустить бота напишите python3 bot.py')
	elif setinstall == '3':
		print('Запуск бота....')
		time.sleep(2)
		os.system('screen python3 bot.py')
		print('\n!!!!!Если бот упал - надо создать папку Logs.\nЕсли все еще падает - сделайте полную установку выбрав пункт 1. !!!!!')
	elif setinstall == '4':
		print('Установка бота на Termux...')
		time.sleep(2)
		os.system('pkg update')
		os.system('apt update && apt upgrade')
		os.system('pkg install nano python -y')
		os.system('pip3 install pyTelegramBotAPI')
		os.system('cd WBot-TelegramBot')
		os.system('chmod +x bot.py')
		os.system('mkdir Logs')
		print('\n \n Усстановка завершена! Для запуска напишите python3 bot.py !\n')



	elif setinstall == '5':
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
2) sudo sudo apt install python git nano -y
3) sudo sudo apt install python3-pip -y
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
	elif setinstall == 'a':
		tokenfilev = input('Введите свой токен бота: ')
		print('\nТокен установлен!\n')
		adminfile = input('Введите свой TelegramID: ')
		os.system('touch Config/config.ini')
		configfile = open('Config/config.ini', 'w+')
		configfile.write('''[Bot]
token=''' +str(tokenfilev)+ '''
adminid='''+str(adminfile))
		configfile.close()
		print('Конфиг файл создан и настроен!')
startinstall()