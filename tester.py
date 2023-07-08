# curl 'https://api.twilio.com/2010-04-01/Accounts/AC51aed9f25f1520177abded6658a8a798/Messages.json' -X POST \
# --data-urlencode 'To=+962796371959' \
# --data-urlencode 'From=+14176145045' \
# -u AC51aed9f25f1520177abded6658a8a798:[AuthToken]
# from twilio.rest import Client

# account_sid = 'AC51aed9f25f1520177abded6658a8a798'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+14176145045',
#   to='+962796371959'
# )

# print(message.sid)


