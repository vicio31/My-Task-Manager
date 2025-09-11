# Importa la classe Flask dalla libreria flask
from flask import Flask
from dotenv import load_dotenv #importa la funzione per caricare .env
import os
import mysql.connector

# Carico le variabili del file .env nell'ambiente
load_dotenv()

# Crea un'istanza dell'applicazione Flask. __name__ è una variabile speciale di Python.
app = Flask(__name__)

# Configuro l'app con le variabili d'ambiente
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

# Funzione per creare una connessione al database
def get_db_connector():
    conn = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME')
    )
    return conn


# Definisce cosa succede quando un utente visita la homepage ("/")
@app.route('/')
def hello():
    return 'HELLO WORD, this is my tasks manager'

    # Fase di debuggin: CONNESSIONE AL DATABASE RIUSCITA CORRETTAMENTE
    # try:
    #     # Provo a stabilire una connessione
    #     conn = get_db_connector()
    #     # se arriva qui, la connessione è ok
    #     conn.close() # per chiudere la connessione
    #     return 'Connessione al database riuscita!'
    # except mysql.connector.Error as err:
    #     # se qualcosa va storto, cattura l'errore e mostralo
    #     return f"Errore di connessione: {err}"

# Questo blocco fa sì che l'app si avvii solo se eseguiamo direttamente questo script.
if __name__ == '__main__':
    app.run(debug=True)