#Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
class SMSClient:
    account_sid = "ACf181fce995302c0dc8e9209598b8a699"
    auth_token = "9be1ae6ae5f2808e583333262b6442f2"
    client = Client(account_sid, auth_token)

    @classmethod
    def send_message(cls, text): 
        message = cls.client.messages.create(
          body=text,
          from_="+18885745804",
          to="+16196189435"
        )

