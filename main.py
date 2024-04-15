import asyncio
from aiogram import Bot, Dispatcher
from datetime import datetime, time

# Укажите токен вашего бота
API_TOKEN = ''

# Укажите ID вашей группы
# Список ID групп (через запятую 0001, 0002)
group_ids = [-10000000000000000]


# Создаем экземпляр бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Функция для отправки сообщений в группу
async def send_message():
    current_time = datetime.now().time()

    for GROUP_ID in group_ids:
        if current_time.hour == 21 and current_time.minute == 57:
            await bot.send_message(GROUP_ID,
                                   f"ВНИМАНИЕ test! \n"
                                   )
        if current_time.hour == 21 and current_time.minute == 30:
            await bot.send_message(GROUP_ID,
                                   f"ВНИМАНИЕ! \n"
                                   f"Ваша смена близится к завершению. \n"
                                   f"Необходимо: \n"
                                   f"1 - Сделать это. \n"
                                   f"2 - А также не забыть сделать вот это. \n"
                                   )
        if current_time.hour == 10 and current_time.minute == 0:
            await bot.send_message(GROUP_ID,
                                   f"ВНИМАНИЕ! \n"
                                   f"Еще одно сообещние \n"
                                   )
        if current_time.hour == 22 and current_time.minute == 0:
            await bot.send_message(GROUP_ID,
                                   f"ВНИМАНИЕ! \n"
                                   f"Другое сообещние по указанному времени \n"
                                   )
        else:
            print("Сообщение еще не готово")

# Функция для запуска цикла событий


async def scheduler():
    while True:
        await send_message()
        await asyncio.sleep(60)  # Проверяем каждую минуту

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())  # Создаем задачу для отправки сообщений
    loop.run_forever()  # Запускаем цикл событий
