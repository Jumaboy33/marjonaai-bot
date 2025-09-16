import os
import telebot
from openai import OpenAI

# 🔑 Tokenlarni environment variable orqali olish
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Telegram bot va OpenAI clientni ishga tushirish
bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

# Har qanday xabarni qabul qilish
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    try:
        # OpenAI ga so'rov yuborish
        response = client.responses.create(
            model="gpt-5",
            input=message.text
        )

        # OpenAI javobini foydalanuvchiga yuborish
        bot.reply_to(message, response.output_text)

    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {e}")

print("✅ Marjona.AI bot ishga tushdi...")
bot.polling()
