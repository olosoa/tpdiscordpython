import discord

client = discord.Client()


@client.event
async def on_ready():
	print("Le bot est pret.")


@client.event
async def on_message(message):  
	#print(message.content) #affiche les messages entrer dans discord dans la console
	
	#reponse de discord si on envoie le mot "ping"
	if message.content.lower() == "ping":		
		await message.channel.send("pong")




client.run("OTU4NjkwODE0NTA5MzUxMDEy.YkRAZQ.YdcjZAmcwCTPVZUWzywEPQ5yZ30")