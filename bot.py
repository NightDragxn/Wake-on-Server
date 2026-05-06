import discord
import wakeonlan
import os

TOKEN = os.getenv("TOKEN")
MAC = os.getenv("MAC")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot läuft als {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "!start":
        wakeonlan.send_magic_packet(MAC, ip_address="255.255.255.255", port=9)
        await message.channel.send("Wake signal gesendet!")

client.run(TOKEN)
