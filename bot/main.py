from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          CallbackQueryHandler,
                          MessageHandler,
                          Filters,
                          PreCheckoutQueryHandler,
                          PicklePersistence)
from bot.src.registration import Registration
from config.settings import DEBUG
import dotenv
import os
import logging

dotenv.load_dotenv()
logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


registration = Registration()


def main():
    updater = Updater(token=os.getenv("BOT_TOKEN"))
    dispatcher = updater.dispatcher


    main_conversation = ConversationHandler(
        entry_points = [
            CommandHandler('start', registration.start)],
        states = {

        },
        fallbacks=[
            CommandHandler('start', registration.start)]
    )
    dispatcher.add_handler(main_conversation)
    

    updater.start_polling()
    updater.idle()