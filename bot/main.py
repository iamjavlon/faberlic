from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          CallbackQueryHandler,
                          MessageHandler,
                          Filters,
                          PreCheckoutQueryHandler,
                          PicklePersistence)
                          
from core.settings import BOT_ID, DEBUG
import logging

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


updater = Updater('YOUR TOKEN HERE')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()