import os
from twilio.rest import Client

client = Client()

from_whatsapp = 'whatsapp:+85296516506'
to_whatsapp='whatsapp:LlhnVvkq8Ze7eGHV7qXUvB'

message = client.messages.create(body='test',media_url='https://demo.twilio.com/owl.png',from_=from_whatsapp,to=to_whatsapp)

print(message.sid)