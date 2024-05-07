import os
import smtplib
import ssl
import argon2
import psycopg2
from flask import request


def login(username, password):
    db = psycopg2.connect("dbname='postgres' user='softwareengineer' host='73.18.161.233' password='cs471' port='5432'")
    cur = db.cursor()
    cur.execute('SELECT * FROM accounts WHERE name = %s', (username,))
    account = cur.fetchone()
    cur.close()
    db.close()
    try:
        verify_pass = argon2.PasswordHasher().verify(hash=account[1], password=password)
    except argon2.exceptions.VerifyMismatchError as e:
        print(e)
        verify_pass = False

    if verify_pass:
        return "Logged in successfully!"
    return "Wrong password!"


def signup(username, password):
    db = psycopg2.connect("dbname='postgres' user='softwareengineer' host='73.18.161.233' password='cs471' port='5432'")
    cur = db.cursor()
    hashed_password = argon2.PasswordHasher().hash(password=str.encode(password))
    try:
        cur.execute('''INSERT INTO accounts (name, pass) VALUES (%s, %s);''',
                    (username, hashed_password,))
        db.commit()
    except psycopg2.Error as e:
        print(e)
        cur.close()
        db.close()
        return "User already exists!"

    cur.close()
    db.close()
    return "Account Created!"


def password_reset():
    if request.method == 'POST':
        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host=os.getenv("SMTP_SERVER"), port=int(os.getenv("PORT")), context=context) as server:
            server.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
            # TODO: Send email here

    elif request.method == 'GET':
        return "Password Reset Sent."
