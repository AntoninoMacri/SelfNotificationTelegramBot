from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from telegram.error import Forbidden

print("Il bot si sta avviando...")

# Carica variabili d’ambiente
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
USER_ID = int(os.getenv("USER_ID"))

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    print(f"/start da: {user_id}")
    if user_id == USER_ID:
        try:
            await context.bot.send_message(chat_id=user_id, text="Benvenuto! Da ora posso inviarti notifiche.")
        except Forbidden:
            print(f"⚠️ Il bot NON ha il permesso per scrivere a {user_id}.")
    else:
        try:
            await context.bot.send_message(chat_id=user_id, text="Non sei autorizzato a usare questo bot.")
        except Forbidden:
            print(f"❌ Utente non autorizzato ({user_id}) ha provato a usare il bot, ma il bot non può rispondergli.")

# Handler per messaggi normali
async def notify_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    print(f"Messaggio da: {user_id}")

    if user_id == USER_ID:
        try:
            await context.bot.send_message(chat_id=USER_ID, text=f"Hai scritto: {update.message.text}")
        except Forbidden:
            print(f"⚠️ Il bot non ha il permesso per scrivere all’utente {user_id}.")
    else:
        print(f"Messaggio ignorato da utente non autorizzato ({user_id})")

# Avvio dell'applicazione
app = Application.builder().token(TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (filters.ChatType.GROUPS | filters.ChatType.PRIVATE), notify_user))

print("Il bot è avviato")
app.run_polling()

