import os
from dotenv import load_dotenv

# load_dotenv(".backend_env")

SMTP_SERVER = os.getenv("SMTP_SERVER", default="smtp.gmail.com")
SMTP_PORT = os.getenv("SMTP_PORT", default="587")

##
if os.getenv("EMAIL") == '' or os.getenv("EMAIL") is None:
    raise ValueError("EMAIL environment variable not set")
else:
    EMAIL = os.getenv("EMAIL")

##
if os.getenv("EMAIL_PASSWORD") == '' or os.getenv("EMAIL_PASSWORD") is None:
    raise ValueError("EMAIL_PASSWORD environment variable not set")
else:
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

##
if os.getenv("DATABASE_PASSWORD") == '' or os.getenv("DATABASE_PASSWORD") is None:
    raise ValueError("DATABASE_PASSWORD environment variable not set")
else:
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

##
if os.getenv("DATABASE_HOST") == '' or os.getenv("DATABASE_HOST") is None:
    raise ValueError("DATABASE_HOST environment variable not set")
else:
    DATABASE_HOST = os.getenv("DATABASE_HOST")

##
if os.getenv("DATABASE_PORT") == '' or os.getenv("DATABASE_PORT") is None:
    DATABASE_PORT = str(5432)
else:
    DATABASE_PORT = os.getenv("DATABASE_PORT")

##
if os.getenv("DATABASE_NAME") == '' or os.getenv("DATABASE_NAME") is None:
    DATABASE_NAME = "postgres"
    print("Recommend changing DATABASE_NAME environment variable from the default PostgreSQL database")
else:
    DATABASE_NAME = os.getenv("DATABASE_NAME")

##
if os.getenv("DATABASE_USER") == '' or os.getenv("DATABASE_USER") is None:
    DATABASE_USER = "postgres"
    print("Recommend changing DATABASE_USER environment variable from the default PostgreSQL user")
else:
    DATABASE_USER = os.getenv("DATABASE_USER")
