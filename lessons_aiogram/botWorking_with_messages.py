# импорты
import asyncio
import logging
import sys
import json
import aiohttp
from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command  import Command



from aiogram import F
from aiogram.client.default import DefaultBotProperties
# from aiogram.types import ParseMode




# ******************************************************************************************
# Сообщения в Telegram делятся на текстовые, медиафайлы и служебные (они же — сервисные).
# ******************************************************************************************



# https://mastergroosha.github.io/aiogram-3-guide/messages/


# parse_mode = 'HTML'

#  К счастью, в aiogram можно задать параметры бота по умолчанию
# bot = Bot(
#     token = config.bot_token.get_secret_value(),
#     default = DefaultBotProperties(
#         parse = 'HTML'
#         # тут ещё много других интересных настроек
#     )
# )

# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'

bot = Bot(token = config.bot_token.get_secret_value())




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









#==================================================================================================#
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



#==================================================================================================#
# answer метод

# ��эндлер на любое сообщение
# @dp.message()
# async def echo(message: types.Message):
#     await message.answer(message.text)


# Хэндлер на команду answer dice
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


# # Однако, вы можете отследить, какое число было выброшено, используя событие  dice .  
# @dp.message(type.ContentTypes.DICE)
# async def handle_dice(message: types.Message):
#     dice_value = message.dice.value  # Получаем значение, выброшенное кубиком
#     await message.answer(f"Вы выбросили: {dice_value}")
   

# Хэндлер на команду answer send_animation
@dp.message(Command("send_animation"))
async def send_animation(message: types.Message):
    try:
        animation_url = "https://i.natgeofe.com/k/63b1a8a7-0081-493e-8b53-81d01261ab5d/red-panda-full-body_4x3.jpg"
        await message.answer_animation(animation_url)
    except Exception as e:
        # Логируем ошибку или обрабатываем её соответствующим образом
        print(f"Ошибка при отправке animation: {e}")









#==================================================================================================#
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







# Обработка текстовых сообщений 
#===========================================================================================================#
# это, пожалуй, одно из важнейших действий у большинства ботов. 
# Текстом можно выразить практически что угодно и при этом подавать информацию хочется красиво. 

from aiogram import F
from aiogram.enums import ParseMode



# Если не указать фильтр F.text, 
# то хэндлер сработает даже на картинку с подписью /test
@dp.message(F.text, Command("test"))
async def any_message(message: types.Message):
    text = "Привет, это бот! <u>HTML-разметкой</u> "  # Добавляем текст из сообщения к тексту ответа
    await message.answer(
        "Hello, <b>world</b>!", 
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "Hello, *world*\!", 
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await message.answer(text, parse_mode = ParseMode.HTML )



# Экранирование ввода
@dp.message(Command("hello"))
async def cmd_hello(message: types.Message):
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML
    )





# Но тут приходит юзер с именем <Cлавик777> и бот молчит! А в логах видно следующее: 
# aiogram.exceptions.TelegramBadRequest: 
# Telegram server says - Bad Request: can't parse entities: 
# Unsupported start tag "Славик777" at byte offset 7

from aiogram.utils.formatting import Text, Bold

@dp.message(Command("Hello"))
async def cmd_hello(message: types.Message):
    content = Text(
        "Hello, ",
        Bold(message.from_user.full_name)
    )
    await message.answer(
        **content.as_kwargs()
    )



# Упомянутый инструмент форматирования довольно комплексный, 
# официальная документация демонстрирует удобное отображение сложных конструкций, например:
# https://docs.aiogram.dev/en/latest/utils/formatting.html

from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)


