import discord
from discord.ext import commands
from discord.utils import get
from discord_slash import cog_ext, SlashContext
import json
import random
import asyncio
import sys
from main import GetLastKanjiID
from main import SetLastKanjiID


class Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables
    kanjijson = "kanji.json"
    with open(kanjijson, "r", encoding="utf8") as JsonFile:
        kanjidata = json.load(JsonFile)

    mpdocument = "https://docs.google.com/spreadsheets/d/1z-eeH8Q1c3uJliE5v_K_MkNDp30SVGam2cyZvDE56Oo/edit?usp=sharing"
    github = "https://github.com/Cerrebe/Symbot"

    facilipeach = "media/images/facilipeach.png"
    facilicheat = "media/images/facilicheat.jpg"
    amañapeach = "media/images/amañapeach.png"
    facilimario = "media/images/facilimario.jpg"
    faciliboo = "media/images/faciliboo.png"
    luiramo = "media/images/luiramo.jpg"
    impercerbero = "media/images/impercerbero.png"
    dificilikong = "media/images/dificilikong.jpg"
    luistoriador = "media/images/luistoriador.png"
    filetrelay = "media/images/filetrelay.jpg"
    wpcerrebe = "media/images/wpcerrebe.png"
    bonustars = "media/images/bonustars.jpg"
    hiddenblock = "media/images/hiddenblock.png"
    luipadres = "media/images/luipadres.jpg"
    misteryduel = "media/images/misteryduel.jpg"
    ganerrebe = "media/images/ganerrebe.jpg"
    trust = "media/images/trust.png"
    choice = "media/images/choice.png"
    cerrescritorio = "media/images/cerrescritorio.png"
    patrickmp = "media/images/patrickmp.png"
    muchokanji = "media/images/muchokanji.png"
    frowaifu = "media/images/frowaifu.png"
    toadship = "media/gifs/toadship.gif"
    pinged = "media/gifs/pinged.gif"
    slicerelay = "media/audios/slicerelay.mp3"
    amogus = "media/videos/amogus.mp4"
    symjoy = "media/videos/symjoy.mp4"
    mp5enjoyer = "media/videos/mp5enjoyer.mp4"
    traumas = "media/videos/traumas.mp4"
    switch = "media/videos/switch.mp4"
    typo = "media/videos/typo.mp4"

    # Regular Functions
    def GetKanjiByID(self, id):
        return self.kanjidata["notes"][id]["fields"][0]

    def GetKanjiByName(self, name):
        for k in range(len(self.kanjidata["notes"])):
            if self.kanjidata["notes"][k]["fields"][1] == name:
                return self.kanjidata["notes"][k]["fields"][0]

    def GetKanjiName(self, kanji):
        for k in range(len(self.kanjidata["notes"])):
            if self.kanjidata["notes"][k]["fields"][0] == kanji:
                return self.kanjidata["notes"][k]["fields"][1]

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("slash cog loaded")

    # Commands
    @cog_ext.cog_slash(
        description="Sends a kanji, can be limited by heising number",
    )
    async def KanjiCompetitivo(self, ctx: SlashContext, limit: int = 2041):
        limit -= 1
        id = random.randint(0, limit)
        await ctx.send(self.GetKanjiByID(id))
        SetLastKanjiID(id)

    @cog_ext.cog_slash(
        description="Sends a keyword of a kanji, can be limited by heising number",
    )
    async def KanjiCompetitivoR(self, ctx: SlashContext, limit: int = 2041):
        limit -= 1
        id = random.randint(0, limit)
        await ctx.send(self.GetKanjiName(self.GetKanjiByID(id)))
        SetLastKanjiID(id)

    @cog_ext.cog_slash(
        description="Sends the last kanji that has been sent by KanjiCompetitivo",
    )
    async def LastKanji(self, ctx: SlashContext):
        if GetLastKanjiID() == None:
            await ctx.send("No kanji was sent recently")
            return
        await ctx.send(self.GetKanjiByID(GetLastKanjiID()))

    @cog_ext.cog_slash(
        description="Sends the keyword of the last kanji that has been sent by KanjiCompetitivo",
    )
    async def LastKanjiName(self, ctx: SlashContext):
        if GetLastKanjiID() == None:
            await ctx.send("No kanji was sent recently")
            return
        await ctx.send(self.GetKanjiName(self.GetKanjiByID(GetLastKanjiID())))

    @cog_ext.cog_slash(
        description="Sends the ASCII Art of Facilito",
    )
    async def Facilito(self, ctx: SlashContext):
        await ctx.send(
            ".  ━━━━━-╮\n ╰┃ ┣▇━▇\n ┃ ┃  ╰━▅╮ \n ╰┳╯ ╰━━┳╯F A S I L I T O\n  ╰╮ ┳━━╯ E L\n ▕▔▋ ╰╮╭━╮ T U T O R I A L\n ╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n ▏  ▔▔▔▔▔▔▔  O O┃ \n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n ▏╳▕▇▇▕ ▏╳▕▇▇▕\n ╲▂╱╲▂╱ ╲▂╱╲▂╱"
        )

    @cog_ext.cog_slash(
        description="Pings the role @Slice Juega Symphonia",
    )
    async def Symphonia(self, ctx: SlashContext):
        sjs = get(ctx.guild.roles, name="Slice Juega Symphonia")
        await ctx.send(sjs.mention)

    @cog_ext.cog_slash(
        description="Sends a link to the googledocs of Mario Party",
    )
    async def MPDocument(self, ctx: SlashContext):
        await ctx.send(self.mpdocument)

    @cog_ext.cog_slash(
        description="Sends a link to the repository of this bot",
    )
    async def GitHub(self, ctx: SlashContext):
        await ctx.send(self.github)

    @cog_ext.cog_slash(
        description="Says something on the current channel",
    )
    async def Di(self, ctx: SlashContext, *text: str):
        await ctx.send(" ".join(text[:]))

    @cog_ext.cog_slash(
        description="Creates a real time updating timer",
    )
    async def Timer(self, ctx: SlashContext, number: int):
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

    @cog_ext.cog_slash(
        description="Sends the image of Facilipeach",
    )
    async def Facilipeach(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.facilipeach))

    @cog_ext.cog_slash(
        description="Sends the image of Facilicheat",
    )
    async def Facilicheat(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.facilicheat))

    @cog_ext.cog_slash(
        description="Sends the image of Amañapeach",
    )
    async def Amañapeach(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.amañapeach))

    @cog_ext.cog_slash(
        description="Sends the image of Facilimario",
    )
    async def Facilimario(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.facilimario))

    @cog_ext.cog_slash(
        description="Sends the image of Faciliboo",
    )
    async def Faciliboo(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.faciliboo))

    @cog_ext.cog_slash(
        description="Sends the image of Luiramo",
    )
    async def Luiramo(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.luiramo))

    @cog_ext.cog_slash(
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.impercerbero))

    @cog_ext.cog_slash(
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.impercerbero))

    @cog_ext.cog_slash(
        description="Sends the image of Luistoriador",
    )
    async def Luistoriador(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.luistoriador))

    @cog_ext.cog_slash(
        description="Sends the image of Filetrelay",
    )
    async def Filetrelay(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.filetrelay))

    @cog_ext.cog_slash(
        description="Sends the image of WPCerrebe",
    )
    async def WPCerrebe(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.wpcerrebe))

    @cog_ext.cog_slash(
        description="Sends the image of Bonustars",
    )
    async def Bonustars(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.bonustars))

    @cog_ext.cog_slash(
        description="Sends the image of Hiddenblock",
    )
    async def Hiddenblock(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.hiddenblock))

    @cog_ext.cog_slash(
        description="Sends the image of Luipadres",
    )
    async def Luipadres(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.luipadres))

    @cog_ext.cog_slash(
        description="Sends the image of Misteryduel",
    )
    async def Misteryduel(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.misteryduel))

    @cog_ext.cog_slash(
        description="Sends the image of Ganerrebe",
    )
    async def Ganerrebe(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.ganerrebe))

    @cog_ext.cog_slash(
        description="Sends the image of Trust",
    )
    async def Trust(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.trust))

    @cog_ext.cog_slash(
        description="Sends the image of Choice",
    )
    async def Choice(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.choice))

    @cog_ext.cog_slash(
        description="Sends the image of Cerrescritorio",
    )
    async def Cerrescritorio(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.cerrescritorio))

    @cog_ext.cog_slash(
        description="Sends the image of PatrickMP",
    )
    async def PatrickMP(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.patrickmp))

    @cog_ext.cog_slash(
        description="Sends the image of MuchoKanji",
    )
    async def MuchoKanji(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.muchokanji))

    @cog_ext.cog_slash(
        description="Sends the image of Frowaifu",
    )
    async def Frowaifu(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.frowaifu))

    @cog_ext.cog_slash(
        description="Sends the gif of Toadship",
    )
    async def Toadship(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.toadship))

    @cog_ext.cog_slash(
        description="Sends the gif of Pinged",
    )
    async def Pinged(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.pinged))

    @cog_ext.cog_slash(
        description="Sends the audio of Slicerelay",
    )
    async def Slicerelay(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.slicerelay))

    @cog_ext.cog_slash(
        description="Sends the video of amogus",
    )
    async def Amogus(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.amogus))

    @cog_ext.cog_slash(
        description="Sends the video of Symjoy",
    )
    async def Symjoy(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.symjoy))

    @cog_ext.cog_slash(
        description="Sends the video of MP5Enjoyer",
    )
    async def MP5Enjoyer(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.mp5enjoyer))

    @cog_ext.cog_slash(
        description="Sends the video of Traumas",
    )
    async def Traumas(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.traumas))

    @cog_ext.cog_slash(
        description="Sends the video of Switch",
    )
    async def Switch(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.switch))

    @cog_ext.cog_slash(
        description="Sends the video of Typo",
    )
    async def Typo(self, ctx: SlashContext):
        await ctx.send(file=discord.File(self.typo))


def setup(client):
    client.add_cog(Slash(client))
