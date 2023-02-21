from api.Auth import Auth
from api.Friend import Friend
import json


with open('tokens', encoding='utf-8') as data_file:
	data = json.loads(data_file.read())

new_token_pair = Auth.GrabNewTokens(data['refresh'])

tokens = {
	"oauth": new_token_pair[0],
	"refresh": new_token_pair[1],
	"npsso": data['npsso'] # saved above!
}

friend = Friend(tokens)
friend_list = friend.my_friends()

friend_string = ''
if(bool(friend_list)):
	for key, value in friend_list.items():
		if(value != ""):
			friend_string += key+' is playing '+value+"\n"
		else:
			friend_string += key+' is online'+"\n"
else:
	friend_string = 'No friends online'

print(friend_string.replace('ÂŽ', ''))