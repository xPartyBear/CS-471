import smtplib
import ssl
import argon2
import psycopg2
import constants
from flask import jsonify


def login(request):
    data = request.get_json()
    print(data)
    email = data['email']
    password = data['password']

    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
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
        return jsonify(res="Passed", username=account[2])
    return "Wrong password!"


def signup(request):
    data = request.get_json()['data']
    print(data)
    email = data['email']
    password = data['password']
    username = data['username']

    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    hashed_password = argon2.PasswordHasher().hash(password=str.encode(password))
    try:
        cur.execute('''INSERT INTO accounts (name, pass, email) VALUES (%s, %s, %s);''',
                    (username, hashed_password, email,))
        db.commit()
    except psycopg2.Error as e:
        print(e)
        cur.close()
        db.close()
        return "User already exists!"

    cur.close()
    db.close()
    return "Account Created!"


def password_reset(request):
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=constants.SMTP_SERVER, port=constants.SMTP_PORT, context=context) as server:
        server.login(user=constants.EMAIL, password=constants.EMAIL_PASSWORD)
        # TODO: Send email here
