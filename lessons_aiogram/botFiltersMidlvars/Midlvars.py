# Мидлвари

# Зачем нужны мидлвари?
# https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/#middlewares-structure



# https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/#middlewares-structure

# Каждая мидлварь, построенная на классах (мы не будем рассматривать иные варианты), должна реализовывать метод __call__() с тремя аргументами:
# handler . event . data.



# Рассмотрим простейшую мидлварь:
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

class SomeMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        print("Before handler")
        result = await handler(event, data)
        print("After handler")
        return result
    



# Рассмотрим несколько примеров мидлварей.
# Передача аргументов в мидлварь


# . Напишем бесполезную, но наглядную "замедляющую" мидлварь, которая будет тормозить обработку входящих сообщений на указанное количество секунд:

import asyncio
from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

class SlowpokeMiddleware(BaseMiddleware):
    def __init__(self, sleep_sec: int):
        self.sleep_sec = sleep_sec

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        # Ждём указанное количество секунд и передаём управление дальше по цепочке
        # (это может быть как хэндлер, так и следующая мидлварь)
        await asyncio.sleep(self.sleep_sec)
        result = await handler(event, data)
        # Если в хэндлере сделать return, то это значение попадёт в result
        print(f"Handler was delayed by {self.sleep_sec} seconds")
        return result
    

# И теперь повесим её на два роутера с разными значениями: - > handlers/username







#=========================================================================================
# Передача данных из мидлвари
# https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/#middleware-store-data


from random import randint
from typing import Any, Callable, Dict, Awaitable
from datetime import datetime
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

# Мидлварь, которая достаёт внутренний айди юзера из какого-то стороннего сервиса
class UserInternalIdMiddleware(BaseMiddleware):
    # Разумеется, никакого сервиса у нас в примере нет,
    # а только суровый рандом:
    def get_internal_id(self, user_id: int) -> int:
        return randint(100_000_000, 900_000_000) + user_id

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]
        data["internal_id"] = self.get_internal_id(user.id)
        return await handler(event, data)



# Мидлварь, которая вычисляет "счастливый месяц" пользователя
class HappyMonthMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        # Получаем значение из предыдущей мидлвари
        internal_id: int = data["internal_id"]
        current_month: int = datetime.now().month
        is_happy_month: bool = (internal_id % 12) == current_month
        # Кладём True или False в data, чтобы забрать в хэндлере
        data["is_happy_month"] = is_happy_month
        return await handler(event, data)