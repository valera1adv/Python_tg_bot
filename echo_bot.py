import telebot

token = "6350792761:AAHlqpuEiN9v3CzkkdAA4My3xxAIrY7xZ_U"
bot = telebot.TeleBot(token)
string = ["Валера", "Алина", "Катя", "Оля", "Ксюша"]

@bot.message_handler(content_types=['text'])

def echo(message):
    if message.text in string:
        bot.send_message(message.from_user.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True)

