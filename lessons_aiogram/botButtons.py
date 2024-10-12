# ******************************************************************************************
# В этой главе мы познакомимся с такой замечательной фичей Telegram-ботов как  | кнопки |. 
# Прежде всего, чтобы избежать путаницы, определимся с названиями. 
# То, что цепляется к низу экрана вашего устройства, будем называть обычными кнопками, <-
# а то, что цепляется непосредственно к сообщениям, назовём инлайн-кнопками <-
# ******************************************************************************************


import asyncio
import logging
import sys
import json
import aiohttp
from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command  import Command


bot = Bot(token = config.bot_token.get_secret_value())
dp = Dispatcher()











#==================================================================================================#
# Обычные кнопки¶
# Кнопки как шаблоны

#  Принцип простой: что написано на кнопке, то и будет отправлено в текущий чат. 
# Соответственно, чтобы обработать нажатие такой кнопки, бот должен распознавать входящие текстовые сообщения.

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


# Как-то некрасиво. Во-первых, хочется сделать кнопки поменьше, а во-вторых, расположить их горизонтально.
# а для пущей важности добавим параметр input_field_placeholder, 
# который заменит текст в пустой строке ввода, когда активна обычная клавиатура:

@dp.message(Command("startSmall"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)



# Осталось научить бота реагировать на нажатие таких кнопок.
# новый импорт!
from aiogram import F

@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text.lower() == "без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!", reply_markup=types.ReplyKeyboardRemove())
    

# Чтобы удалить кнопки, необходимо отправить новое сообщение со специальной «удаляющей» 
# клавиатурой типа ReplyKeyboardRemove. Например: await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())













#==================================================================================================#
# Keyboard Builder
# Для более динамической генерации кнопок можно воспользоваться сборщиком клавиатур

# Создадим пронумерованную клавиатуру размером 4×4:

# новый импорт!
from aiogram.utils.keyboard import ReplyKeyboardBuilder

@dp.message(Command("reply_builder"))
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(types.KeyboardButton(text=str(i)))  #add(<KeyboardButton>) — добавляет кнопку в память сборщика;

    builder.adjust(4)                                   #adjust(int1, int2, int3...) — делает строки по int1, int2, int3... кнопок;

    await message.answer(
        "Выберите число:",
        reply_markup=builder.as_markup(resize_keyboard=True),   # as_markup() — возвращает готовый объект клавиатуры;
    )

# У объекта обычной клавиатуры есть ещё две полезных опции: one_time_keyboard для автоматического скрытия 
# кнопок после нажатия и selective для показа клавиатуры лишь некоторым участникам группы. 
# Их использование остаётся для самостоятельного изучения. == https://core.telegram.org/bots/api#replykeyboardmarkup













#==================================================================================================#
# Специальные обычные кнопки

# существует шесть специальных видов обычных кнопок, не являющихся обычными шаблонами сообщений. 
# Они предназначены для:
# - отправки текущей геолокации;
# - отправки своего контакта с номером телефона;
# - создания опроса/викторины;
# - выбора и отправки боту данных пользователя с нужными критериями;
# - выбора и отправки боту данных (супер)группы или канала с нужными критериями;
# - запуска веб-приложения (WebApp).



@dp.message(Command("special_buttons"))
async def cmd_special_buttons(message: types.Message):
    builder = ReplyKeyboardBuilder()
    # метод row позволяет явным образом сформировать ряд
    # из одной или нескольких кнопок. Например, первый ряд
    # будет состоять из двух кнопок...
    builder.row(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True)
    )
    # ... второй из одной ...
    builder.row(types.KeyboardButton(
        text="Создать викторину",
        request_poll=types.KeyboardButtonPollType(type="quiz"))
    )
    # ... а третий снова из двух
    builder.row(
        types.KeyboardButton(
            text="Выбрать премиум пользователя",
            request_user=types.KeyboardButtonRequestUser(
                request_id=1,
                user_is_premium=True
            )
        ),
        types.KeyboardButton(
            text="Выбрать супергруппу с форумами",
            request_chat=types.KeyboardButtonRequestChat(
                request_id=2,
                chat_is_channel=False,
                chat_is_forum=True
            )
        )
    )
    # WebApp-ов пока нет, сорри :(

    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )













#==================================================================================================#
# Инлайн-кнопки #


