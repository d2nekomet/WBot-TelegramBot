#Channel: t.me/www_project 
#Coder: t.me/os_people
#Emoji ➡⬅🔃💻📷📸📹🎥📽💡💣🧱📁📂🗂🔍🔎🔏🔐🔒🔓❤️🧡💛💚💙💜🖤☢️☣️📴📳🆔✉️📩📨📧💌📱📲💻⌨️🖥🖨

import time
import os
import telebot
from telebot import *
import logging
import threading
import configparser
from subprocess import check_output

logs = open('Logs/log' + time.strftime('%B%d%Y', time.localtime()) + '.txt', 'w+')
logs.close()
logs = open('Logs/log' + time.strftime('%B%d%Y', time.localtime()) + '.txt', 'a+')
idslist = open('Other/idlist.txt', 'w+')

conf = configparser.RawConfigParser()
conf.read("Config/config.ini")
print('Ваш токен: '+conf.get("Bot", "token"))
print('Ваш id: '+conf.get("Bot", "adminid"))
TOKEN = conf.get("Bot", "token")
adminid = int(conf.get("Bot", "adminid"))
idslist = open('Other/idlist.txt', 'w+')

bot = telebot.TeleBot(TOKEN)

def friend_base(message):
	global friendbase
	friendbase = open('Other/friends.txt','a+')
	friendbase.write(message.text + '\n')
	friendbase.close()                           #это обновление списка баз данных
	friendbase = open('Other/friends.txt','r')
	bot.send_message(message.chat.id, 'Список друзей обновлен!\nВот он: \n' + friendbase.read())
	friendbase.close()

def url_links(message):
	links = open('Other/links.txt','w+')
	links.write(message.text + '\n')
	links.close()
	links = open('Other/links.txt','r')
	bot.send_message(message.chat.id, 'Список софта обновлен!\nВот он: \n' + links.read())
	links.close()

def url_base(message):
	base = open('Other/base.txt','w+')
	base.write(message.text + '\n')
	base.close()
	base = open('Other/base.txt','r')
	bot.send_message(message.chat.id, 'Список баз данных обновлен!\nВот он: \n' + base.read())
	base.close()

blockdbname = ['qwerty','qwert','qwer','123456','1234','1234567890','123456654321','12345678900987654321','qwertyuiop','qwertyui','qwaszx','artem','nikita','anton','andrei','lox','adminlox','1234','12345','katya','sasha','putin','sotka']

def dbupl(message):
	global logs, dbl
	if os.path.exists('Logs/' + str(message.text)) == True:
		logs.close()
		dbl = open('Logs/' + str(message.text), 'r')
		bot.send_message(message.chat.id, '📁Отправляю файл!📁\n📁Имя файла: Logs/' + str(message.text) + ' 📁')
		bot.send_document(adminid, dbl)
		dbl.close()
		logs = open('Logs/log' + time.strftime('%B%d%Y', time.localtime()) + '.txt', 'w+')
	else:
		bot.send_message(adminid, 'Нет такого файла!\nПожалуйста, введите команду /dbupload с корректными данными!')




def restartlog():
	logs.close()
	logs = open('Logs/log' + time.strftime('%B%d%Y',time.localtime()) + '.txt', 'w+')
	logs.close()
	logs = open('Logs/log' + time.strftime('%B%d%Y', time.localtime()) + '.txt', 'a+')

def logres():
	while True:
		if time.strftime("%H:%M:%S") == '00:00:01':
			bot.send_message(adminid,'Логи обновлены!')
			restartlog()
			time.sleep(1)
	pass

def serachdb(message):
	if len(message.text) < 5 or message.text == 'qwerty' or message.text == 'qwert' or message.text == 'qwer' or message.text == '123456' or message.text == '1234' or message.text == '1234567890' or message.text == '123456654321' or message.text == '12345678900987654321' or message.text == 'qwertyuiop' or message.text == 'qwertyui' or message.text == 'qwaszx' or message.text == 'artem' or message.text == 'nikita' or message.text == 'anton' or message.text == 'andrei' or message.text == 'lox' or message.text == 'adminlox' or message.text == '1234' or message.text == '12345' or message.text == 'katya' or message.text == 'sasha' or message.text == 'putin' or message.text == 'sotka':
		bot.send_message(message.chat.id,'Попытка выгрузки базы? Пошел нахуй.')
		bot.send_message(adminid,'Тут этот хуй базу попытался выгрузить: \n' + 'Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n')
	else:
		dbpass = open('db.txt').readlines()
		for i in iter(dbpass):
			if message.text in i:
				listdb = '\n' + str(i) + '\n'
				bot.send_message(message.chat.id, '🔐Логин и пароль: \n' + listdb + '🔐')

