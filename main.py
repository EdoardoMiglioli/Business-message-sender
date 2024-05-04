import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message_text = ""

message = client.messages.create(
                     body="Hi!",
                     from_=os.environ['PHONE_NUMBER'],
                     to='number'
                )

print(message)
