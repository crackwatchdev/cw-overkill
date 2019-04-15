import praw, configparser, os, sys, time
from termcolor import colored
config = configparser.ConfigParser()
config.read('settings.ini')

def login():
	username = config.get('Credentials', 'Username')
	password = config.get('Credentials', 'Password')
	client_id = config.get('Credentials', 'Client_ID')
	client_secret = config.get('Credentials', 'Client_Secret')
	if username == "replace_me" or password == "replace_me" or client_id == "replace_me" or client_secret == "replace_me":
		print(colored("ERROR: Please fill out login credentials! (You can do that in settings.ini!)", 'red'))
		os.system("pause>nul")
		sys.exit()
	try:
		client = praw.Reddit(
			username = username,
			password = password,
			client_id = client_id,
			client_secret = client_secret,
			user_agent = "crackwatch reddit bot"
		)
		print(colored("SUCCESS: Logged in as u/{}!".format(username), 'green'))
		return client
	except:
		print(colored("ERROR: Invalid credentials! Please check settings.ini!", 'red'))
		os.system("pause>nul")
		sys.exit()


client = login()
