from telegram.ext import CallbackContext, ConversationHandler
from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup,
                      ReplyKeyboardMarkup,
                      ReplyKeyboardRemove,
                      KeyboardButton,
                      LabeledPrice)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from users.models import User



class Registration:
    """
    Base class for registration
    """

    def start(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        first_name = update.effective_user.first_name
        last_name = update.effective_user.last_name
        username = (
            "@" + update.effective_user.username) if update.effective_user.username is not None else None
        context.bot.send_message(chat_id, f'Hello {username}. Welcome to online shop for products from Faberlic')
        
        # User.objects.create(id=chat_id, first_name= f'{first_name}', last_name= f'{last_name}', username=f'{username}')