from flask import Flask
from threading import Thread
import telebot
import os

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hey! I'm alive 24/7 🔥")

# Flask server
app = Flask('')

@app.route('/')
def home():
    return "Aura Bot is alive ✅"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

Thread(target=run).start()
bot.infinity_polling()