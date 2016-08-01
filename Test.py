import sys
import discord
import random
import pull_bot_pass
client = discord.Client()
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

class User():
    def _init_(self, name):
		self.name = name
		self.maxhealth = 10
		self.health = self.maxhealth
		self.attack = 1
	
def start(author, message):
    client.send_message(message.channel, "%s, Prepare to begin" % author)
    menu()

def menu():
	 client.send_message(message.channel, "Attack: %d" % self.attack)
	 client.send_message(message.channel, "Health: %i/%i" % (self.health, self.maxhealth))

password = pull_bot_pass.pull_pass()    
password = 'DJRhynocerous'
client.login('rhinomusicbot@gmail.com', password)
client.accept_invite('https://discord.gg/9nmjV8c')
client.run()
