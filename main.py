import telebot
from flask import Flask, request

TOKEN = "هنا_تحطين_التوكن_حقك"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# الرد الأساسي
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "هلا والله 👋✨ Bot is running!")

# Webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@app.route("/", methods=['GET'])
def index():
    return "Bot is live!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="هنا_تحطين_رابط_الرايلواي_حقك" + TOKEN)
    app.run(host="0.0.0.0", port=8080)

