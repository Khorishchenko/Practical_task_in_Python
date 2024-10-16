# ******************************************************************************************
# Настало время разобраться, как устроены фильтры и мидлвари в aiogram 3.x, 
# а также познакомиться с «убийцей лямбда-выражений» фреймворка — магическими фильтрами.
# https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/
# ******************************************************************************************





#==================================================================================================#
# Точка входа в приложение


import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config

from handlers import group_games
from Midlvars import UserInternalIdMiddleware



# Запуск бота
async def main():
    bot = Bot(token = config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(group_games.router)


    # Где-то в другом месте:
    # <...>
    dp.update.outer_middleware(UserInternalIdMiddleware())


    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



# Но чтобы обрабатывать сообщения, этого недостаточно, 
# нужны ещё хэндлеры. Мы хотим их расположить в других файлах, 
# чтобы не устраивать портянки на несколько тысяч строк. 
# В предыдущих главах все наши хэндлеры прицеплялись к диспетчеру, 
# но сейчас он внутри функции и мы точно не хотим делать его глобальным объектом.
# Что же делать? И тут на помощь приходят...Роутеры





# Итог¶
# У нас получилось аккуратно разделить бота по разным файлам, 
# не нарушая его работу. Примерное дерево файлов и каталогов получилось следующим 
# (здесь сознательно пропущены некоторые несущественные для примера файлы):

# ├── bot.py
# ├── handlers
# │   ├── different_types.py
# │   └── questions.py
# ├── keyboards
# │   └── for_questions.py