import telebot
from telebot import types

bot = telebot.TeleBot('*********************************')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("Начать")
    markup.add(btn0)
    bot.send_message(message.from_user.id, "Привет! Я бот-помошник технической поддержки!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Начать': #Начало цикла
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Дизайн')
        btn2 = types.KeyboardButton('Товары')
        btn3 = types.KeyboardButton('Категории')
        btn4 = types.KeyboardButton('База знаний')
        btn5 = types.KeyboardButton('Оставить заявку')
        btn6 = types.KeyboardButton('Найти специалиста')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, 'Выберите категорию вопроса', reply_markup=markup) #ответ бота


    elif message.text == 'Дизайн': #Вложенный цикл
        bot.send_message(message.from_user.id, 'Статьи по вопросам Дизайна сайта\n \nдоступны по ' + '[ссылке](https://www.advantshop.net/help/pages/shablony-dizaina)', parse_mode='Markdown')

    elif message.text == 'Товары':
        bot.send_message(message.from_user.id, 'Статьи по работе с товарами\n \nдоступны по ' + '[ссылке](https://www.advantshop.net/help/pages/add-product)', parse_mode='Markdown')

    elif message.text == 'Категории':
        bot.send_message(message.from_user.id, 'Статьи по работе с категориями\n \nдоступны по ' + '[ссылке](https://www.advantshop.net/help/pages/directory-categories)', parse_mode='Markdown')

    elif message.text == 'База знаний':
        bot.send_message(message.from_user.id, 'База знаний\n \nдоступна по ' + '[ссылке](https://www.advantshop.net/help)', parse_mode='Markdown')

    elif message.text == 'Найти специалиста':
        bot.send_message(message.from_user.id, 'Выбрать подходящего специалиста\n \nможно по ' + '[ссылке](https://www.advantshop.net/partners)', parse_mode='Markdown')

    elif message.text == 'Оставить заявку':
        bot.send_message(message.from_user.id, 'Уточнить свой вопрос у специалиста можно [тут](https://www.advantshop.net/support)', parse_mode='Markdown')
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
