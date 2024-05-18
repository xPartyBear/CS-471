import constants
import argon2
import psycopg2
import pypokedex
from flask import Flask, request
from flask_cors import CORS
import accounts

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/get_daily/<day>")
def get_daily(day):
    # TODO: Get the daily Pokemon
    return "To get daily Pokemon for " + day


@app.route("/get_mon/<dex_num>")
@app.route("/get_mon/<dex_num>/<attribute>")
def dex(dex_num, attribute=None):
    pokemon = pypokedex.get(dex=int(dex_num))
    pokemon_json = {
        "dex": pokemon.dex,
        "name": pokemon.name,
        "types": pokemon.types,
        "abilities": pokemon.abilities,
        "height": str(pokemon.height / 10) + " m",
        "weight": str(pokemon.weight / 10) + "kg",
        "sprites": pokemon.sprites,
    }
    if attribute is not None:
        return pokemon_json[attribute]
    return pokemon_json


@app.route("/get_db", methods=['GET'])
def get_db():
    # Connect to postgres DB
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()

    # Select all products from the table
    cur.execute('''SELECT * FROM accounts''')

    # Fetch the data
    data = cur.fetchall()

    # close the cursor and connection
    cur.close()
    db.close()
    return data


@app.route("/login", methods=['POST'])
def login():
    return accounts.login(request)


@app.route("/signup", methods=['POST'])
def signup():
    return accounts.signup(request)


@app.route('/reset', methods=['POST'])
def password_reset():
    return accounts.password_reset(request)


if __name__ == "__main__":
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS accounts (name varchar(100) PRIMARY KEY, 
                                                        pass varchar(1000),
                                                        email varchar(100));''')

    # Insert some data into the table
    hashed_password = argon2.PasswordHasher().hash(password=str.encode('password'))
    cur.execute('''INSERT INTO accounts (name, pass, email) VALUES 
                ('username', %s, 'example@example.com') ON CONFLICT DO NOTHING ;''',
                (hashed_password,))

    # commit the changes
    db.commit()

    # close the cursor and connection
    cur.close()
    db.close()
    app.run(debug=True)
