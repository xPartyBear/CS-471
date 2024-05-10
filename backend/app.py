import psycopg2
import argon2
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=['POST'])
def ping():
    print("HELP",request.get_json())
    return jsonify(data = 'pong')


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


# THIS IS A TERRIBLE WAY TO LOGIN!!
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    email = data['email']
    password = data['password']

    db = psycopg2.connect("dbname='postgres' user='softwareengineer' host='73.18.161.233' password='cs471' port='5432'")
    cur = db.cursor()
    cur.execute('SELECT * FROM accounts WHERE email = %s', (email,))
    account = cur.fetchone()
    cur.close()
    db.close()
    try:
        verify_pass = argon2.PasswordHasher().verify(hash=account[1], password=password)
    except argon2.exceptions.VerifyMismatchError as e:
        print(e)
        verify_pass = False

    if verify_pass:
        # say they logged in successfully and give them their username
        return jsonify(res="Passed",username=account[2])
    return "Wrong password!"


# THIS IS A TERRIBLE WAY TO SIGNUP!!
@app.route("/signup", methods=['POST'])
def signup():
    data = request.get_json()['data']
    print(data)
    email = data['email']
    password = data['password']
    username = data['username']
    
    db = psycopg2.connect("dbname='postgres' user='softwareengineer' host='73.18.161.233' password='cs471' port='5432'")
    cur = db.cursor()
    hashed_password = argon2.PasswordHasher().hash(password=str.encode(password))
    try:
        cur.execute('''INSERT INTO accounts (name, pass, email) VALUES (%s, %s, %s);''',
                    (username, hashed_password, email))
        db.commit()
    except psycopg2.errors.UniqueViolation as e:
        print(e)
        cur.close()
        db.close()
        return "User already exists!"

    cur.close()
    db.close()
    return "Account Created!"


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
