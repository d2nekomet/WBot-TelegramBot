#Бот канала t.me/www_project 
#Написан t.me/os_people
#Emoji for message      	➡	⬅🔃  💻📷 📸 📹 🎥 📽💡💣🧱📁 📂 🗂🔍 🔎 🔏 🔐 🔒 🔓❤️ 🧡 💛 💚 💙 💜 🖤☢️ ☣️ 📴 📳🆔  ✉️ 📩 📨 📧 💌  📱 📲 💻 ⌨️ 🖥 🖨
##########################
import time
import os
import telebot
import logging               # Модули для работы бота 
from telebot import types
##########################
logs = open('Logs/log' + time.strftime('%B%d%Y', time.localtime()) + '.txt', 'w+')
logs.close()                                         #создание файла логов
logs = open('Logs/log' + time.strftime('%B%d%Y', time.localtime()) + '.txt', 'a+')

idslist = open('idlist.txt', 'a+')

tokenfile = open('Config/token.txt', 'r')
TOKEN = tokenfile.read()

adminidf = open('Config/adminid.txt', 'r')
adminidr = adminidf.read()
print('Ваш TelegramID: ' + adminidr + '\nВаш токен бота: ' + TOKEN)

idslist = open('idlist.txt', 'a+')
bot = telebot.TeleBot(TOKEN) # TOKEN 
adminid = int(adminidr)# TelegramID админа
####################
def url_links(message):
	links = open('links.txt','a+')
	links.write(message.text + '\n')
	links.close()                           # это у нас функция обновления списка хоста.
	links = open('links.txt','r')
	bot.send_message(message.chat.id, 'Список софта обновлен!\nВот он: \n' + links.read())
	links.close()

def url_base(message):
	base = open('base.txt','a+')
	base.write(message.text + '\n')
	base.close()                           #это обновление списка баз данных
	base = open('base.txt','r')
	bot.send_message(message.chat.id, 'Список баз данных обновлен!\nВот он: \n' + base.read())
	base.close()
def friend_base(message):
	global friendbase
	friendbase = open('friends.txt','a+')
	friendbase.write(message.text + '\n')
	friendbase.close()                           #это обновление списка баз данных
	friendbase = open('friends.txt','r')
	bot.send_message(message.chat.id, 'Список друзей обновлен!\nВот он: \n' + friendbase.read())
	friendbase.close()

def dbupl(message):
	global logs, dbl
	logs.close()
	bot.send_message(message.chat.id, '📁Отправляю файл!📁\n📁Имя файла: Logs/' + str(message.text) + ' 📁')
	dbl = open('Logs/' + str(message.text), 'rb')
	bot.send_document(adminid, dbl)       # это дампит логи
	dbl.close()
	logs = open('Logs/log' + time.strftime('%B%d%Y', time.localtime()) + '.txt', 'a+')

##################
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('💾Софт💾')
itembtn2 = types.KeyboardButton('🔒Базы🔒')
itembtn3 = types.KeyboardButton('💩Админы💩') # Это кнопки / Buttons
itembtn4 = types.KeyboardButton('😁Помощь😁')
itembtn4 = types.KeyboardButton('2>')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

markup2 = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('📊Статистика📊')
itembtn2 = types.KeyboardButton('🔎GitHub🔍')
itembtn3 = types.KeyboardButton('👨‍👩‍👧‍👦Друзья👨‍👩‍👧‍👦')
itembtn4 = types.KeyboardButton('💳Реквизиты💳') # Это кнопки / Buttons
itembtn5 = types.KeyboardButton('3>')
itembtn6 = types.KeyboardButton('<1')
markup2.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

markup3 = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Not found')  # Это кнопки / Buttons
itembtn2 = types.KeyboardButton('<2')
markup3.add(itembtn1, itembtn2)

admmarkup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/addlink')
itembtn2 = types.KeyboardButton('/addbase')
itembtn3 = types.KeyboardButton('/dbupload')
itembtn3 = types.KeyboardButton('/addfriend')
itembtn4 = types.KeyboardButton('Exit')
admmarkup.add(itembtn1, itembtn2, itembtn3, itembtn4)
###################
@bot.message_handler(content_types=['text', '/start'])
###################
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
''')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
	elif message.text == '✉️Чат✉️' or message.text == '/chat':
		bot.send_message(message.chat.id,"Наш чат: t.me/wproject_chat")
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
	elif message.text == '💾Софт💾' or message.text == '/soft':
		links2 = open('links.txt','r')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.send_message(message.chat.id, '💾Список программ и ссылок на их: \n' + links2.read() + '\n💾')
		links2.close()
	elif message.text == '🔒Базы🔒'  or message.text == '/dblist':
		base2 = open('base.txt','r')
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
		friendbase = open('friends.txt','r')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.send_message(message.chat.id, 'Наши друзья: \n' + friendbase.read())
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
	elif message.text == '/stat' or message.text == '📊Статистика📊':
		idslist.close()  #проблема в статистке с которой я еще списал пару команд и получил ахуенные баги
		idslist = open('idlist.txt','r')
		with open('idlist.txt') as idslist:
			size=sum(1 for _ in idslist)
			bot.send_message(message.chat.id, '📊Статистика отображается в реальном времени!📊\nПользователей🙎‍♂: '+ str(size))
			idslist.close()
			idslist = open('idlist.txt','a')
			pass
	elif message.text == '🔎GitHub🔍' or  message.text == '/github':
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n')
		bot.send_message(message.chat.id, '🔎Страница бота на GitHub - https://github.com/d2nekomet/WBot-TelegramBot🔍')
	elif message.text == '/payments' or message.text == '💳Реквизиты💳':
		bot.send_message(message.chat.id, '''Привет. Всем надо зарабатывать и кушать. Админ этого бота и канала @www_project не исключение. Однако я не создаю приватные группы и т.д. Почему? Я считаю, что информация должна быть бесплатной!
Поэтому прошу помочь проекту рублем и украсить вечер админа порцией кексиков, ну или стену канала еще одним годным постом сделанным благодаря Вашим поддержкам!
Спасибо :)
Реквизиты:
Qiwi - https://qiwi.me/wwwproject
QiWi Карта - 
BTC - 1EwW7KwrEr5w2UXeCnJdJKAGPuWQPS1ZfV
Ethereum: 0xdb05ab0547e28f62ad0c7d856c0b9b4ed6d28789
Спасибо!❤️
''')
#       СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ  
#       СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ  
#       СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ   СЛУЖЕБНЫЕ КОМАНДЫ  
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
	msg = message.text.split()
	if msg[0] == '/send':
		myList = msg[2:]
		myString = '	'.join(myList)
		bot.send_message(chat_id=msg[1],text= '📩Вам сообщения от админа: ' + str(myString))
		bot.send_message(adminid, '✉️Соощение пользователю ' + msg[1] + ' отправлено успешно!\n✉️Текст сообщения: ' + str(myString) + ' ✉️')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) #логи в консоль
bot.polling(none_stop=True)