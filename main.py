import discord
from discord.ext import commands


intents = discord.Intents.default()  # All but the THREE privileged ones
intents.message_content = True  # Subscribe to the Message Content intent
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if 'youtube.com/shorts' in message.content:
        await message.delete()
        print("short detectado!")

bot.run(":)")
