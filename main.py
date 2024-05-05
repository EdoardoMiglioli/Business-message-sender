from dotenv import load_dotenv
import os
import psycopg2
from twilio.rest import Client

load_dotenv()

conn = psycopg2.connect(
    dbname=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    host=os.environ.get("DB_HOST"),
    port='5432'
)

cur = conn.cursor()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message_text = ""

def get_phone_numbers():
     cur.execute("SELECT tel FROM business;")
     rows = cur.fetchall()

     return [row[0] for row in rows if row[0]]

def send_message(number):
     message = client.messages.create(
                         body="Hi!",
                         from_=os.environ['PHONE_NUMBER'],
                         to={number}
                    )

print(get_phone_numbers())