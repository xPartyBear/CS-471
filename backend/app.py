import argon2
import psycopg2
import pypokedex
from flask import Flask, request, jsonify
from flask_cors import CORS
import accounts

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


# THIS IS A TERRIBLE WAY TO LOGIN!!
@app.route("/login/<username>/<password>/", methods=['GET'])
def login(username, password):
    return accounts.login(username, password)


# THIS IS A TERRIBLE WAY TO LOGIN!!
@app.route("/signup/<username>/<password>/", methods=['GET'])
def signup(username, password):
    return accounts.signup(username, password)


@app.route('/reset', methods=['GET', 'POST'])
def password_reset():
    return accounts.password_reset()


@app.route("/")
def base():
    return "Hello World!"


@app.route("/<dex_num>")
def dex(dex_num):
    pokemon = pypokedex.get(dex=int(dex_num))
    return pokemon.name + " " + str(pokemon.types)


@app.route("/get_db", methods=['GET'])
def get_db():
    # Connect to postgreSQL DB
    db = psycopg2.connect("dbname='postgres' user='softwareengineer' host='73.18.161.233' password='cs471' port='5432'")
    cur = db.cursor()

    # Select all products from the table
    cur.execute('''SELECT * FROM accounts''')

    # Fetch the data
    data = cur.fetchall()

    # close the cursor and connection
    cur.close()
    db.close()
    return data


if __name__ == "__main__":
    db = psycopg2.connect("dbname='postgres' user='softwareengineer' host='73.18.161.233' password='cs471' port='5432'")
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS accounts (name varchar(100) PRIMARY KEY, 
                                                        pass varchar(1000));''')

    # Insert some data into the table
    hashed_password = argon2.PasswordHasher().hash(password=str.encode('password'))
    cur.execute('''INSERT INTO accounts (name, pass) VALUES ('username', %s) ON CONFLICT DO NOTHING ;''',
                (hashed_password,))

    # commit the changes
    db.commit()

    # close the cursor and connection
    cur.close()
    db.close()
    app.run(debug=True)