# URL-кнопки
# В отличие от обычных кнопок, инлайновые цепляются не к низу экрана, 
# а к сообщению, с которым были отправлены. В этой главе мы рассмотрим два типа таких кнопок: | URL |  <и>  | Callback. |


# Самые простые инлайн-кнопки относятся к типу URL, т.е. «ссылка». Поддерживаются только протоколы HTTP(S) и tg://
# новый импорт
from aiogram.utils.keyboard import InlineKeyboardBuilder

@dp.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )

    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
    )

    # Чтобы иметь возможность показать ID-кнопку,
    # У юзера должен быть False флаг has_private_forwards
    # user_id = 1234567890
    # chat_info = await bot.get_chat(user_id)

    # if not chat_info.has_private_forwards:
    #     builder.row(types.InlineKeyboardButton(
    #         text="Какой-то пользователь",
    #         url=f"tg://user?id={user_id}")
    #     )

    await message.answer(
        'Выберите ссылку',
        reply_markup=builder.as_markup(),
    )


# С URL-кнопками больше обсуждать, по сути, нечего, поэтому перейдём к гвоздю сегодняшней программы — Callback-кнопкам. 







#==================================================================================================#
# Колбэки

# Это очень мощная штука, которую вы можете встретить практически везде. Кнопки-реакции у постов (лайки), меню у 
# @BotFather и т.д. 
# Суть в чём: у колбэк-кнопок есть специальное значение (data), по которому ваше приложение опознаёт, что нажато и что надо сделать.

# И выбор правильного data очень важен! Стоит также отметить, что, в отличие от обычных кнопок, 
# нажатие на колбэк-кнопку позволяет сделать практически что угодно, от заказа пиццы до запуска вычислений на кластере суперкомпьютеров.



@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )

    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )


# Но как же обработать нажатие? Если раньше мы использовали хэндлер на message для обработки входящих сообщений, 
# то теперь будем использовать хэндлер на callback_query для обработки колбэков. 
# Ориентироваться будем на «значение» кнопки, т.е. на её data:
from random import randint

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))

    # Оказывается, сервер Telegram ждёт от нас подтверждения о доставке колбэка, иначе в течение 30 секунд будет показывать специальную иконку.
    # Чтобы скрыть часики, нужно вызвать метод answer() 
    # у колбэка (или использовать метод API answer_callback_query()). В общем случае, в метод answer() можно ничего не передавать


    # await callback.answer(
    #     text="Спасибо, что воспользовались ботом!",
    #     show_alert=True
    # )
    # или просто 
    await callback.answer()







# Перейдём к примеру посложнее. Пусть пользователю предлагается сообщение с числом 0, а внизу три кнопки: +1, -1 

# Здесь хранятся пользовательские данные.
# Т.к. это словарь в памяти, то при перезапуске он очистится
user_data = {}

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
            types.InlineKeyboardButton(text="+1", callback_data="num_incr")
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard



# Новые импорты!
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest

async def update_num_text(message: types.Message, new_value: int):
    # await message.edit_text(
    #     f"Укажите число: {new_value}",
    #     reply_markup=get_keyboard()
    # )
    # Если теперь вы попробуете повторить пример выше, то указанное исключение в этом блоке кода бот просто-напросто проигнорирует.
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Укажите число: {new_value}",
            reply_markup=get_keyboard()
        )


@dp.message(Command("numbers"))
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())


