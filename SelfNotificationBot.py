from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters
import os
from dotenv import load_dotenv

print("Il bot si sta avviando...")

# Carica le variabili d’ambiente
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
USER_ID = int(os.getenv("USER_ID"))

async def notify_user(update: Update, context):
    if update.message.from_user.id == USER_ID:
        bot = context.bot
        await bot.send_message(chat_id=USER_ID, text=f"Hai scritto: {update.message.text}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, notify_user))

print("Il bot è avviato")

app.run_polling()

