import os
import discord
from dotenv import load_dotenv

load_dotenv()


default_intents=discord.Intents.default() #permissions par defaut
default_intents.members = True #perissions relative aux membres 

client = discord.Client(intents=default_intents)


#evenement permettant d'afficher en cli que le bot est connecte sur discord
@client.event
async def on_ready():
	print("Le bot est pret.")






#evenement qui permet de gerer l'arrive de nouveaux membres 
@client.event
async def on_member_join(member):
	general_channel: discord.TextChannel = client.get_channel(958694311342522430)
	await  general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")






#evenement qui renvoie des messages du bot 
@client.event
async def on_message(message):  
	#print(message.content) #affiche les messages entrer dans discord dans la console
	
	#reponse de discord si on envoie le mot "ping"
	if message.content.lower() == "ping":		
		await message.channel.send("pong")




client.run(os.getenv("TOKEN")) 