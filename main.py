import os
import discord
from keep_alive import keep_alive
import commands

# Instantiate a discord client with intents
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Bot Name
botName = "Jiya"

# Call to print console message after successful login
@client.event
async def on_ready():
    print(f"You have successfully logged in as {client}")

# Send cryptocurrency price in discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip()
    # Check if the message starts with a command prefix
    for command_prefix, action in commands.command_mappings.items():
        if content.startswith(command_prefix):
            command_args = content[len(command_prefix):].strip()
            await action(client, message, command_args)
            break

# Keep Active
keep_alive()

# Bot Credentials
try:
    # Bot Access Token
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    # Run Bot
    client.run(BOT_TOKEN)
except KeyError:
    print("Discord Credentials are not satisfied")
