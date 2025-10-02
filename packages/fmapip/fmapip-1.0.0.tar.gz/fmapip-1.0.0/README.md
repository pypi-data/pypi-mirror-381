# FMAPIP - FlorestMessangerAPIPlus
Библиотека, предназначенная для облегчения написания ботов на мессенджере [FlorestMessanger](https://florestmsgs-florestdev4185.amvera.io/) с помощью библиотеки [FlorestMessangerAPI](https://pypi.org/project/florestmessangerapi/)
# Примеры
Используя синхронизацию:
```python
from fmapip import Bot, Message, MessagePlus, set_bot

bot = Bot(
    'your-token', # получить его можно в личном кабинете мессенджера
    'bot-name', # название бота
    '!', # префикс бота
    raise_on_status_code = True # вызвать ошибку, если попытка выполнить код неуспешна
)
set_bot(bot) # чтобы использовать функции fmapip
m = MessagePlus()

@bot.add_command('hello')
def hello(message: Message): # название команды и функции могут не совпадаться
    m.send('Привет!')

bot.run()
```
Используя асинхронизацию:
```python
from fmapip import AsyncBot, AsyncMessagePlus, Message, set_bot

bot = AsyncBot(
    'your-token', # получить его можно в личном кабинете мессенджера
    'bot-name', # название бота
    '!', # префикс бота
    raise_on_status_code = True # вызвать ошибку, если попытка выполнить код неуспешна
)
set_bot(bot) # чтобы использовать функции fmapip
m = AsyncMessagePlus()

@bot.add_command('hello')
async def hello(message: Message): # название команды и функции могут не совпадаться
    await m.send('Привет!')

bot.run()
```
# Документация
Документацию можно прочесть [здесь](https://florestmsgs-florestdev4185.amvera.io/api_docs/python/plus)