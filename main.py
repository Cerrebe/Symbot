import discord
from discord.channel import DMChannel
from discord.ext import commands
from discord.utils import get
from discord import DMChannel
import json
import os

# Essential Functions
def GetJsonElement(file, element, element2=None, id=None):
    with open(file) as JsonFile:
        return json.load(JsonFile)[element]


# Variables
devs = [212620735754010624]
configjson = "config.json"
token = GetJsonElement(configjson, "token")
client = commands.Bot(command_prefix="!re")

# Regular Functions
async def AddReaction(ctx, emojis):
    await ctx.add_reaction(emojis)


# Events
@client.event
async def on_ready():
    print("Logged on as {0}!".format(client.user))


@client.event
async def on_message(message):
    if "$!#" in message.content and message.author == client.user:
        editedmsg = message.content.replace("$!#", "")
        await message.edit(content=editedmsg)
        await AddReaction(message, "⬆️")
        await AddReaction(message, "⬇️")

    if "!reFacilipeach" in message.content and message.author == client.user:
        await message.channel.send(file=discord.File("images/facilipeach.png"))
    #    if message.author == client.user:
    #        return

    print(
        "Message in {0.guild} from {0.author} in #{0.channel}: {0.content}".format(
            message
        )
    )
    await client.process_commands(message)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            "**Still on cooldown**, please try again in {:.2f}s".format(
                error.retry_after
            )
        )


# Commands
@client.command(
    aliases=["load"],
    brief="Loads a cog, devs only",
    description="Loads a cog, devs only",
    pass_context=True,
)
async def Load(ctx, extension):
    if ctx.message.author.id in devs:
        client.load_extension(f"cogs.{extension}")


@client.command(
    aliases=["unload"],
    brief="Unloads a cog, devs only",
    description="Unloads a cog, devs only",
    pass_context=True,
)
async def Unload(ctx, extension):
    if ctx.message.author.id in devs:
        client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(token)
