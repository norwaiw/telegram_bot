import sqlite3
import telebot
from API import token

bot = telebot.TeleBot(token)

# Функция для получения ответа из базы данных по заданному числу
def get_answer_by_number(number):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT string_column FROM my_table WHERE id = ?', (number,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Пытаемся получить число из сообщения пользователя
        number = int(message.text)

        # Проверяем, что число находится в диапазоне от 1 до 10
        if 1 <= number <= 4:  # Замените на нужный диапазон
            # Получение ответа из базы данных по заданному числу
            answer = get_answer_by_number(number)

            if answer:
                bot.reply_to(message, f"Ваше число: {number}\nОтвет из базы данных: {answer}")
            else:
                bot.reply_to(message, "Данные не найдены для этого числа.")
        else:
            bot.reply_to(message, "Пожалуйста, введите число от 1 до 4.")  # Измените на нужный диапазон
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите числовое значение от 1 до 4.")