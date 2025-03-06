1. mettere i dati corretti nell'env file, in particolare l'ID. Per ottenere il Tuo ID Telegram: Vai su @userinfobot e scrivigli /start>>>>>Ti risponderà con il tuo ID utente (salvalo).

.env:
export BOT_TOKEN=BOT_TOKEN
export USER_ID=CODICE_TUO_ID

2.1 SE SERVE: pip install python-telegram-bot python-dotenv
2.2 Avviare python .\SelfNotificationBot.py magari come demone o con un gestore di demoni sul server
3. è possibile usare il bot