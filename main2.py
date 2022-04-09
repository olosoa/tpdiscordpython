import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()



class DocBot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix="/")




doc_bot = DocBot()
doc_bot.run(os.getenv("TOKEN"))