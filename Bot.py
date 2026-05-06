import discord
import subprocess

TOKEN = "DEIN_DISCORD_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!start":
        subprocess.run(["wakeonlan", "30:56:0f:7e:3c:e3"])
        await message.channel.send("Server wird gestartet 🔥")

client.run(TOKEN)
