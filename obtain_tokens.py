from api.Auth import Auth
from api.Friend import Friend
from api.User import User
from api.Messaging import Messaging
import json

auth = Auth('YOUR_EMAIL', 'YOUR_PASSWORD', 'TICKET_UUID', '2FA')

tokens = auth.get_tokens()

f = open('tokens', 'wt', encoding='utf-8')
f.write(json.dumps(tokens))
f.close()

print('Your tokens have been saved in the file \'tokens\'')