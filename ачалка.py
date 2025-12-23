import random
import telebot

bot = telebot.TeleBot('8562188337AAHucn5k49skI4Bub9WI2FlTciAybrkHr4M')


@bot.message_handler(commands=['random'])
def random_number(message)
    try
        numbers = message.text.split()[1]
        start = int(numbers)
        end = int(numbers)
        random_num = random.randint(start, end)
        bot.send_message(message.chat.id, f'Случайно число {random_num}')
    except (ValueError, IndexError)
        bot.send_message(message.chat.id, Пожалуйста, введите два числа через пробел после команды random)


bot.polling(none_stop=True, interval=0)