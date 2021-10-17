from telegram.ext import CallbackContext, ConversationHandler
from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup,
                      ReplyKeyboardMarkup,
                      ReplyKeyboardRemove,
                      KeyboardButton,
                      LabeledPrice)


class Registration:
    """
    Base class for registration
    """

    def start(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id, 'Hello world')