@dp.callback_query(F.data.startswith("num_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "incr":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message, user_value+1)
    elif action == "decr":
        user_data[callback.from_user.id] = user_value-1
        await update_num_text(callback.message, user_value-1)
    elif action == "finish":
        await callback.message.edit_text(f"Итого: {user_value}")

    await callback.answer()











#==================================================================================================#
# Фабрика колбэков
# А теперь представьте, что вам нужно хранить не одно значение, а три: order_1_1994_2731519. Что здесь артикул, цена, количество? 
# А может быть, тут вообще год выпуска? Да и разбиение строки начинает выглядеть страшно: .split("_")[2]. А почему не 1 или 3?


# новые импорты!
from typing import Optional
from aiogram.filters.callback_data import CallbackData

class NumbersCallbackFactory(CallbackData, prefix="fabnum"):
    action: str
    value: Optional[int] = None


# Теперь напишем функцию генерации клавиатуры.
# Здесь нам пригодится метод button(), который автоматически будет создавать кнопку с нужным типом, а от нас требуется только передать аргументы

def get_keyboard_fab():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="-2", callback_data=NumbersCallbackFactory(action="change", value=-2)
    )
    builder.button(
        text="-1", callback_data=NumbersCallbackFactory(action="change", value=-1)
    )
    builder.button(
        text="+1", callback_data=NumbersCallbackFactory(action="change", value=1)
    )
    builder.button(
        text="+2", callback_data=NumbersCallbackFactory(action="change", value=2)
    )
    builder.button(
        text="Подтвердить", callback_data=NumbersCallbackFactory(action="finish")
    )
    # Выравниваем кнопки по 4 в ряд, чтобы получилось 4 + 1
    builder.adjust(4)
    return builder.as_markup()



# Методы отправки сообщения и его редактирования оставляем теми же (в названиях и командах добавим суффикс _fab):
async def update_num_text_fab(message: types.Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Укажите число: {new_value}",
            reply_markup=get_keyboard_fab()
        )

@dp.message(Command("numbers_fab"))
async def cmd_numbers_fab(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())



# Наконец, переходим к главному — обработке колбэков. Для этого в декоратор надо передать класс, 
# колбэки с которым мы ловим, с вызванным методом filter(). 
# Также появляется дополнительный аргумент с названием callback_data (имя должно быть именно таким!), 
# и имеющим тот же тип, что и фильтруемый класс:

@dp.callback_query(NumbersCallbackFactory.filter())
async def callbacks_num_change_fab(
        callback: types.CallbackQuery, 
        callback_data: NumbersCallbackFactory
):
    # Текущее значение
    user_value = user_data.get(callback.from_user.id, 0)
    # Если число нужно изменить
    if callback_data.action == "change":
        user_data[callback.from_user.id] = user_value + callback_data.value
        await update_num_text_fab(callback.message, user_value + callback_data.value)
    # Если число нужно зафиксировать
    else:
        await callback.message.edit_text(f"Итого: {user_value}")
    await callback.answer()




# Ещё немного конкретизируем наши хэндлеры и сделаем отдельный обработчик для числовых кнопок и для кнопки «Подтвердить»
# новый импорт!
from magic_filter import F

# Нажатие на одну из кнопок: -2, -1, +1, +2
@dp.callback_query(NumbersCallbackFactory.filter(F.action == "change"))
async def callbacks_num_change_fab(
        callback: types.CallbackQuery, 
        callback_data: NumbersCallbackFactory
):
    # Текущее значение
    user_value = user_data.get(callback.from_user.id, 0)

    user_data[callback.from_user.id] = user_value + callback_data.value
    await update_num_text_fab(callback.message, user_value + callback_data.value)
    await callback.answer()


# Нажатие на кнопку "подтвердить"
@dp.callback_query(NumbersCallbackFactory.filter(F.action == "finish"))
async def callbacks_num_finish_fab(callback: types.CallbackQuery):
    # Текущее значение
    user_value = user_data.get(callback.from_user.id, 0)

    await callback.message.edit_text(f"Итого: {user_value}")
    await callback.answer()










#==================================================================================================#
# Автоответ на колбэки
# Если у вас очень много колбэк-хэндлеров, на которые нужно либо просто отвечать, либо отвечать однотипно, 
# можно немного упростить себе жизнь, воспользовавшись специальной мидлварью

# Итак, самый простой вариант — это добавить вот такую строчку после создания диспетчера:

# не забываем про новый импорт
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

dp = Dispatcher()
dp.callback_query.middleware(CallbackAnswerMiddleware())

# Увы, ситуации, когда на все колбэк-хэндлеры одинаковый ответ, довольно редки. К счастью, переопределить поведение мидлвари в конкретном 
# обработчике довольно просто: достаточно пробросить аргумент callback_answer и выставить ему новые значения:

# новый импорт!
from aiogram.utils.callback_answer import CallbackAnswer

@dp.callback_query()
async def my_handler(callback: CallbackQuery, callback_answer: CallbackAnswer):
    ... # тут какой-то код
    everything = True
    ok = True
    if everything is ok:
        callback_answer.text = "Отлично!"
    else:
        callback_answer.text = "Что-то пошло не так. Попробуйте позже"
        callback_answer.cache_time = 10
    ... # тут какой-то код





#==================================================================================================#
# Запуск процесса поллинга новых апдейтов
async def main():

    # Запускаем процесс поллинга новых апдейтов
    # await dp.start_polling(bot)

    await dp.start_polling(bot)


# ��лавный цикл
if __name__ == "__main__":
    asyncio.run(main())