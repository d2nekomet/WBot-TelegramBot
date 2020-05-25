import os
import time
import logging


def startinstall():
	os.system('clear')
	print('''
──────╔═══╗╔═══╗╔═══╗──╔╗╔═══╗╔═══╗╔════╗
──────║╔═╗║║╔═╗║║╔═╗║──║║║╔══╝║╔═╗║║╔╗╔╗║
╔╗╔╗╔╗║╚═╝║║╚═╝║║║─║║──║║║╚══╗║║─╚╝╚╝║║╚╝
║╚╝╚╝║║╔══╝║╔╗╔╝║║─║║╔╗║║║╔══╝║║─╔╗──║║──
╚╗╔╗╔╝║║───║║║╚╗║╚═╝║║╚╝║║╚══╗║╚═╝║──║║──
─╚╝╚╝─╚╝───╚╝╚═╝╚═══╝╚══╝╚═══╝╚═══╝──╚╝──
Project: https://t.me/www_project
Author: https://t.me/os_people\n''')
	time.sleep(1)
	print('''Выберите нужный вариант:
1) Full Install - устанавливает все либы и зависимости + запуск бота
2) Standart install - устанавливает все либы и зависимости
3) Termux install - установка для Termux
Other:
a) Full config - Установка BotToken, AdminTelegramID и имя канала (Пример - @www_project)
b) Token Config - установка BotToken
c) Id Config - установка TelegramID
d) Channel Config - установка имени канала
f) MCPEDataBase - скачивание (по прямой сссылке) базы данных
Update:
u1) Module Update - обновление модулей''')
	select = input('Выберите нужный вариант: ')
	if select == '1':
		os.system('clear')
		print('\nУстановка началась! \n')
		time.sleep(0.5)
		os.system('mkdir Config Logs Other')
		os.system('sudo apt install python3-pip screen -y')
		os.system('pip3 install pyTelegramBotAPI configparser')
		os.system('touch Config/config.ini')
		os.system('touch Other/base.txt/ Other/friends.txt/ Other/links.txt/')
		configFile = open('Config/config.ini', 'w+')
		botToken = input('Введите токен бота: ')
		adminId = input('Введите id админа бота: ')
		botChannel = input('Введите имя канала(пример - @www_project): ')
		configFile.write('''[Bot]
token=''' +str(botToken)+ '''
adminid='''+str(adminId)+ '''
chbot=''' + str(botChannel))
		configFile.close()
		os.system('clear')
		print('Запуск бота через 3 секунды...')
		print('\n3')
		time.sleep(1)
		print('\n2')
		time.sleep(1)
		print('\n1')
		print('\nЗапуск...')
		time.sleep(1)
		os.system('screen python3 bot.py')

	elif select == '2':
		os.system('clear')
		print('\nУстановка началась! \n')
		time.sleep(0.5)
		os.system('mkdir Config Logs Other')
		os.system('sudo apt install python3-pip screen -y')
		os.system('pip3 install pyTelegramBotAPI configparser')
		os.system('touch Config/config.ini')
		os.system('touch Other/base.txt/ Other/friends.txt/ Other/links.txt/')
		configFile = open('Config/config.ini', 'w+')
		botToken = input('Введите токен бота: ')
		adminId = input('Введите id админа бота: ')
		botChannel = input('Введите имя канала(пример - @www_project): ')
		configFile.write('''[Bot]
token=''' +str(botToken)+ '''
adminid='''+str(adminId)+ '''
chbot=''' + str(botChannel))
		configFile.close()
		os.system('clear')
		print('Бот установлен!')

	elif select == '3':
		os.system('clear')
		print('Установка началась!')
		os.system('mkdir Config Logs Other')
		os.system('pkg install screen -y')
		os.system('pip3 install pyTelegramBotAPI configparser')
		os.system('touch Config/config.ini')
		os.system('touch Other/base.txt/ Other/friends.txt/ Other/links.txt/')
		configFile = open('Config/config.ini', 'w+')
		botToken = input('Введите токен бота: ')
		adminId = input('Введите id админа бота: ')
		botChannel = input('Введите имя канала(пример - @www_project): ')
		configFile.write('''[Bot]
token=''' +str(botToken)+ '''
adminid='''+str(adminId)+ '''
chbot=''' + str(botChannel))
		configFile.close()
		os.system('clear')
		print('Бот установлен!')

	elif select == 'a':
		configFile = open('Config/config.ini', 'w+')
		botToken = input('Введите токен бота: ')
		adminId = input('Введите id админа бота: ')
		botChannel = input('Введите имя канала(пример - @www_project): ')
		configFile.write('''[Bot]
token=''' +str(botToken)+ '''
adminid='''+str(adminId)+ '''
chbot=''' + str(botChannel))
		configFile.close()
		os.system('clear')
		print('Сконфигурировал!')

	elif select == 'b':
		botTokenFile = open('Config/config.ini', 'r+')
		botTokenLine = botTokenFile.readlines()
		token = botTokenLine[2]
		chbotLine = botTokenLine[3]
		botTokenFile.close()
		botTokenFile = open('Config/config.ini', 'w+')
		botToken = input('Введите токен бота: ')
		botTokenFile.write('''[Bot]
token=''' +str(botToken)+'\n'+str(token)+ str(chbotLine))
		print('''Вот конфиг: [Bot]
token=''' +str(botToken)+'\n'+str(token)+ str(chbotLine))
		botTokenFile.close()

	elif select == 'c':
		adminIdFile = open('Config/config.ini', 'r')
		adminIdLine = adminIdFile.readlines()
		token = adminIdLine[1]
		chbot = adminIdLine[3]
		adminIdFile.close()
		adminIdFile = open('Config/config.ini', 'w+')
		teleIDLine = input('Введи свой TelegramID: ')
		adminIdFile.write('''[Bot]
''' + token + 'adminid='+ teleIDLine + '\n' + chbot)
		print('''[Bot]
''' + token + 'adminid='+ teleIDLine + '\n' + chbot)
		adminIdFile.close()

	elif select == 'd':
		channelFile = open('Config/config.ini', 'r')
		channelLine = channelFile.readlines()
		token = channelLine[1]
		adminid = channelLine[2]
		channelFile.close()
		channelFile = open('Config/config.ini', 'w+')
		chIdLine = input('Введи свой канал (Пример: @www_project): ')
		channelFile.write('''[Bot]
''' + token + adminid + 'chbot=' + chIdLine)
		print('''\n[Bot]
''' + token + adminid + 'chbot=' + chIdLine)
		channelFile.close()	

	elif select == 'f':
		dataBaseDownload = input('Введите прямую ссылку на базу: ')
		os.system('wget ' + dataBaseDownload)
		os.system('clear')
		print('\n\nНе забудьте переименовать базу в db.txt!!!')

	elif select == 'u1':
		os.system('clear')
		os.system('sudo apt install python3-pip screen -y')
		os.system('pip3 install pyTelegramBotAPI configparser')

startinstall()
