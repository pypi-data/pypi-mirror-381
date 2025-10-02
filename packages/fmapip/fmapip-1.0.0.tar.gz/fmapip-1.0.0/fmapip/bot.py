from colorama import Fore, init
from sys import exit
from random import randint

from florestmessangerapi import AsyncBot, Bot, Message
from . import message as _m

bot = None
init()

def set_bot(_bot: AsyncBot | Bot):
    global bot
    bot = _bot
    _m.set_bot(bot)

class BotPlus:
    "Функции для работы с ботом типа Bot"
    def __init__(self, turn_off: str = 'Выключаюсь...', admin_error: str = 'Недостаточно прав!', code_error: str = 'Неверный код!'):
        """Создать класс
        Args:
            turn_off (str): сообщение о выключении бота
            admin_error (str): сообщение о нехватке прав
            code_error (str): сообщение о неверном коде"""
        self.code = 179
        self.tom = turn_off
        self.aem = admin_error
        self.cem = code_error
        self.m = _m.MessagePlus()
        print(f'\n{Fore.YELLOW}* Выбран код по умолчанию (179).\nНе забудьте использовать set_code()!')

    def set_code(self, begin: int = 100, end: int = 999, code: int | None = None):
        """Поставить код для `BotPlus.stop()`
        Args:
            begin (int): от какого числа выбрать код, игнорируется при присутствии `code`. По умолчанию 100
            end (int): до какого числа выбрать код, игнорируется при присутствии `code`. По умолчанию 999
            code (int | None): свой код. По умолчанию None
        ## Примеры использования
        ``` # поставить рандомный код (использовать с 'code = set_code(...)', чтобы получить число)
        set_code() # выберет число от 100 до 999 и поставит его в качестве кода
        set_code(1, 1000) # выберет число от 1 до 1000 и поставит его в качестве кода
        \n# поставить свой код
        set_code(code = 179) # поставит 179 в качестве кода
        code = set_code(code = 179) # то же самое, что и сверху"""
        if not code:
            self.code = randint(begin, end)
        else:
            self.code = code
        print(f'\n{Fore.GREEN}* Поставлен код {self.code}!\n')
        return self.code

    def get_code(self):
        """Получить код для `BotPlus.stop()`
        Returns:
            code (int): код"""
        return self.code

    def stop(self, message: Message):
        """Команда для остановки бота. **Требует** права администрации и код (его можно посмотреть в консоли, если не задан свой код)!
        Args:
           message (Message): сообщение"""
        if not message.is_admin:
            return self.m.send(self.aem)
        if not self.m.get_args(message) or not int(self.m.get_args(message)[0]) == self.code:
            return self.m.send(self.cem)

        self.m.send(self.tom)
        exit()

class AsyncBotPlus:
    "Функции для работы с ботом типа AsyncBot"
    def __init__(self, turn_off: str = 'Выключаюсь...', admin_error: str = 'Недостаточно прав!', code_error: str = 'Неверный код!'):
        """Создать класс
        Args:
            turn_off (str): сообщение о выключении бота
            admin_error (str): сообщение о нехватке прав
            code_error (str): сообщение о неверном коде"""
        self.code = 179
        self.tom = turn_off
        self.aem = admin_error
        self.cem = code_error
        self.m = _m.AsyncMessagePlus()
        print(f'\n{Fore.YELLOW}* Выбран код по умолчанию (179).\nНе забудьте использовать set_code()!')

    def set_code(self, begin: int = 100, end: int = 999, code: int | None = None):
        """Поставить код для `BotPlus.stop()`
        Args:
            begin (int): от какого числа выбрать код, игнорируется при присутствии `code`. По умолчанию 100
            end (int): до какого числа выбрать код, игнорируется при присутствии `code`. По умолчанию 999
            code (int | None): свой код. По умолчанию None
        ## Примеры использования
        ```# поставить рандомный код (использовать с 'code = set_code(...)', чтобы получить число)
        set_code() # выберет число от 100 до 999 и поставит его в качестве кода
        set_code(1, 1000) # выберет число от 1 до 1000 и поставит его в качестве кода
        \n# поставить свой код
        set_code(code = 179) # поставит 179 в качестве кода
        code = set_code(code = 179) # то же самое, что и сверху"""
        if not code:
            self.code = randint(begin, end)
        else:
            self.code = code
        print(f'\n{Fore.GREEN}* Поставлен код {self.code}!\n')
        return self.code

    def get_code(self):
        """Получить код для `BotPlus.stop()`
        Returns:
            code (int): код"""
        return self.code

    async def stop(self, message: Message):
        """Команда для остановки бота. **Требует** права администрации и код (его можно посмотреть в консоли, если не задан свой код)!
        Args:
           message (Message): сообщение"""
        if not message.is_admin:
            return await self.m.send(self.aem)
        if not self.m.get_args(message) or not int(self.m.get_args(message)[0]) == self.code:
            return await self.m.send(self.cem)

        await self.m.send(self.tom)
        await exit()