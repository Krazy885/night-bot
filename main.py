import disnake
from disnake.ext import commands
import os
from config import settings

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, test_guilds=[1079792436727009280])


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
        print(f'ког {file} готов')

bot.run(settings['token'])
