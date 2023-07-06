import os
import discord
from keep_alive import keep_alive
import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)

botName = "Jiya"

@client.event
async def on_ready():
    print(f"You have successfully logged in as {client}")
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip()
    for command_prefix, action in commands.command_mappings.items():
        if content.startswith(command_prefix):
            command_args = content[len(command_prefix):].strip()
            await action(client, message, command_args)
            break
          
keep_alive()

try:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    client.run(BOT_TOKEN)
except KeyError:
    print("Discord Credentials are not satisfied")
