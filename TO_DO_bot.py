import telebot

token = "*****"

bot = telebot.TeleBot(token)

HELP = """
/help - Напечатать срисок доступных комманд
/add - Добавить задачу
/show - Показать все запланированные задачи
"""

tasks = {}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    if len(task) < 3:
        text = "Задача слишком короткая."
    else:
        text = "Задача " + task + " добавлена на дату " + date 
        add_todo(date, task)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = []
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text += "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"    
    bot.send_message(message.chat.id, text)\

bot.polling(non_stop=True)
    