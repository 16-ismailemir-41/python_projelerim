from dotenv import load_dotenv
load_dotenv()

import os
import random

TOKEN = os.environ.get("DISCORD_TOKEN")


import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('selam'):
        await message.channel.send(f"selam ben {bot.user.name}")
    if message.content.startswith('nasılsın'):
        await message.channel.send(f"teşekkürler ben iyiyim sen nasılsın?")
    if message.content.startswith('naber'):
        await message.channel.send(f"teşekkürler ben iyi senden naber?")
    await bot.process_commands(message)

@bot.command("topla")
async def topla(ctx, *sayilar):
    toplam =  0     
    for sayi in sayilar:
        toplam += int(sayi)
    await ctx.channel.send(toplam)

@bot.command("cikar")
async def cikar(ctx, *sayilar):
    cikarilan = int(sayilar[0])  
    for sayi in sayilar[1:]:  
        cikarilan -= int(sayi)
    await ctx.channel.send(cikarilan)

caps_list = os.listdir("./caps")

@bot.command("capss")
async def caps(ctx):
    chosen_caps = random.choice(caps_list)
    chosen_caps = os.path.join("./caps", chosen_caps)
    with open(chosen_caps, "rb") as doc:
        file = discord.file(doc)
    await ctx.send(file = file)
    

bot.run(TOKEN)                   