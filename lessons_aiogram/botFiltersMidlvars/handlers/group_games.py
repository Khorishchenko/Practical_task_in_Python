from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command

from filters.chat_type import ChatTypeFilter

router = Router()

# И теперь повесим её на два роутера с разными значениями:

from aiogram import Router
from Midlvars import SlowpokeMiddleware
from Midlvars import HappyMonthMiddleware

# Где-то в другом месте
router1 = Router()
router2 = Router()

router1.message.middleware(SlowpokeMiddleware(sleep_sec=5))
router2.message.middleware(SlowpokeMiddleware(sleep_sec=10))

router.message.middleware(HappyMonthMiddleware())



# @router.message(
#     ChatTypeFilter(chat_type=["group", "supergroup"]),
#     Command(commands=["dice"]),
# )
# async def cmd_dice_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.DICE)


# @router.message(
#     ChatTypeFilter(chat_type=["group", "supergroup"]),
#     Command(commands=["basketball"]),
# )
# async def cmd_basketball_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.BASKETBALL)



# Вроде всё хорошо, но что, если у нас будет не 2 хэндлера, а 10? 
# Придётся каждому указывать наш фильтр и нигде не забыть. 
# К счастью, фильтры можно цеплять прямо на роутеры! 
# В этом случае проверка будет выполнена ровно один раз, когда апдейт долетит до этого роутера

router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.message(Command("dice"))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(Command("basketball"))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)







#===============================================================================================
# Магические фильтры
#  И вы правы! Действительно, для некоторых простых случаев, 
# когда нужно просто проверить значение поля объекта, 
# создавать отдельный файл с фильтром, потом его импортировать, смысла мало.



from aiogram import F

# Здесь F - это message
@router.message(F.photo)
async def photo_msg(message: Message):
    await message.answer("Это точно какое-то изображение!")



# И теперь, обладая таким сакральным знанием, мы легко можем заменить фильтр ChatTypeFilter на магию:
@router.message.filter(F.chat.type.in_({"group", "supergroup"}))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)




# (другими словами, отсекаем форварды от анонимных админов, реагируя только на форварды из каналов):
from aiogram import F
from aiogram.types import Message, Chat

@router.message(F.forward_from_chat[F.type == "channel"].as_("channel"))
async def forwarded_from_channel(message: Message, channel: Chat):
    await message.answer(f"This channel's ID is {channel.id}")



# Ещё более сложный пример. При помощи magic-filter можно проверить элементы списка на соответствие какому-нибудь признаку:
from aiogram.enums import MessageEntityType

@router.message(F.entities[:].type == MessageEntityType.EMAIL)
async def all_emails(message: Message):
    await message.answer("All entities are emails")


@router.message(F.entities[...].type == MessageEntityType.EMAIL)
async def any_emails(message: Message):
    await message.answer("At least one email!")





# MagicData¶
# Наконец, слегка затронем MagicData. Этот фильтр позволяет подняться на уровень выше в плане фильтров, 
# и оперировать значениями, которые передаются через мидлвари или в диспетчер/поллинг/вебхук. 
# Предположим, у вас есть популярный бот.
# https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/#magic-data






# Передача данных из мидлвари
from aiogram.filters import Command
@router.message(Command("happymonth"))
async def cmd_happymonth(
        message: Message, 
        internal_id: int, 
        is_happy_month: bool
):
    phrases = [f"Ваш ID в нашем сервисе: {internal_id}"]
    if is_happy_month:
        phrases.append("Сейчас ваш счастливый месяц!")
    else:
        phrases.append("В этом месяце будьте осторожнее...")
    await message.answer(". ".join(phrases))
