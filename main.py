import discord
from discord.ext import commands
from discord.utils import get
import csv
import random
import time
import asyncio


# This function will search an specified value on a specified csv file
# csv files must have the value keyword on the row 0
def SearchElementOnCSV(csvFile, args, row):
    with open(csvFile, "rt", encoding="utf8") as f:
        fileReader = csv.reader(f)
        fileList = list(fileReader)
        for i in range(len(fileList)):
            if fileList[0][i] == args:
                return fileList[row][i]


# Only for 2 col lists
def SearchInverseElementOnCSV(csvFile, args):
    with open(csvFile, "rt", encoding="utf8") as f:
        fileReader = csv.reader(f)
        fileList = list(fileReader)
        for i in range(len(fileList)):
            if fileList[i][0] == args:
                return fileList[i][1]
            elif fileList[i][1] == args:
                return fileList[i][0]


def SearchKnownElementOnCsv(csvFile, row, col):
    with open(csvFile, "rt", encoding="utf8") as f:
        fileReader = csv.reader(f)
        fileList = list(fileReader)
        return fileList[row][col]


configcsv = "config.csv"
kanjicsv = "kanji.csv"
token = SearchElementOnCSV(configcsv, "Token", 1)
client = commands.Bot(command_prefix="!re")
lastKanji = "Uno"
lastkanjireverse = "Dos"


@client.event
async def on_ready():
    print("Logged on as {0}!".format(client.user))


async def on_message(message):
    if message.author == client.user:
        return

    print("Message from {0.author}: {0.content}".format(message))


@client.command()
async def Facilito(ctx):
    await ctx.send(
        ".  ━━━━━-╮\n ╰┃ ┣▇━▇\n ┃ ┃  ╰━▅╮ \n ╰┳╯ ╰━━┳╯F A S I L I T O\n  ╰╮ ┳━━╯ E L\n ▕▔▋ ╰╮╭━╮ T U T O R I A L\n ╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n ▏  ▔▔▔▔▔▔▔  O O┃ \n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n ▏╳▕▇▇▕ ▏╳▕▇▇▕\n ╲▂╱╲▂╱ ╲▂╱╲▂╱"
    )


def sendKanji(rorw, limit):  # 0 = Read  1 = Write
    if rorw is True:
        keyword = SearchElementOnCSV(kanjicsv, "kanji_key", random.randint(1, limit))
    else:
        keyword = SearchElementOnCSV(kanjicsv, "kanji_char", random.randint(1, limit))
    global lastKanji
    global lastkanjireverse
    lastKanji = keyword
    lastkanjireverse = SearchInverseElementOnCSV(kanjicsv, keyword)
    return keyword


@client.command()
async def kanjicompetitivor(ctx, limit: int, time: int):
    await ctx.send(sendKanji(False, int(limit)))
    try:
        if time < 0:
            await ctx.send("number cant be a negative")
        elif time > 300:
            await ctx.send("number must be under 300")
        else:
            message = await ctx.send(time)
            while time != 0:
                time -= 1
                await message.edit(content=time)
                await asyncio.sleep(1)
            await message.edit(content="Tiempo! la respuesta era: " + lastkanjireverse)

    except ValueError:
        await ctx.send("time was not a number")


@client.command()
async def kanjicompetitivow(ctx, limit: int, time: int):
    await ctx.send(sendKanji(True, int(limit)))
    try:
        if time < 0:
            await ctx.send("number cant be a negative")
        elif time > 300:
            await ctx.send("number must be under 300")
        else:
            message = await ctx.send(time)
            while time != 0:
                time -= 1
                await message.edit(content=time)
                await asyncio.sleep(1)
            await message.edit(content="Tiempo! la respuesta era: " + lastkanjireverse)

    except ValueError:
        await ctx.send("time was not a number")


@client.command()
async def kanjilast(ctx):
    await ctx.send(lastKanji + " " + lastkanjireverse)


@client.command()
async def lastkanji(ctx):
    await ctx.send(lastKanji + " " + lastkanjireverse)


@client.command()
async def Symphonia(ctx):
    sjs = get(ctx.guild.roles, name="Slice Juega Symphonia")
    await ctx.send(sjs.mention)


@client.command()
async def timer(ctx, number: int):
    try:
        if number < 0:
            await ctx.send("number cant be a negative")
        elif number > 300:
            await ctx.send("number must be under 300")
        else:
            message = await ctx.send(number)
            while number != 0:
                number -= 1
                await message.edit(content=number)
                await asyncio.sleep(1)
            await message.edit(content="Ended!")

    except ValueError:
        await ctx.send("time was not a number")


@client.command()
async def count(ctx, number: int):
    try:
        if number < 0:
            await ctx.send("number cant be a negative")
        elif number > 300:
            await ctx.send("number must be under 300")
        else:
            message = await ctx.send(number)
            while number != 0:
                number -= 1
                await message.edit(content=number)
                await asyncio.sleep(1)
            await message.edit(content="Ended!")

    except ValueError:
        await ctx.send("time was not a number")


client.run(token)

