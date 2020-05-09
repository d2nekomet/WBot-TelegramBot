#Бот канала t.me/www_project 
#Написан t.me/os_people
#Emoji for message        💻📷 📸 📹 🎥 📽💡💣🧱📁 📂 🗂🔍 🔎 🔏 🔐 🔒 🔓❤️ 🧡 💛 💚 💙 💜 🖤☢️ ☣️ 📴 📳🆔  ✉️ 📩 📨 📧 💌  📱 📲 💻 ⌨️ 🖥 🖨
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
bot = telebot.TeleBot(TOKEN) # TOKEN # TelegramID админа
adminid = int(adminidr)
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
itembtn1 = types.KeyboardButton('✉️Чат✉️')
itembtn2 = types.KeyboardButton('💩Админы💩')   # Это кнопки
itembtn3 = types.KeyboardButton('😁Помощь😁')
itembtn4 = types.KeyboardButton('💾Софт💾')
itembtn5 = types.KeyboardButton('🔒Базы🔒')
markup.add(itembtn4,itembtn5,itembtn1, itembtn2, itembtn3)

admmarkup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/addlink')
itembtn2 = types.KeyboardButton('/addbase')
itembtn3 = types.KeyboardButton('/dbupload')
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
/buttons - 🗂Перезагрузка кнопок🗂
/stat - 📊Статистика📊
/github - 🔎страница бота на GitHub🔍
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
	elif message.text == '/github':
		bot.send_message(message.chat.id, '🔎GitHub РЕпозиторий бота: https://github.com/d2nekomet/WBot-TelegramBot 🔍')
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 

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
	elif message.text == '/dbupload' and message.chat.id == adminid:
		myDBList = os.listdir(path="Logs/")
		myDBString = '	,	'.join(myDBList)
		db = bot.send_message(message.chat.id, 'Выберите базу которую хотите скачать (напишите имя файла): \n' + myDBString)
		logs.write('Сообщения: ' + message.text + '\nВремя получения: ' + time.ctime() + '\nАйди: '+ str(message.chat.id) +'\nИмя: ' + str(message.from_user.first_name) + '\nФамилия: ' + str(message.from_user.last_name) + '\nНик: @' + str(message.from_user.username)+ '\n' + 'Тип чата: '+ str(message.chat.type) +'\n\n') 
		bot.register_next_step_handler(db, dbupl)
	elif message.text == '/stat':
		idslist.close()
		idslist = open('idlist.txt','r')
		with open('idlist.txt') as idslist:
			size=sum(1 for _ in idslist)
			bot.send_message(message.chat.id, '📊Статистика отображается в реальном времени!📊\nПользователей🙎‍♂: '+ str(size))
			idslist.close()
			idslist = open('idlist.txt','a')
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