1. Creare un .env file:
export BOT_TOKEN=BOT_TOKEN
export USER_ID=CODICE_TUO_ID

2. Mettere i dati corretti nell'env file. In particolare l'ID. Per ottenere il Tuo ID Telegram: Vai su @userinfobot (quello con centinaia di migliaia di utenti) e scrivigli /start.
La risposta sarà del tipo: 
👤 Your Telegram ID: 123456789
🗣 First name: Nome
🌐 Language: it

3. Copiare il tuo ID utente al posto di CODICE_TUO_ID nell'env file
3. SE SERVE: pip install python-telegram-bot python-dotenv
4. Avviare python .\SelfNotificationBot.py [o con python3 SelfNotificationBot.py ] (magari come demone o con un gestore di demoni sul server)
5. Per usare il bot va inserito in un gruppo telegram con permessi lettura messaggi o amministratore
6. Quindi per fare i permessi al bot di poter scrivere all'utente che ha messo il proprio codice id bisogna scrivere un messaggio al bot in privato e quindi premere avvia. Il bot riponderà "Benvenuto! Da ora posso inviarti notifiche."
7. Andare sul gruppo e inserire un messagio e vedere se il bot reinvia in privato il messaggio mandato.
