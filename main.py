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

message_text = (
"""
Questo messaggio è riservato ai propretari
 dei bagni della Riviera. Ti abbiamo allegato un 
 questionario che ha l'obiettivo di darti la possibilità
 di condividerci la tua opinione per capire se il nostro
 prodotto può aiutare il tuo business. Tutte le informazioni sono
 descritte nel questionario. Grazie mille per il tuo tempo.

 per qualsiasi informazione, scrivi pure a questo numero: 

 https://forms.gle/mw7kP7NdTnPCERRU8
"""
)

def get_phone_numbers():
     cur.execute("SELECT tel FROM business;")
     rows = cur.fetchall()

     raw_numbers =  [[num.replace(" ", "") for num in row[0] if num[0] != "0"] for row in rows if row[0]] 

     return [tel for tel in raw_numbers if tel]

def send_message(number):
     message = client.messages.create(
                         body={message_text},
                         from_=os.environ['PHONE_NUMBER'],
                         to={"+39" + number}
                    )

phone_numbers = get_phone_numbers()

messages_sent = 0

for tel_array in phone_numbers:
     for tel in tel_array:
          messages_sent += 1
          send_message(tel)

print(messages_sent)