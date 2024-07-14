import mysql.connector
from mysql.connector import errorcode


config = {
    'host': 'localhost',
    'user': 'user',
    'password': 'user',
    'database': 'textdb'
}


def connect_db(config: dict):
    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Há um problema com o seu usuário ou senha.')
        else:
            print(e)
    else:
        return conn


def get_text(sign_name: str):
    conn = connect_db(config)

    cur = conn.cursor()

    cur.execute(f'SELECT horoscope_text FROM texts WHERE sign_name="{sign_name}"')
    text = cur.fetchone()

    conn.close()

    return text
