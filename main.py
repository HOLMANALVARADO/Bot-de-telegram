import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

API_KEY = "2041835515:AAGzcXgAFuw2sfDqCyfSW8vT7lcsWVLPl-Y"
bot = telebot.TeleBot(API_KEY)

api_id = 'API_id'
api_hash = 'API_hash'
token = 'bot token'
message = "Working..."
phone = '+573143277479'

@bot.message_handler(commands=['tareas'])
def greet(message):
  bot.reply_to(message, "No hay tareas asignadas")

@bot.message_handler(commands=['hola'])
def hola(message):
  bot.send_message(message.chat.id, "Te saluda tu bot de tareas")

def task_request(message):
  request = message.text.split()
  if len(request)< 2 or request[0].lower() not in "anotar":
    return False
  else:
    return True

@bot.message_handler(func=task_request)
def send_task(message):
  bot.send_message(message.chat.id, "Tu tarea ha sido anotada y se recordará")
  pass


bot.polling()