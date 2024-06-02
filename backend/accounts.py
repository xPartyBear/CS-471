import smtplib
import ssl
import argon2
import psycopg2
import constants
from flask import jsonify


def login(request):
    data = request.get_json()
    print(data)
    email = data['email'].strip("'")
    password = data['password'].strip("'")

    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    cur.execute(f'''SELECT * FROM "{constants.USER_TABLE}" WHERE email = %s''', (email,))
    account = cur.fetchone()
    print (account)
    cur.close()
    db.close()
    try:
        verify_pass = argon2.PasswordHasher().verify(hash=account[2], password=password)
    except argon2.exceptions.VerifyMismatchError as e:
        print(e)
        verify_pass = False

    if verify_pass:
        # say they logged in successfully and give them their username
        # should send them a session id or something but whatever
        return jsonify(res="Passed", username=account[1])
    return jsonify(res="Failed", data="Wrong password!")


def signup(request):
    data = request.get_json()
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
        cur.execute(f'''SELECT * FROM "{constants.USER_TABLE}" WHERE email = %s;''', (email,))
        account = cur.fetchone()
        cur.execute(f'''SELECT * FROM "{constants.USER_TABLE}" WHERE username = %s;''', (username,))
        account2 = cur.fetchone()
        if account is None and account2 is None:
            cur.execute(f'''INSERT INTO "{constants.USER_TABLE}" (username, password, email) VALUES (%s, %s, %s);''',
                        (username, hashed_password, email,))
            db.commit()
            cur.close()
            db.close()
            return jsonify(res="Passed", data="Account Created")
        cur.close()
        db.close()
        return jsonify(res="Failed", data="Account Already Exists")
    except psycopg2.Error as e:
        print(e)
        return jsonify(res="Failed", data="Error Signing Up")


def password_reset(request):
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=constants.SMTP_SERVER, port=constants.SMTP_PORT, context=context) as server:
        server.login(user=constants.EMAIL, password=constants.EMAIL_PASSWORD)
        # TODO: Send email here
