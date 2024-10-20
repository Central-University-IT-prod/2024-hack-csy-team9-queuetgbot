import telebot
from operator import truediv
from telebot import types


bot = telebot.TeleBot('{{sensitive data}}')
#для нажатие кнопики старт выдает :
@bot.message_handler(commands=['start'])
def start(message):
  markup = types.InlineKeyboardMarkup()

  btn1 = types.InlineKeyboardButton('сайт для того что бы войти в очередь', url='https://www.tbank.ru/loans/')
  markup.row(btn1)

  btn2 = types.InlineKeyboardButton('встать в очередь', url='https://www.tbank.ru/loans/' )
  btn3 = types.InlineKeyboardButton('выйти из очереди', url='https://www.lingscars.com/' )
  btn4 = types.InlineKeyboardButton('какой ты в очериди', url='https://www.tbank.ru/loans/' )
  markup.row(btn2, btn3, btn4)
  btn5 = types.InlineKeyboardButton('крутой ролик на дермовом сайте', url='{{sensitive data}}')
  markup.row(btn5)

  bot.reply_to(message, 'здраствуйте, в этом боте вы можете встать в электронную очередь', reply_markup=markup)



@bot.message_handler(commands=['help1'])
def help1(message):
  bot.reply_to(message, 'команда /start - войти в очередь /help1 -все комады')

@bot.message_handler()
def info(message):
  bot.send_message(message.chat.id, '<b>Общайтесь с помощью спец.команд(пожалуйста) обратитесь к команде /help1</b>', parse_mode='html')


bot.polling(none_stop=True)
