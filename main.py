
from cmath import exp
from unittest import expectedFailure
import discord

import config
#import customPrefix

import json

from discord.ext import commands

#------====== Load Guild Specific Prefix ======------
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

intents1 = discord.Intents.default()
intents1.members = True

client = commands.Bot(command_prefix = get_prefix, intents=intents1)

#------====== NickBot Startup ======------
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await client.change_presence(activity=discord.Game(name = "Creating Myself"))



@client.event
async def on_message(message):
    if message.author == client.user:       #Checks to See if itself sent the message
        return

    if  message.content[0] != '!':          #Checks to see if its a command
        return
    


    await message.channel.send("THIS WORKS?")
    await client.process_commands(message)


client.run(config.DISCORD_TOKEN)