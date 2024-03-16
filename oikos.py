from discord.ext.commands import Bot
from discord import Intents
from config import config

TOKEN = config.App().Token

# Define the intents
intents = Intents.default()
intents.voice_states = True
intents.messages = True
intents.guilds = True
intents.message_content = True

extensions = ["commands"]

bot = Bot(command_prefix='!', intents=intents) 
    
@bot.event
async def on_ready():
    for extension in extensions:
        await bot.load_extension(extension)
    print(f'Logged in as {bot.user}')
    

bot.run(TOKEN, reconnect=True)
