import os
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)
from dotenv import load_dotenv

load_dotenv()

def send_notification(visit):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('ADMIN_CHAT_ID')
    
    updater = Updater(token=bot_token, use_context=True)
    message = f"""
    New Appointment!
    Client: {visit.name}
    Phone: {visit.phone}
    Master: {visit.master}
    Service: {visit.service}
    """
    updater.bot.send_message(chat_id=chat_id, text=message)
