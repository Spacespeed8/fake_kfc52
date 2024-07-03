import telebot
import buttons as bt
import webbrowser


bot = telebot.TeleBot(token="6915422620:AAFtz_shvDRbRGBAYyfctm2xZ7u0Evy5-VY")


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Здравстуйте! Это бот доставки.\n"
                              "Пожалуйста, напишите свое имя")

    name = message.text
    bot.register_next_step_handler(message, get_name)





def get_name(message):
    user_id = message.from_user.id

    name = message.text
    bot.send_message(user_id, "Отправьте свой номер", reply_markup=bt.phone_number_bt())
    bot.register_next_step_handler(message, get_number, name)
    print(name)




def get_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        number = message.contact.phone_number
        bot.send_message(user_id, "Отправьте свою локацию"
                         ,reply_markup = bt.location_bt())
        bot.register_next_step_handler(message, get_location, name,number)
    else:
        bot.send_message(user_id, "Отпрвьте свой номер через кнопку",
                         reply_markup = bt.phone_number_bt())
        bot.register_next_step_handler(message,get_number, name)

def get_location(message, name, number):
    user_id = message.from_user.id
    print(message)
bot.infinity_polling()


@bot.callback_query_handlers(lambda call:call.data in ["main_menu", "cart","minus","plus"])
def all_calls(call):
    user_id= call.message.chat.id
    if call.data=="main_menu":
        bot.delete_message(user_id,call.message.message_id)
        bot.send_message(user_id, "Выберите действие", reply_markup=bt.main_menu_kb())
    elif call.data == "cart":
        bot.send_message(user_id, "ваша корзина")
    elif call.data =="plus"
        current_amount

def product_call(call):
    user_id = call.message.chat.id
    bot.delete_message(user_id, call.message.message_id)
    product_id = int(call.data.replace("prod_"))