@dp.message(Command("advanced_example"))
async def cmd_advanced_example(message: types.Message):
    content = as_list(
        as_marked_section(
            Bold("Success:"),
            "Test 1",
            "Test 3",
            "Test 4",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Failed:"),
            "Test 2",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("Summary:"),
            as_key_value("Total", 4),
            as_key_value("Success", 3),
            as_key_value("Failed", 1),
            marker="  ",
        ),
        HashTag("#test"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs())






# Работа с entities¶
# Telegram сильно упрощает жизнь разработчикам, выполняя предобработку сообщений пользователей на своей стороне. 
# Например, некоторые сущности, типа e-mail, 
# номера телефона, юзернейма и др. можно не доставать регулярными выражениями, 
# а извлечь напрямую из объекта Message и поля entities,
import html
from aiogram import types

# @dp.message(F.text)
@dp.message(Command("Pass"))
async def extract_data(message: types.Message):
     # Проверка, является ли сообщение командой или простым текстом
    if message.entities is None or len(message.entities) == 0:
        await message.reply("Пожалуйста, введите корректные данные (URL, E-mail или код).")
        return

    data = {
        "url": "<N/A>",
        "email": "<N/A>",
        "code": "<N/A>"
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            # Неправильно
            # data[item.type] = message.text[item.offset : item.offset+item.length]
            # Правильно
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Вот что я нашёл:\n"
        f"URL: {html.escape(data['url'])}\n"
        f"E-mail: {html.escape(data['email'])}\n"
        f"Пароль: {html.escape(data['code'])}"
    )








# Команды и их аргументы¶
# Telegram предоставляет пользователям множество способов ввода информации. Одним из них являются 
# команды: ключевые слова, начинающиеся со слэша, например, /new или /ban. 
# Иногда бот может быть спроектирован так, чтобы ожидать после самой команды какие-то аргументы, 
# вроде /ban 2d или /settimer 20h This is delayed message. В составе aiogram есть фильтр Command(), 
# упрощающий жизнь разработчика.


# Команды и их аргументы
@dp.message(Command("settimer"))
async def cmd_settimer(
        message: types.Message,
        command
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу
    try:
        delay_time, text_to_send = command.args.split(" ", maxsplit=1)
    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n"
            "/settimer <time> <message>"
        )
        return
    await message.answer(
        "Таймер добавлен!\n"
        f"Время: {delay_time}\n"
        f"Текст: {text_to_send}"
    )








# Диплинки¶
# Команда /start в Telegram може містити додаткові параметри через диплінк (t.me/bot?start=xxx), 
# що автоматично передає їх боту при натисканні кнопки "Почати", і це зручно для активації команд, реферальних систем та налаштувань.

import re
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

@dp.message(Command("help"))
@dp.message(CommandStart(
    deep_link=True, magic=F.args == "help"
))
async def cmd_start_help(message: Message):
    await message.answer("Это сообщение со справкой")


@dp.message(CommandStart(
    deep_link=True,
    magic=F.args.regexp(re.compile(r'book_(\d+)'))
))
async def cmd_start_book(
        message: Message,
        command: CommandObject
):
    book_number = command.args.split("_")[1]
    await message.answer(f"Sending book №{book_number}")








# Предпросмотр ссылок
# Обычно при отправке текстового сообщения со ссылками Telegram пытается найти и показать предпросмотр первой по порядку ссылки. 
# Это поведение можно настроить по своему желанию, передав в качестве аргумента link_preview_options метода send_message() 
# объект LinkPreviewOptions:


# Новый импорт
from aiogram.types import LinkPreviewOptions

@dp.message(Command("links"))
async def cmd_links(message: Message):
    links_text = (
        "https://nplus1.ru/news/2024/05/23/voyager-1-science-data"
        "\n"
        "https://t.me/telegram"
    )
    # Ссылка отключена
    options_1 = LinkPreviewOptions(is_disabled=True)
    await message.answer(
        f"Нет превью ссылок\n{links_text}",
        link_preview_options=options_1
    )

    # -------------------- #

    # Маленькое превью
    # Для использования prefer_small_media обязательно указывать ещё и url
    options_2 = LinkPreviewOptions(
        url="https://nplus1.ru/news/2024/05/23/voyager-1-science-data",
        prefer_small_media=True
    )
    await message.answer(
        f"Маленькое превью\n{links_text}",
        link_preview_options=options_2
    )

    # -------------------- #

    # Большое превью
    # Для использования prefer_large_media обязательно указывать ещё и url
    options_3 = LinkPreviewOptions(
        url="https://nplus1.ru/news/2024/05/23/voyager-1-science-data",
        prefer_large_media=True
    )
    await message.answer(
        f"Большое превью\n{links_text}",
        link_preview_options=options_3
    )

    # -------------------- #

    # Можно сочетать: маленькое превью и расположение над текстом
    options_4 = LinkPreviewOptions(
        url="https://nplus1.ru/news/2024/05/23/voyager-1-science-data",
        prefer_small_media=True,
        show_above_text=True
    )
    await message.answer(
        f"Маленькое превью над текстом\n{links_text}",
        link_preview_options=options_4
    )

    # -------------------- #

    # Можно выбрать, какая ссылка будет использоваться для предпосмотра,
    options_5 = LinkPreviewOptions(
        url="https://t.me/telegram"
    )
    await message.answer(
        f"Предпросмотр не первой ссылки\n{links_text}",
        link_preview_options=options_5
    )










# Медиафайлы
# Помимо обычных текстовых сообщений Telegram позволяет обмениваться 
# медиафайлами различных типов: фото, видео, гифки, геолокации, стикеры и т.д

# У большинства медиафайлов есть свойства file_id и file_unique_id.

# К примеру, следующий код заставит бота моментально ответить пользователю той же гифкой, что была прислана:
@dp.message(F.animation)
async def echo_gif(message: Message):
    await message.reply_animation(message.animation.file_id)



# Всегда используйте правильные file_id!
# https://mastergroosha.github.io/aiogram-3-guide/messages/



# В aiogram 3.x присутствуют 3 класса для отправки файлов и медиа - FSInputFile, BufferedInputFile, URLInputFile,
# с ними можно ознакомиться в документации.
# https://docs.aiogram.dev/en/dev-3.x/api/upload_file.html


# Рассмотрим простой пример отправки изображений всеми различными способами:
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

@dp.message(Command('images'))
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Чтобы продемонстрировать BufferedInputFile, воспользуемся "классическим"
    # открытием файла через `open()`. Но, вообще говоря, этот способ
    # лучше всего подходит для отправки байтов из оперативной памяти
    # после проведения каких-либо манипуляций, например, редактированием через Pillow
    with open("buffer_emulation.jpg", "rb") as image_from_buffer:
        result = await message.answer_photo(
            BufferedInputFile(
                image_from_buffer.read(),
                filename="image from buffer.jpg"
            ),
            caption="Изображение из буфера"
        )
        file_ids.append(result.photo[-1].file_id)

    # Отправка файла из файловой системы
    image_from_pc = FSInputFile("image_from_pc.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id)

    # Отправка файла по ссылке
    image_from_url = URLInputFile("https://picsum.photos/seed/groosha/400/300")
    result = await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке"
    )
    file_ids.append(result.photo[-1].file_id)
    await message.answer("Отправленные файлы:\n"+"\n".join(file_ids))








# Скачивание файлов
# Помимо переиспользования для отправки, бот может скачать медиа к себе на компьютер/сервер. 
# Для этого у объекта типа Bot есть метод download()





# Альбомы
# То, что мы называем «альбомами» (медиагруппами) в Telegram, на самом деле отдельные сообщения \
#     с медиа, у которых есть общий media_group_id и которые визуально «склеиваются» на клиентах.

from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder

@dp.message(Command("album"))
async def cmd_album(message: Message):
    # Создаем билдер для альбома
    album_builder = MediaGroupBuilder(
        caption = "Общая подпись для будущего альбома"
    )


    # Отправка файла из файловой системы
    album_builder.add(
        type = "photo",
        media = FSInputFile("image_from_pc.jpg")
        # caption="Подпись к конкретному медиа"

    )



    # Если мы сразу знаем тип, то вместо общего add
    # можно сразу вызывать add_<тип>
    album_builder.add_photo(
        # Для ссылок или file_id достаточно сразу указать значение
        media = URLInputFile("https://picsum.photos/seed/groosha/400/300")
    )

    # Для других медиа-типов вам нужно будет написать свои add_<тип>
    album_builder.add_photo(
        media = "<ваш file_id>"
    )
    await message.answer_media_group(
        # Не забудьте вызвать build()
        media = album_builder.build()
    )








# Сервисные (служебные) сообщения
@dp.message(F.new_chat_members)
async def somebody_added(message: Message):
    for user in message.new_chat_members:
        # проперти full_name берёт сразу имя И фамилию 
        # (на скриншоте выше у юзеров нет фамилии)
        await message.reply(f"Привет, {user.full_name}")




#==================================================================================================#

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
