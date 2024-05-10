import smtplib
import ssl
import argon2
import psycopg2
import constants


def login(username, password, request):
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
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


def signup(username, password, request):
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
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


def password_reset(request):
    if request.method == 'POST':
        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host=constants.SMTP_SERVER, port=constants.SMTP_PORT, context=context) as server:
            server.login(user=constants.EMAIL, password=constants.EMAIL_PASSWORD)
            # TODO: Send email here

    elif request.method == 'GET':
        return "Password Reset Sent."