def getpid():
	name = 'python3 bot.py'
	return map(int,check_output(["pidof",name]).split())
	pidid = map(int,check_output(["pidof",name]).split())
t = threading.Thread(target=logres, name='Thread1',)
t.start()


markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('💾Софт💾')
itembtn2 = types.KeyboardButton('🔒Базы🔒')
itembtn3 = types.KeyboardButton('✉️Чат✉️') # Это кнопки / Buttons
itembtn4 = types.KeyboardButton('😁Помощь😁')
itembtn4 = types.KeyboardButton('2>')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

markup2 = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('📊Статистика📊')
itembtn2 = types.KeyboardButton('🔎GitHub🔍')
itembtn3 = types.KeyboardButton('👨‍👩‍👧‍👦Друзья👨‍👩‍👧‍👦')
itembtn4 = types.KeyboardButton('💳Реквизиты💳') # Это кнопки / Buttons
itembtn5 = types.KeyboardButton('<1')
itembtn6 = types.KeyboardButton('3>')
markup2.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

markup3 = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('💩Админы💩')
itembtn2 = types.KeyboardButton('🔐MCPE DB🔐')
itembtn3 = types.KeyboardButton('<2')
markup3.add(itembtn1, itembtn2, itembtn3)

admmarkup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/addlink')
itembtn2 = types.KeyboardButton('/addbase')
itembtn3 = types.KeyboardButton('/dbupload')
itembtn4 = types.KeyboardButton('/addfriend')
itembtn5 = types.KeyboardButton('/logupload')
itembtn6 = types.KeyboardButton('Exit')
admmarkup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

@bot.message_handler(content_types=['text', '/start'])

