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

sys.path.insert(1, "/mediavars.py")
import mediavars


class Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables
    kanjijson = "kanji.json"
    with open(kanjijson, "r", encoding="utf8") as JsonFile:
        kanjidata = json.load(JsonFile)

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
    # kanji
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

    # misc
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
        await ctx.send(mediavars.mpdocument)

    @cog_ext.cog_slash(
        description="Sends a link to the repository of this bot",
    )
    async def GitHub(self, ctx: SlashContext):
        await ctx.send(mediavars.github)

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

    # media
    @cog_ext.cog_slash(
        description="Sends the image of PanConParty",
    )
    async def PanConParty(self, ctx):
        await ctx.send(file=discord.File(mediavars.panconparty))

    @cog_ext.cog_slash(
        description="Sends the image of PanConPartyPaint",
    )
    async def PanConPartyPaint(self, ctx):
        await ctx.send(file=discord.File(mediavars.panconpartypaint))

    @cog_ext.cog_slash(
        description="Sends the image of Friendship",
    )
    async def Friendship(self, ctx):
        await ctx.send(file=discord.File(mediavars.friendship))

    @cog_ext.cog_slash(
        description="Sends the image of PaoComFesta",
    )
    async def PaoComFesta(self, ctx):
        await ctx.send(file=discord.File(mediavars.paocomfesta))

    @cog_ext.cog_slash(
        description="Sends the image of Logo",
    )
    async def Logo(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.logo))

    @cog_ext.cog_slash(
        description="Sends the image of PeachParty",
    )
    async def PeachParty(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.peachparty))

    @cog_ext.cog_slash(
        description="Sends the image of Facilipeach",
    )
    async def Facilipeach(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.facilipeach))

    @cog_ext.cog_slash(
        description="Sends the image of Facilicheat",
    )
    async def Facilicheat(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.facilicheat))

    @cog_ext.cog_slash(
        description="Sends the image of Amañapeach",
    )
    async def Amañapeach(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.amañapeach))

    @cog_ext.cog_slash(
        description="Sends the image of Facilimario",
    )
    async def Facilimario(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.facilimario))

    @cog_ext.cog_slash(
        description="Sends the image of Faciliboo",
    )
    async def Faciliboo(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.faciliboo))

    @cog_ext.cog_slash(
        description="Sends the image of Faciliwario",
    )
    async def Faciliwario(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.faciliwario))

    @cog_ext.cog_slash(
        description="Sends the image of Faciliyoshi",
    )
    async def Faciliyoshi(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.faciliyoshi))

    @cog_ext.cog_slash(
        description="Sends the image of Facilitoad",
    )
    async def Facilitoad(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.facilitoad))

    @cog_ext.cog_slash(
        description="Sends the image of Luiramo",
    )
    async def Luiramo(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.luiramo))

    @cog_ext.cog_slash(
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.impercerbero))

    @cog_ext.cog_slash(
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.impercerbero))

    @cog_ext.cog_slash(
        description="Sends the image of Dificilikong",
    )
    async def Dificilikong(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.dificilikong))

    @cog_ext.cog_slash(
        description="Sends the image of Peterilito",
    )
    async def Peterilito(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.peterilito))

    @cog_ext.cog_slash(
        description="Sends the image of Filefacilito",
    )
    async def Filefacilito(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.filefacilito))

    @cog_ext.cog_slash(
        description="Sends the image of Mortafacilito",
    )
    async def Mortafacilito(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.mortafacilito))

    @cog_ext.cog_slash(
        description="Sends the image of Luistoriador",
    )
    async def Luistoriador(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.luistoriador))

    @cog_ext.cog_slash(
        description="Sends the image of Filetrelay",
    )
    async def Filetrelay(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.filetrelay))

    @cog_ext.cog_slash(
        description="Sends the image of WPCerrebe",
    )
    async def WPCerrebe(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.wpcerrebe))

    @cog_ext.cog_slash(
        description="Sends the image of Bonustars",
    )
    async def Bonustars(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.bonustars))

    @cog_ext.cog_slash(
        description="Sends the image of Hiddenblock",
    )
    async def Hiddenblock(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.hiddenblock))

    @cog_ext.cog_slash(
        description="Sends the image of Luipadres",
    )
    async def Luipadres(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.luipadres))

    @cog_ext.cog_slash(
        description="Sends the image of Misteryduel",
    )
    async def Misteryduel(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.misteryduel))

    @cog_ext.cog_slash(
        description="Sends the image of Ganerrebe",
    )
    async def Ganerrebe(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.ganerrebe))

    @cog_ext.cog_slash(
        description="Sends the image of Trust",
    )
    async def Trust(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.trust))

    @cog_ext.cog_slash(
        description="Sends the image of Choice",
    )
    async def Choice(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.choice))

    @cog_ext.cog_slash(
        description="Sends the image of Cerrescritorio",
    )
    async def Cerrescritorio(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.cerrescritorio))

    @cog_ext.cog_slash(
        description="Sends the image of PatrickMP",
    )
    async def PatrickMP(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.patrickmp))

    @cog_ext.cog_slash(
        description="Sends the image of Cachonda",
    )
    async def Cachonda(self, ctx):
        await ctx.send(file=discord.File(mediavars.cachonda))

    @cog_ext.cog_slash(
        description="Sends the image of Luiexpose",
    )
    async def Luiexpose(self, ctx):
        await ctx.send(file=discord.File(mediavars.luiexpose))

    @cog_ext.cog_slash(
        description="Sends the image of Luiexpose2",
    )
    async def Luiexpose2(self, ctx):
        await ctx.send(file=discord.File(mediavars.luiexpose2))

    @cog_ext.cog_slash(
        description="Sends the image of Cheatrade",
    )
    async def Cheatrade(self, ctx):
        await ctx.send(file=discord.File(mediavars.cheatrade))

    @cog_ext.cog_slash(
        description="Sends the image of Claramente",
    )
    async def Claramente(self, ctx):
        await ctx.send(file=discord.File(mediavars.claramente))

    @cog_ext.cog_slash(
        description="Sends the image of Dinklerrebe",
    )
    async def Dinklerrebe(self, ctx):
        await ctx.send(file=discord.File(mediavars.dinklerrebe))

    @cog_ext.cog_slash(
        description="Sends the image of Ememp",
    )
    async def Ememp(self, ctx):
        await ctx.send(file=discord.File(mediavars.ememp))

    @cog_ext.cog_slash(
        description="Sends the image of McFlurry",
    )
    async def McFlurry(self, ctx):
        await ctx.send(file=discord.File(mediavars.mcflurry))

    @cog_ext.cog_slash(
        description="Sends the image of Miyazakimp",
    )
    async def Miyazakimp(self, ctx):
        await ctx.send(file=discord.File(mediavars.miyazakimp))

    @cog_ext.cog_slash(
        description="Sends the image of NeverChanceTime",
    )
    async def NeverChanceTime(self, ctx):
        await ctx.send(file=discord.File(mediavars.neverchancetime))

    @cog_ext.cog_slash(
        description="Sends the image of NobitaPistol",
    )
    async def NobitaPistol(self, ctx):
        await ctx.send(file=discord.File(mediavars.nobitapistol))

    @cog_ext.cog_slash(
        description="Sends the image of Pozoaceptacion",
    )
    async def Pozoaceptacion(self, ctx):
        await ctx.send(file=discord.File(mediavars.pozoaceptacion))

    @cog_ext.cog_slash(
        description="Sends the image of ViernesNoche",
    )
    async def ViernesNoche(self, ctx):
        await ctx.send(file=discord.File(mediavars.viernesnoche))

    @cog_ext.cog_slash(
        description="Sends the image of BowserAkello",
    )
    async def BowserAkello(self, ctx):
        await ctx.send(file=discord.File(mediavars.bowserakello))

    @cog_ext.cog_slash(
        description="Sends the image of Ani2AM",
    )
    async def Ani2AM(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.ani2am))

    @cog_ext.cog_slash(
        description="Sends the image of MP8PM",
    )
    async def MP8PM(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.mp8pm))

    @cog_ext.cog_slash(
        description="Sends the image of MuchoKanji",
    )
    async def MuchoKanji(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.muchokanji))

    @cog_ext.cog_slash(
        description="Sends the image of Frowaifu",
    )
    async def Frowaifu(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.frowaifu))

    @cog_ext.cog_slash(
        description="Sends the gif of Toadship",
    )
    async def Toadship(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.toadship))

    @cog_ext.cog_slash(
        description="Sends the gif of Pinged",
    )
    async def Pinged(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.pinged))

    @cog_ext.cog_slash(
        description="Sends the gif of Follar",
    )
    async def Follar(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.follar))

    @cog_ext.cog_slash(
        description="Sends the audio of Slicerelay",
    )
    async def Slicerelay(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.slicerelay))

    @cog_ext.cog_slash(
        description="Sends the video of amogus",
    )
    async def Amogus(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.amogus))

    @cog_ext.cog_slash(
        description="Sends the video of Symjoy",
    )
    async def Symjoy(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.symjoy))

    @cog_ext.cog_slash(
        description="Sends the video of MP5Enjoyer",
    )
    async def MP5Enjoyer(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.mp5enjoyer))

    @cog_ext.cog_slash(
        description="Sends the video of Traumas",
    )
    async def Traumas(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.traumas))

    @cog_ext.cog_slash(
        description="Sends the video of Luifoxfg",
    )
    async def Luifoxfg(self, ctx):
        await ctx.send(file=discord.File(mediavars.luifoxfg))

    @cog_ext.cog_slash(
        description="Sends the video of LoLogro",
    )
    async def LoLogro(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.lologro))

    @cog_ext.cog_slash(
        description="Sends the video of PartyPosting",
    )
    async def PartyPosting(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.partyposting))

    @cog_ext.cog_slash(
        description="Sends the video of Rajoypensar",
    )
    async def Rajoypensar(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.rajoypensar))

    @cog_ext.cog_slash(
        description="Sends the video of Sympinged",
    )
    async def Sympinged(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.sympinged))

    @cog_ext.cog_slash(
        description="Sends the video of Switch",
    )
    async def Switch(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.switch))

    @cog_ext.cog_slash(
        description="Sends the video of Typo",
    )
    async def Typo(self, ctx: SlashContext):
        await ctx.send(file=discord.File(mediavars.typo))


def setup(client):
    client.add_cog(Slash(client))
