from bot import bot
import sqlite3

def start():
    conn = sqlite3.connect('database.db')

    # Создание курсора для выполнения SQL-запросов
    cursor = conn.cursor()

    # Название таблицы, которую вы хотите проверить
    table_name = 'my_table'

    # SQL-запрос для проверки существования таблицы
    check_table_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"

    # Выполнение SQL-запроса
    cursor.execute(check_table_query)

    # Извлечение результатов запроса
    result = cursor.fetchone()

    if result:
        pass
    else:
        # SQL-запрос для создания таблицы
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS my_table (
                id INTEGER PRIMARY KEY,
                string_column TEXT
            );
            '''

        # Выполнение SQL-запроса для создания таблицы
        cursor.execute(create_table_query)

        # Пример данных для вставки
        data_to_insert = [
            (1, 'Свитшот ИОМ'),
            (2, 'Майка ИОМ'),
            (3, 'Фредди фазбер'),
            # Добавьте здесь нужные данные для вставки
        ]

        # SQL-запрос для вставки данных в таблицу
        insert_query = 'INSERT INTO my_table (id, string_column) VALUES (?, ?)'

        # Вставка данных в таблицу
        cursor.executemany(insert_query, data_to_insert)

        # Сохранение изменений и закрытие соединения
        conn.commit()

    conn.close()

if __name__ == "__main__":
    start()

    bot.polling()