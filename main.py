import discord
from discord.ext import commands
import json
# Carga de datos guardados
with open('links_borrados.json', 'r') as f:
    data = json.load(f)
    links_borrados = data.get('links_borrados', 0)


intents = discord.Intents.default()  # All but the THREE privileged ones
intents.message_content = True  # Subscribe to the Message Content intent
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    global links_borrados
    if 'youtube.com/shorts' in message.content:
        await message.delete()
        links_borrados += 1
        # Actualización del archivo JSON
        with open('links_borrados.json', 'w') as f:
            json.dump({'links_borrados': links_borrados}, f)

        # Actualización del estado del bot
        await bot.change_presence(activity=discord.Game(name=f'Borrados {links_borrados} links.'))
        print("short detectado!")

bot.run(":)")
