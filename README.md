1. mettere i dati corretti nell'env file. In particolare l'ID. 
Per ottenere il Tuo ID Telegram: Vai su @userinfobot e scrivigli /start>>>>>Ti risponderà con il tuo ID utente (salvalo).

2. Creare un .env file:
export BOT_TOKEN=BOT_TOKEN
export USER_ID=CODICE_TUO_ID

3. SE SERVE: pip install python-telegram-bot python-dotenv
4. Avviare python .\SelfNotificationBot.py (magari come demone o con un gestore di demoni sul server)
5. Per usare il bot va inserito in un gruppo telegram con permessi lettura messaggi o amministratore
