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


# Only for first 2 col of lists
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


"""
def GetListCsv(csvFile):
    with open(csvFile, "rt", encoding="utf8") as f:
        return list(csv.reader(f))


def WriteElementOnCsv(csvFile, args, row, col):
    with open(csvFile, "wt", encoding="utf8") as f:
        fileWriter = csv.writer(f)
        r = csv.reader(open(csvFile))
        lines = list(r)
        print(lines)
        try:
            lines[row][col] = str(args)
        except:
            fileWriter.writerows(lines)
        fileWriter.writerows(lines)


def WriteCsv(csvFile, args):
    with open(csvFile, "wt", encoding="utf8") as f:
        fileWriter = csv.writer(f)
"""

# fileWriter.writerow(fileContent[rowi][coll])

configcsv = "config.csv"
kanjicsv = "kanji.csv"
scorecsv = "score.csv"
token = SearchElementOnCSV(configcsv, "Token", 1)
client = commands.Bot(command_prefix="!re")
lastKanji = "Uno"
lastkanjireverse = "Dos"
vidwhitelist = [
    212620735754010624,  # Cerrebe
    733893829555519590,  # Matt
    726828706852634724,  # JD
    803495880317599754,  # Brix
    763926695026622515,  # Peri
]


async def AddReaction(ctx, emojis):
    await ctx.add_reaction(emojis)


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

    if message.author == client.user:
        return

    print(
        "Message in {0.guild} from {0.author} in #{0.channel}: {0.content}".format(
            message
        )
    )
    await client.process_commands(message)


"""
    for a in message.attachments:
        for e in [
            "3g2",
            "3gp",
            "amv",
            "asf",
            "avi",
            "drc",
            "f4a",
            "f4b",
            "f4p",
            "f4v",
            "flv",
            "gif",
            "gifv",
            "m2ts",
            "m2v",
            "m4p",
            "m4v",
            "mkv",
            "mng",
            "mov",
            "mp2",
            "mp4",
            "mpe",
            "mpeg",
            "mpg",
            "mpv",
            "mts",
            "mxf",
            "nsv",
            "ogg",
            "ogv",
            "qt",
            "rm",
            "rmvb",
            "roq",
            "svi",
            "ts",
            "vob",
            "webm",
            "wmv",
            "yuv",
        ]:
            if a.filename[-len(e) - 1 :] == f".{e}" or "mp4" in message.content:
                for i in range(len(vidwhitelist)):
                    if message.author.id == vidwhitelist[i]:
                        await message.reply(
                            "https://cdn.discordapp.com/attachments/716278110433312804/826399285289287731/final_6062e58f654b58004361619f_926958.mp4"
                        )
    if ".mp4" in message.content:
        for i in range(len(vidwhitelist)):
            if message.author.id == vidwhitelist[i]:
                await message.reply(
                    "https://cdn.discordapp.com/attachments/716278110433312804/826399285289287731/final_6062e58f654b58004361619f_926958.mp4"
                )
    """


@client.event
async def on_message_edit(before, after):
    if (
        "https://cdn.discordapp.com/attachments/711087005680795649/826269840130048010/SPOILER_average_fan_Slice.mp4"
        in after.content
    ):
        await after.reply(
            "https://cdn.discordapp.com/attachments/716278110433312804/826399285289287731/final_6062e58f654b58004361619f_926958.mp4"
        )


@client.command()
async def Facilito(ctx):
    await ctx.send(
        ".  ━━━━━-╮\n ╰┃ ┣▇━▇\n ┃ ┃  ╰━▅╮ \n ╰┳╯ ╰━━┳╯F A S I L I T O\n  ╰╮ ┳━━╯ E L\n ▕▔▋ ╰╮╭━╮ T U T O R I A L\n ╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n ▏  ▔▔▔▔▔▔▔  O O┃ \n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n ▏╳▕▇▇▕ ▏╳▕▇▇▕\n ╲▂╱╲▂╱ ╲▂╱╲▂╱"
    )


@client.command()
async def Facilipeach(ctx):
    await ctx.send(file=discord.File("images/facilipeach.png"))


@client.command()
async def MuchoKanji(ctx):
    await ctx.send(file=discord.File("images/muchokanji.png"))


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
async def kanjicompetitivornt(ctx, limit: int):
    await ctx.send(sendKanji(False, int(limit)))


@client.command()
async def kanjicompetitivownt(ctx, limit):
    await ctx.send(sendKanji(True, int(limit)))


@client.command()
async def di(ctx, *text: str):
    await ctx.send(" ".join(text[:]))


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


user1score = 0
user2score = 0
totalq = 0
emojis = [":arrow_up:", ":arrow_down:"]


@client.command()
async def CrearPuntuacion(ctx, user1, user2):
    global user1score
    global user2score
    global totalq
    global emojis
    await ctx.send("$!#" + user1 + ": " + str(user1score))
    await ctx.message.add_reaction("👍")
    await ctx.send("$!#" + user2 + ": " + str(user2score))


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


"""
@client.command()
async def loopav(ctx, args: int):
    for i in range(args):
        await ctx.send(
            "https://cdn.discordapp.com/attachments/716278110433312804/826399285289287731/final_6062e58f654b58004361619f_926958.mp4"
        )
"""


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


@client.command(
    brief="Echos, developers only",
    description="Echos, developers only",
    pass_context=True,
)
async def echo(ctx, id, *echowords: str):
    if ctx.message.author.id in [212620735754010624]:
        msg = list()
        sendchannel = client.get_channel(int(id))
        for i in range(len(echowords)):
            if echowords[i].startswith("@ "):
                msg.append(
                    get(
                        sendchannel.guild.roles, name=echowords[i].replace("@ ", "")
                    ).mention
                )
            else:
                print(str(i))
                msg.append(echowords[i])
        await sendchannel.send(" ".join(msg[:]))
    else:
        await ctx.send("Bot developers only :<")


client.run(token)
