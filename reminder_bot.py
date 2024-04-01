from pyrogram import Client, filters
import schedule
import time

api_id = 27944333  # Замените на ваше реальное API ID
api_hash = '4b78bc078465c7d40895e979f17b5aec'  # Замените на ваш реальный API Hash
bot_token = '6189617084:AAG5NajeoYSDtpj_4ov2IO6svW-bsrYGnwE'  # Замените на ваш реальный токен бота

# ID чата (вашего пользователя в Telegram). Его нужно получить, отправив любое сообщение боту и просмотрев логи.
chat_id = '126713607'

app = Client("my_reminder_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text & (filters.regex("^(привет|Привет)$")))
async def greet_user(client, message):
    # Ответ "мау" на сообщение "привет" или "Привет"
    await message.reply("мау")

@app.on_message(filters.all)
async def log_chat_id(client, message):
    chat_id = message.chat.id
    print(f"Получено сообщение из чата с ID: {chat_id}")
    # Также вы можете отправить ID обратно пользователю, если это необходимо
    await message.reply(f"Ваш chat_id: {chat_id}")

app.run()

def send_reminder():
    with app:
        app.send_message(chat_id, "Не забудь заполнить гугл-таблицы сегодня! 😊\n"
                                  "1. https://docs.google.com/spreadsheets/d/19dugcxPmBDzzS5ikvpIGOaP-wQSxFgOqglJPt6b7R0s/edit#gid=2022225061\n"
                                  "2. https://docs.google.com/spreadsheets/d/1uqIY3wbXN9I1H0pkJWc14YT45TPgWtOCNnipeAwRhwY/edit#gid=215593323")

# Настройка расписания
schedule.every().friday.at("14:00").do(send_reminder)  # Время в формате 24H, например, "09:00" для 9 утра

# Запуск бота и планировщика
if __name__ == '__main__':
    with app:
        app.send_message(chat_id, "Бот-напоминалка активирован. Буду напоминать каждую пятницу в 09:00!")  # Отправка сообщения о запуске бота
    while True:
        schedule.run_pending()
        time.sleep(1)