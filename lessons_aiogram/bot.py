# импорты
import asyncio
import logging
import sys
import json
import aiohttp
from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command  import Command

# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")



# Хэндлер на команду /test2
# Хэндлер cmd_test2 не сработает, т.к. диспетчер о нём не знает. Исправим эту ошибку и отдельно зарегистрируем функцию:
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")










# Синтаксический сахар
# Для того чтобы сделать код чище и читабельнее, aiogram расширяет возможности стандартных объектов Telegram. 
# Например, вместо bot.send_message(...) можно написать message.answer(...) или message.reply(...). 
# В последних двух случаях не нужно подставлять chat_id, подразумевается, что он такой же, как и в исходном сообщении.

# Разница между answer и reply простая: 
# первый метод просто отправляет сообщение в тот же чат, второй делает "ответ" на сообщение из message:

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')



#==================================================================================================
# answer метод


# Хэндлер на команду answer dice
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


# Однако, вы можете отследить, какое число было выброшено, используя событие  dice .  
@dp.message(type.ContentTypes.DICE)
async def handle_dice(message: types.Message):
    dice_value = message.dice.value  # Получаем значение, выброшенное кубиком
    await message.answer(f"Вы выбросили: {dice_value}")
   

# Хэндлер на команду answer send_animation
@dp.message(Command("send_animation"))
async def send_animation(message: types.Message):
    try:
        animation_url = "https://i.natgeofe.com/k/63b1a8a7-0081-493e-8b53-81d01261ab5d/red-panda-full-body_4x3.jpg"
        await message.answer_animation(animation_url)
    except Exception as e:
        # Логируем ошибку или обрабатываем её соответствующим образом
        print(f"Ошибка при отправке animation: {e}")









#==================================================================================================
# Передача доп. параметров¶

# Где-то в другом месте
# Например, в точке входа в приложение
from datetime import datetime


# bot = ...
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")



@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")


@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")






#==================================================================================================

# Запуск процесса поллинга новых апдейтов
async def main():
    # Где-то в другом месте, например, в функции main(): отдельно зарегистрируем функцию Хэндлер cmd_test2
    dp.message.register(cmd_test2, Command("test2"))

    # Запускаем процесс поллинга новых апдейтов
    # await dp.start_polling(bot)
    await dp.start_polling(bot, mylist=[1, 2, 3])


# ��лавный цикл
if __name__ == "__main__":
    asyncio.run(main())