def send_welcome(message):
	global logs, myString, idslist
	if message.text == '/start':
		idslist.write(str(message.chat.id) + '  @' + str(message.from_user.username) + '  ---->  ' + time.ctime() + '\n')
		bot.send_message(message.chat.id,"Привет!😀\nЯ бот канала @www_project .\nНапиши  /help чтобы узнать список команд.", reply_markup=markup)

	elif message.text == '😁Помощь😁' or message.text == '/help':
		bot.send_message(message.chat.id, '''Команды:
/chat- ✉️наш чат✉️
/soft - 💾список полезных программ и скриптов💾
/dblist - 🔒список баз данных🔒
/admin - 👦наш(и) - админ(ы)👦
/button - 🔃Перезагрузка кнопок🔃
/stat - 📊Статистика📊
/github - 🔎страница бота на GitHub🔍
/payments - 💳поддержка проекта монетой💳
/friends - 👨‍👩‍👧‍👦друзья проекта👨‍👩‍👧‍👦
/db - 🔐поиск пароля по нику MCPE🔐
''')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '✉️Чат✉️' or message.text == '/chat':
		bot.send_message(message.chat.id,"Наш чат: t.me/wproject_chat")
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '💾Софт💾' or message.text == '/soft':
		links2 = open('Other/links.txt','r')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.send_message(message.chat.id, '💾Список программ и ссылок на их: \n' + links2.read() + '\n💾')
		links2.close()

	elif message.text == '🔒Базы🔒'  or message.text == '/dblist':
		base2 = open('Other/base.txt','r')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.send_message(message.chat.id, '📁Список баз данных и ссылок на их: \n' + base2.read() + '\n📁')
		base2.close()

	elif message.text == '💩Админы💩' or message.text == '/admin':
		bot.send_message(message.chat.id, '👦Создатель проекта: @os_people')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '/button':
		bot.send_message(message.chat.id, '⌨️Кнопки установлены!⌨️', reply_markup=markup)
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '2>' or message.text == '<2':
		bot.send_message(message.chat.id, 'Страница №2', reply_markup=markup2)
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '<1':
		bot.send_message(message.chat.id, 'Страница №1', reply_markup=markup)
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '3>' or message.text == '<3':
		bot.send_message(message.chat.id, 'Страница №3', reply_markup=markup3)
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '/friends' or message.text == '👨‍👩‍👧‍👦Друзья👨‍👩‍👧‍👦':
		friendbase = open('Other/friends.txt','r')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.send_message(message.chat.id, 'Наши друзья: \n' + friendbase.read())
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

	elif message.text == '/stat' or message.text == '📊Статистика📊':
		idslist.close()
		idslist = open('Other/idlist.txt','r')
		with open('Other/idlist.txt') as idslist:
			size=sum(1 for _ in idslist)
			bot.send_message(message.chat.id, '📊Статистика отображается в реальном времени!📊\nПользователей🙎‍♂: '+ str(size))
			idslist.close()
			idslist = open('Other/idlist.txt','a')
			pass

	elif message.text == '🔎GitHub🔍' or  message.text == '/github':
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n')
		bot.send_message(message.chat.id, '🔎Страница бота на GitHub - https://github.com/d2nekomet/WBot-TelegramBot \n🔍')

	elif message.text == '/payments' or message.text == '💳Реквизиты💳':
		bot.send_message(message.chat.id, '''Привет. Всем надо зарабатывать и кушать. Админ этого бота и канала @www_project не исключение. Однако я не создаю приватные группы и т.д. Почему? Я считаю, что информация должна быть бесплатной!
Поэтому прошу помочь проекту рублем и украсить вечер админа порцией кексиков, ну или стену канала еще одним годным постом сделанным благодаря Вашим поддержкам!
Спасибо :)
Реквизиты:
Qiwi - https://qiwi.me/wwwproject
QiWi Карта - 4890494672490182
BTC - 1EwW7KwrEr5w2UXeCnJdJKAGPuWQPS1ZfV
Ethereum: 0xdb05ab0547e28f62ad0c7d856c0b9b4ed6d28789
Спасибо!❤️
''')
	elif message.text == '/db' or message.text == '🔐MCPE DB🔐':
		dbs = bot.send_message(message.chat.id, 'Введите никнейм:')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.register_next_step_handler(dbs, serachdb)

	elif message.text == '/addlink' and message.chat.id == adminid:
		l = bot.send_message(message.chat.id, 'Введите <имя файла> <ссылку на файл>:')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.register_next_step_handler(l, url_links)

	elif message.text == '/addbase' and message.chat.id == adminid:
		b = bot.send_message(message.chat.id, 'Введите <имя базы> <ссылку на базу>:')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.register_next_step_handler(b, url_base)

	elif message.text == '/addfriend' and message.chat.id == adminid:
		fr = bot.send_message(message.chat.id, 'Введите то, что надо ввести чтобы добавить друзей в список:')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.register_next_step_handler(fr, friend_base)

	elif message.text == '/dbupload' and message.chat.id == adminid:
		myDBList = os.listdir(path="Logs/")
		myDBString = '	,	'.join(myDBList)
		db = bot.send_message(message.chat.id, 'Выберите базу которую хотите скачать (напишите имя файла): \n' + myDBString)
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.register_next_step_handler(db, dbupl)

	elif message.text == '/adminka' and message.chat.id == adminid:
		bot.send_message(adminid,"Админ панель открыта!", reply_markup=admmarkup)

	elif message.text == 'Exit' and message.chat.id == adminid:
		bot.send_message(adminid, 'Вы вышли из админ панели!', reply_markup=markup)

	elif message.text == '/logupload' and message.chat.id == adminid:
		logfile = open('sample.log', 'r')
		bot.send_message(adminid, 'Отправляю Log файл!')
		bot.send_document(adminid, logfile)
		logfile.close()
		logstart()
	else:
		bot.send_message(message.chat.id, 'Нет такой команды!\nДля получения списка команд введите /help')

	msg = message.text.split()
	if msg[0] == '/send':
		myList = msg[2:]
		myString = '	'.join(myList)
		bot.send_message(chat_id=msg[1],text= '📩Вам сообщения от админа: ' + str(myString))
		bot.send_message(adminid, '✉️Соощение пользователю ' + msg[1] + ' отправлено успешно!\n✉️Текст сообщения: ' + str(myString) + ' ✉️')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
	msg = message.text.split()


def logstart():
	logging.basicConfig(filename="sample.log", level=logging.DEBUG)
	logging.debug("\nDebug: \n" + time.ctime() + '\n')
	logging.info("\nInformational: \n" + time.ctime()+ '\n')
	logging.error("\n!!!ERROR!!!: \n" + time.ctime()+ '\n')
logstart()
bot.polling(none_stop=True)
