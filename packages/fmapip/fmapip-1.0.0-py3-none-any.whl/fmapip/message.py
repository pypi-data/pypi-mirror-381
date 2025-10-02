from florestmessangerapi import AsyncBot, Bot, Message, User

bot = None
def set_bot(_bot: AsyncBot | Bot):
    global bot
    bot = _bot

class MessagePlus:
    "Функции для работы с сообщениями с помощью бота типа Bot"
    def __init__(self):
        pass

    def is_has_args(self, message: Message):
        """Возвращает True, если сообщение имеет аргументов, в противном случае False
        Args:
            message (Message): сообщение
        Returns:
            is_has (bool): сообщение имеет аргументов или нет"""
        return self.get_args(message) != [None]
    
    def get_args(self, message: Message):
        """Возвращает аргументы из команды в виде списка
        Args:
            message (Message): сообщение
        Returns:
            args (list): аргументы"""
        if len(message.content.split()) > 2:
            if len(message.content.split()) > 3: # больше 1го аргумента
                return message.content.split()[2:] # без префикса и команды
            return [message.content.split()[2]]
        return [None]

    def get_args_in_str(self, message: Message, split: str = ' '):
        """Возвращает аргументы из команды в виде строки
        Args:
            message (Message): сообщение
            split (str): разделение между аргументами
        Returns:
            args (str | list[None]): аргументы, соединённые `split`'ом. Если аргументы отсутствуют - [None]"""
        args = self.get_args(message)
        if args != [None]:
            return split.join(args)
        return args # возвращает [None]

    def send(self, context, is_text: bool = True):
        """Замена функциям send_message и send_media
Args:
    context: сообщение или путь к медиа
    is_text (bool): отправляется текст или нет (использовать при указании пути)
## Примеры использования
```# отправка текста
send('текст')
# отправка медиа
send('C:/путь/к/med.ia')
# отправка пути к медиа как текст
send('C:/путь/к/med.ia', False)"""
        try:
            if is_text:
                return bot.send_media(open(context, 'rb'))
            bot.send_message(context)
        except:
            bot.send_message(context)
    
    def send_dm(self, context, users: str | list = None):
        """Улучшенная функция `Bot.send_dm()`
Args:
    context: сообщение **(НЕ ПОДДЕРЖИВАЕТ МЕДИА)**
    users (str, list): каким пользователям отправить. По умолчанию всем (`Bot.get_users()`)
## Примеры использования
```# отправка текста всем
send_dm('текст')
# отправка текста кому-то
send_dm('текст', 'some_username')
# отправка текста определённым пользователям
send_dm('текст', ['some1', 'some2', 'some3'])"""
        if type(users) == str:
            users = [users]
        elif not users:
            users = bot.get_users()
        
        for user in users:
            if type(user) != User:
                user = User(user)
            bot.send_dm(user.username, context)

class AsyncMessagePlus:
    "Функции для работы с сообщениями с помощью бота типа AsyncBot"
    def __init__(self):
        pass

    def is_has_args(self, message: Message):
        """Возвращает True, если сообщение имеет аргументов, в противном случае False
        Args:
            message (Message): сообщение
        Returns:
            is_has (bool): сообщение имеет аргументов или нет"""
        return self.get_args(message) != [None]

    def get_args(self, message: Message):
        """Возвращает аргументы из команды в виде списка
        Args:
            message (Message): сообщение
        Returns:
            args (list): аргументы"""
        if len(message.content.split()) > 2:
            if len(message.content.split()) > 3: # больше 1го аргумента
                return message.content.split()[2:] # без префикса и команды
            return [message.content.split()[2]]
        return [None]

    def get_args_in_str(self, message: Message, split: str = ' '):
        """Возвращает аргументы из команды в виде строки
        Args:
            message (Message): сообщение
            split (str): разделение между аргументами
        Returns:
            args (str): аргументы, соединённые `split`'ом. Если аргументы отсутствуют - возвращает `'None'`"""
        args = self.get_args(message)
        if args != [None]:
            return split.join(args)
        return 'None'

    async def send(self, context, is_text: bool = True):
        """Замена функциям send_message и send_media
Args:
context: сообщение или путь к медиа
is_text (bool): отправляется текст или нет (использовать при отправки пути как текст)
## Примеры использования
```# отправка текста
send('текст')
# отправка медиа
send('C:/путь/к/med.ia')
# отправка пути к медиа как текст
send('C:/путь/к/med.ia', False)"""
        try:
            if is_text:
                return await bot.send_media(open(context, 'rb'))
            await bot.send_message(context)
        except:
            await bot.send_message(context)
    
    async def send_dm(self, context, users: str | list = None):
        """Улучшенная функция `AsyncBot.send_dm()`
Args:
    context: сообщение **(НЕ ПОДДЕРЖИВАЕТ МЕДИА)**
    users (str, list): каким пользователям отправить. По умолчанию всем (`AsyncBot.get_users()`)
## Примеры использования
```# отправка текста всем
send_dm('текст')
# отправка текста кому-то
send_dm('текст', 'some_username')
# отправка текста определённым пользователям
send_dm('текст', ['some1', 'some2', 'some3'])"""
        if type(users) == str:
            users = [users]
        elif not users:
            users = await bot.get_users()
        
        for user in users:
            if type(user) != User:
                user = User(user)
            await bot.send_dm(user.username, context)