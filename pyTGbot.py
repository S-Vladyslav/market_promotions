import telebot
import config
from web_scraping import Atbmarket_promotions

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types = ['text'])
def func(message):
    if message.text == 'atb':
        bot.send_message(message.chat.id, 'Будь ласка, зачекай')
        
        atb_promotions = Atbmarket_promotions.get_atb_promotions()
        bot.send_message(message.chat.id, 'Знайдено ' + str(len(atb_promotions)) + ' знижок')

        for promotion_dict in atb_promotions:
            promotion_text = 'Назва продукту: ' + promotion_dict.get('productName') + '\n'
            promotion_text += 'Стара ціна: ' + promotion_dict.get('oldPrice') + '\n'
            promotion_text += 'Нова ціна: ' + promotion_dict.get('newPrice') + '\n'
            promotion_text += 'Знижка: ' + promotion_dict.get('discount') + '\n'
            bot.send_message(message.chat.id, promotion_text)

    elif message.text == '/start':
        bot.send_message(message.chat.id, 'Привіт')
        bot.send_message(message.chat.id, 'Поки що я вмію показувати знижки тільки з АТБ (введи atb)')

    else:
        bot.send_message(message.chat.id, 'Поки що я вмію показувати знижки тільки з АТБ (введи atb)')


bot.polling(none_stop=True)
