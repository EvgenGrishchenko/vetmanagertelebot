import appointment
import telebot
import vetconnect
bot = telebot.TeleBot(vetconnect.config['token'])
surname = ''
name = ''
middle = ''
animal = ''
time = ''

@bot.callback_query_handler(func=lambda call: True)
@bot.message_handler(content_types=['text'])
def talk(message):
    if message.text.lower() == "да":
        smg = bot.send_message(message.chat.id, 'Введите Фамилию: ')
        bot.register_next_step_handler(smg, fam)
    else:
        bot.send_message(message.chat.id, 'Если хотите записаться на прием напишите "да"')
def fam(message):
    global surname
    surname = message.text
    smg = bot.send_message(message.chat.id, 'Введите Имя: ')
    bot.register_next_step_handler(smg, names)
def names(message):
    global name
    name = message.text
    smg = bot.send_message(message.chat.id, 'Введите Отчество: ')
    bot.register_next_step_handler(smg, sern)
def sern(message):
    global middle
    middle = message.text
    smg = bot.send_message(message.chat.id, 'Введите Кличку: ')
    bot.register_next_step_handler(smg, animals)
def animals(message):
    global animal
    animal = message.text
    smg = bot.send_message(message.chat.id, 'Введите время записи от 09 до 18: ')
    bot.register_next_step_handler(smg, hours)
def hours(message):
    global time
    time = message.text
    appoint(message)
def appoint(message):
    global surname, name, middle, animal, time
    appointment.write_client(message, surname, name, middle, animal, time)
def mes(message, tim, surname, name, middle, animal):
    send = 'Вы записаны в Клинику "domain" на прием как '+surname+' '+name+' '+middle+' с Вашим Питомцем '+animal
    bot.send_message(message.chat.id, send+'. Прием в '+tim)
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
if __name__ == '__main__':
    bot.polling(none_stop=True)
