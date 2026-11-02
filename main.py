from telebot import TeleBot
from telebot import types
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN", None)

if not BOT_TOKEN:
    raise ValueError("BOT token sozlanmagan")

bot = TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Assalomu alaykum! {message.from_user.full_name}"
    )

@bot.message_handler(commands=["usd"])
def usd_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"1$ - 11800 so'm"
    )

@bot.message_handler(commands=["rub"])
def rub_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"1RUB - 149,19 so'm"
    )


@bot.message_handler(commands=["owner"])
def owner_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="👨‍💻 Создатель бота: https://t.me/Belling5am"
    )


if __name__ == "__main__":
    print("Bot ishga tushdi")
    bot.infinity_polling()
