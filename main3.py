import os
from discord.ext import commands
from dotenv import load_dotenv
import logging
logging.basicConfig(filename='journal.log', encoding='utf-8')
load_dotenv()




class DocBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="/")


    async def on_ready(self):        
        print("Le bot est pret.")          


    async def on_message(self,message):
        if message.content.lower() == "ping":       
                await message.channel.send("pong")



doc_bot = DocBot()
doc_bot.run(os.getenv("TOKEN"))