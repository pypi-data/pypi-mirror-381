"""## fmapip - FlorestMessangerAPIPlus
Дополнительные функции, облегачющие разработку кода на библиотеке `florestmessangerapi`"""

from . import message, bot as _bot
from florestmessangerapi import AsyncBot, Bot, Message
from florestmessangerapi import Post, User # не будут использованы в fmapip, но добавлены ради совместимости с fmapi

def set_bot(bot: AsyncBot | Bot):
    """Выбрать бота для fmapip
    Args:
        bot (AsyncBot | Bot): бот с параметрами"""
    message.set_bot(bot)
    _bot.set_bot(bot)

# для удобства импортов
MessagePlus = message.MessagePlus
AsyncMessagePlus = message.AsyncMessagePlus
BotPlus = _bot.BotPlus
AsyncBotPlus = _bot.AsyncBotPlus