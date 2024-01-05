from telebot import TeleBot, types
from requests import get
import json
from time import sleep

bot = TeleBot('Введите токен')
bot.delete_webhook()

def send_text_message(message):
    """
    Функция send_text_message
    Отправляет письмо для обратной связи на случай, если инструкция не подошла
    """
    text = "Не нашли ответ на свой вопрос?\nТогда напишите нам [сообщение](https://www.advantshop.net/support)"
    chat_id = message.chat.id
    sleep(60)  # задержка отправки на 60 секунд
    bot.send_message(chat_id, text, parse_mode='Markdown')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добрый день!\nЯ бот помощник компании AdvantShop.\nВведите Ваш вопрос:")

@bot.message_handler(func=lambda message: True)
def answers(message):
    def send_instructions(chat_id, instructions):
        keyboard = types.InlineKeyboardMarkup()
        for instruction in instructions:
            name = instruction["name"]
            url = instruction["url"]
            button = types.InlineKeyboardButton(text=name, url=url)
            keyboard.add(button)
        bot.send_message(chat_id, "Выберите инструкцию:", reply_markup=keyboard)

    text = message.text
    response = questions(text)
    if response is not None:
        send_instructions(message.chat.id, response)
        send_text_message(message)
    else:
        bot.send_message(message.chat.id, "Ошибка при выполнении запроса")
        send_text_message(message)

def questions(question):
    """
    Функция questions
    Выполняет GET-запрос и возвращает элементы "Name" и "Url" из списка инструкций с официального сайта AdvantShop
    """
    link = 'https://www.advantshop.net/help/searchext?q='
    response = get(link + question)
    if response.status_code == 200:
        try:
            json_data = json.loads(response.text)
            instructions = []
            for item in json_data:
                name = item.get("Name")
                url = item.get("Url")
                if name and url:
                    instructions.append({"name": name, "url": url})
            return instructions[:5]
        except json.JSONDecodeError:
            return None
    else:
        return None

bot.polling(non_stop=True)
