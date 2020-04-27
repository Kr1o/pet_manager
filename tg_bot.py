import logging
from functools import wraps

from telegram import ChatAction
from telegram.ext import Updater, CommandHandler

import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context, *args, **kwargs)

    return command_func


@send_typing_action
def start(update, context):
    user_id, user_first_name = update.effective_user.id, update.effective_user.first_name
    msg = f'Привет {user_first_name}! Твой уникальный идентификационный номер: {user_id}. Сейчас я поищу тебя в базе...'
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(config.tg_bot_token, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
