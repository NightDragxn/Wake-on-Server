import discord
import requests
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

FRITZ_URL = "http://fritz.box:49000/upnp/control/hosts"  # wird gleich ersetzt

@client.event
async def on_ready():
    print(f"Bot online: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!start":
        try:
            # einfache WoL über FritzBox (wir ersetzen das gleich sauber)
            requests.get("http://fritz.box")
            await message.channel.send("Server wird gestartet 🔥")
        except Exception as e:
            await message.channel.send(f"Fehler: {e}")

client.run(TOKEN)
