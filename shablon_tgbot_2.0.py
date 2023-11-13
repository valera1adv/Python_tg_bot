import telebot
from telebot import types

bot = telebot.TeleBot('Введите токен')
CHANNEL_NAME = "Введите название канала"
CONTACT_LINK = "Введите ссылку на контактную информацию"
CHANNEL_LINK = "Введите ссылку на канал"

dict_price = {"Товар 1": "Описание и цена", "Товар 2": "Описание и цена"}  # Прайс-лист
questions = {"Вопрос 1": "Ответ 1", "Вопрос 2": "Ответ 2"}  # Вопрос-ответ

# Приветствие
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("Начать")
    markup.add(btn0)
    bot.send_message(chat_id, f"Привет! Я бот-помощник канала {CHANNEL_NAME}!", reply_markup=markup)

# Пользовательский интерфейс
@bot.message_handler(content_types=['text'])
def menu(message):
    chat_id = message.chat.id
    if message.text == 'Начать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Прайс-лист')
        btn2 = types.KeyboardButton('Частые вопросы')
        btn3 = types.KeyboardButton('Вопрос по рекламе')
        btn4 = types.KeyboardButton('TG-канал')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id, 'Выберите категорию вопроса', reply_markup=markup)
    elif message.text == 'Прайс-лист':
        show_price_list(chat_id)
    elif message.text == 'Частые вопросы':
        show_questions(chat_id)
    elif message.text == 'Вопрос по рекламе':
        bot.send_message(chat_id, f'Связаться с администратором\n \nможно по [ссылке]({CONTACT_LINK})', parse_mode='Markdown')
    elif message.text == 'TG-канал':
        bot.send_message(chat_id, f'Телеграм канал\n \nдоступен по [ссылке]({CHANNEL_LINK})', parse_mode='Markdown')

def show_price_list(chat_id):
    price_list = "\n".join(f"{key}: {value}" for key, value in dict_price.items())
    bot.send_message(chat_id, price_list)

def show_questions(chat_id):
    question_list = "\n".join(f"{key}: {value}" for key, value in questions.items())
    bot.send_message(chat_id, question_list)

# Команды администратора
HELP = """
/admin_help - Напечатать список доступных команд;
/add_offer - Добавить товар (/add_offer товар описание-цена)
/add_quest - Добавить вопрос (/add_quest вопрос ответ)
"""

# функция добавления товара
def add_offers(offer, price):
    dict_price[offer.lower()] = price

# функция добавления вопроса
def add_quest(question, answer):
    questions[question.lower()] = answer

# команда хелп
@bot.message_handler(commands=["admin_help"])
def help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, HELP)
    print(HELP)

# команда добавления товара
@bot.message_handler(commands=["add_offer"])
def add_offer(message):
    command = message.text.split(maxsplit=2)
    offer = command[1].lower()
    price = command[2]
    if len(offer) < 3:
        text = "Название слишком короткое."
    else:
        text = f"Описание {price} добавлено к товару {offer}"
        add_offers(offer, price)
    bot.send_message(message.chat.id, text)

# команда добавления вопроса
@bot.message_handler(commands=["add_quest"])
def add_questions(message):
    command = message.text.split(maxsplit=2)
    question = command[1].lower()
    answer = command[2]
    if len(question) < 3:
        text = "Вопрос слишком короткий."
    else:
        text = f"Ответ {answer} добавлен к вопросу {question}"
        add_quest(question, answer)
    bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)