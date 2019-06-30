import twilio
from twilio.rest import Client 
import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))


account_id = os.getenv('twilio_account_sid')
token = os.getenv('twilio_account_authtoken')

# Account Sid and Auth Token from twilio.com/console

account_sid = account_id
auth_token = token

client = Client(account_sid, auth_token)

message = client.messages.create(
                body = 'First text to send to myself',
                from_ = '+16127125846',
                to = '+19523934701'
            )

print(message)