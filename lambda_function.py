from twilio.rest import Client
from os import environ

def lambda_handler(event, context):
  result = send_message(event)
  return result

def send_message(event):
  body = event['body']
  to = event['to']
  from_ = environ['from']
  client = Client(environ['account_sid'], environ['auth_token'])
  msg = client.messages.create(
    body=body,
    from_=from_,
    to=to)
  return {
    'date_created': str(msg.date_created),
    'to': msg.to,
    'from': msg.from_,
    'error_message': msg.error_message,
    'status': msg.status
  }