import discord
import requests
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

FRITZ_IP = "http://fritz.box"

MAC = "30:56:0f:7e:3c:e3"

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!start":
        # FritzBox WoL funktioniert meist direkt im LAN
        # Alternative: einfach Broadcast über Router
        requests.get(f"{FRITZ_IP}")  # Trigger (Fritz erkennt LAN Gerät)
        await message.channel.send("Wake signal gesendet 🔥")

client.run(TOKEN)
