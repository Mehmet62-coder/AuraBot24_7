import telebot
from flask import Flask
from threading import Thread
import os

TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot token
bot = telebot.TeleBot(TOKEN)

# ===== Telegram Commands =====
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hey! I'm alive 24/7 🔥")

# ===== Flask Web Server =====
app = Flask('')

@app.route('/')
def home():
    return "Aura Bot is alive ✅"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
bot.infinity_polling()
