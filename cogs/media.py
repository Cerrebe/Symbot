import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import sys

sys.path.insert(1, "/mediavars.py")
import mediavars


class Media(commands.Cog):
    def __init__(self, client):
        mediavars.client = client

    # Variables

    # Regular Functions

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("media cog loaded")

    # Commands
    @commands.command(
        aliases=["panconparty", "PanconParty"],
        brief="Sends an image",
        description="Sends the image of PanConParty",
    )
    async def PanConParty(self, ctx):
        await ctx.send(file=discord.File(mediavars.panconparty))

    @commands.command(
        aliases=["panconpartypaint", "PanconPartyPaint"],
        brief="Sends an image",
        description="Sends the image of PanConPartyPaint",
    )
    async def PanConPartyPaint(self, ctx):
        await ctx.send(file=discord.File(mediavars.panconpartypaint))

    @commands.command(
        aliases=["friendship", "amistad", "Amistad"],
        brief="Sends an image",
        description="Sends the image of Friendship",
    )
    async def Friendship(self, ctx):
        await ctx.send(file=discord.File(mediavars.friendship))

    @commands.command(
        aliases=["logo"],
        brief="Sends an image",
        description="Sends the image of Logo",
    )
    async def Logo(self, ctx):
        await ctx.send(file=discord.File(mediavars.logo))

    @commands.command(
        aliases=["peachparty", "Peachparty"],
        brief="Sends an image",
        description="Sends the image of PeachParty",
    )
    async def PeachParty(self, ctx):
        await ctx.send(file=discord.File(mediavars.peachparty))

    @commands.command(
        aliases=["facilipeach"],
        brief="Sends an image",
        description="Sends the image of Facilipeach",
    )
    async def Facilipeach(self, ctx):
        await ctx.send(file=discord.File(mediavars.facilipeach))

    @commands.command(
        aliases=["facilicheat"],
        brief="Sends an image",
        description="Sends the image of Facilicheat",
    )
    async def Facilicheat(self, ctx):
        await ctx.send(file=discord.File(mediavars.facilicheat))

    @commands.command(
        aliases=["amañapeach"],
        brief="Sends an image",
        description="Sends the image of Amañapeach",
    )
    async def Amañapeach(self, ctx):
        await ctx.send(file=discord.File(mediavars.amañapeach))

    @commands.command(
        aliases=["facilimario"],
        brief="Sends an image",
        description="Sends the image of Facilimario",
    )
    async def Facilimario(self, ctx):
        await ctx.send(file=discord.File(mediavars.facilimario))

    @commands.command(
        aliases=["faciliboo"],
        brief="Sends an image",
        description="Sends the image of Faciliboo",
    )
    async def Faciliboo(self, ctx):
        await ctx.send(file=discord.File(mediavars.faciliboo))

    @commands.command(
        aliases=["faciliwario"],
        brief="Sends an image",
        description="Sends the image of Faciliwario",
    )
    async def Faciliwario(self, ctx):
        await ctx.send(file=discord.File(mediavars.faciliwario))

    @commands.command(
        aliases=["faciliyoshi"],
        brief="Sends an image",
        description="Sends the image of Faciliyoshi",
    )
    async def Faciliyoshi(self, ctx):
        await ctx.send(file=discord.File(mediavars.faciliyoshi))

    @commands.command(
        aliases=["facilitoad"],
        brief="Sends an image",
        description="Sends the image of Facilitoad",
    )
    async def Facilitoad(self, ctx):
        await ctx.send(file=discord.File(mediavars.facilitoad))

    @commands.command(
        aliases=["luiramo"],
        brief="Sends an image",
        description="Sends the image of Luiramo",
    )
    async def Luiramo(self, ctx):
        await ctx.send(file=discord.File(mediavars.luiramo))

    @commands.command(
        aliases=["impercerbero", "imperiocancerbero"],
        brief="Sends an image",
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx):
        await ctx.send(file=discord.File(mediavars.impercerbero))

    @commands.command(
        aliases=["impercerbero"],
        brief="Sends an image",
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx):
        await ctx.send(file=discord.File(mediavars.impercerbero))

    @commands.command(
        aliases=["dificilikong"],
        brief="Sends an image",
        description="Sends the image of Dificilikong",
    )
    async def Dificilikong(self, ctx):
        await ctx.send(file=discord.File(mediavars.dificilikong))

    @commands.command(
        aliases=["peterilito"],
        brief="Sends an image",
        description="Sends the image of Peterilito",
    )
    async def Peterilito(self, ctx):
        await ctx.send(file=discord.File(mediavars.peterilito))

    @commands.command(
        aliases=["luistoriador"],
        brief="Sends an image",
        description="Sends the image of Luistoriador",
    )
    async def Luistoriador(self, ctx):
        await ctx.send(file=discord.File(mediavars.luistoriador))

    @commands.command(
        aliases=["filetrelay"],
        brief="Sends an image",
        description="Sends the image of Filetrelay",
    )
    async def Filetrelay(self, ctx):
        await ctx.send(file=discord.File(mediavars.filetrelay))

    @commands.command(
        aliases=["wpcerrebe", "WPcerrebe", "Wpcerrebe", "bienjugadocerrebe"],
        brief="Sends an image",
        description="Sends the image of WPCerrebe",
    )
    async def WPCerrebe(self, ctx):
        await ctx.send(file=discord.File(mediavars.wpcerrebe))

    @commands.command(
        aliases=["bonustars", "bonusstars", "Bonusstars"],
        brief="Sends an image",
        description="Sends the image of Bonustars",
    )
    async def Bonustars(self, ctx):
        await ctx.send(file=discord.File(mediavars.bonustars))

    @commands.command(
        aliases=["hiddenblock", "HiddenBlock"],
        brief="Sends an image",
        description="Sends the image of Hiddenblock",
    )
    async def Hiddenblock(self, ctx):
        await ctx.send(file=discord.File(mediavars.hiddenblock))

    @commands.command(
        aliases=["luipadres"],
        brief="Sends an image",
        description="Sends the image of Luipadres",
    )
    async def Luipadres(self, ctx):
        await ctx.send(file=discord.File(mediavars.luipadres))

    @commands.command(
        aliases=[
            "misteryduel",
            "mistemporal",
            "lapiedrashapiñondermario",
            "lapiedrashapinondermario",
        ],
        brief="Sends an image",
        description="Sends the image of Misteryduel",
    )
    async def Misteryduel(self, ctx):
        await ctx.send(file=discord.File(mediavars.misteryduel))

    @commands.command(
        aliases=[
            "ganerrebe",
            "ganeacerrebe",
            "GaneACerrebe",
            "GaneCerrebe",
            "ganecerrebe",
        ],
        brief="Sends an image",
        description="Sends the image of Ganerrebe",
    )
    async def Ganerrebe(self, ctx):
        await ctx.send(file=discord.File(mediavars.ganerrebe))

    @commands.command(
        aliases=["trust", "confianza"],
        brief="Sends an image",
        description="Sends the image of Trust",
    )
    async def Trust(self, ctx):
        await ctx.send(file=discord.File(mediavars.trust))

    @commands.command(
        aliases=["choice"],
        brief="Sends an image",
        description="Sends the image of Choice",
    )
    async def Choice(self, ctx):
        await ctx.send(file=discord.File(mediavars.choice))

    @commands.command(
        aliases=["cerrescritorio", "cerresktop"],
        brief="Sends an image",
        description="Sends the image of Cerrescritorio",
    )
    async def Cerrescritorio(self, ctx):
        await ctx.send(file=discord.File(mediavars.cerrescritorio))

    @commands.command(
        aliases=["patrickmp", "patrickMP", "Patrickmp"],
        brief="Sends an image",
        description="Sends the image of PatrickMP",
    )
    async def PatrickMP(self, ctx):
        await ctx.send(file=discord.File(mediavars.patrickmp))

    @commands.command(
        aliases=["cachonda", "viejacachonda"],
        brief="Sends an image",
        description="Sends the image of Cachonda",
    )
    async def Cachonda(self, ctx):
        await ctx.send(file=discord.File(mediavars.cachonda))

    @commands.command(
        aliases=["luiexpose"],
        brief="Sends an image",
        description="Sends the image of Luiexpose",
    )
    async def Luiexpose(self, ctx):
        await ctx.send(file=discord.File(mediavars.luiexpose))

    @commands.command(
        aliases=["luiexpose2"],
        brief="Sends an image",
        description="Sends the image of Luiexpose2",
    )
    async def Luiexpose2(self, ctx):
        await ctx.send(file=discord.File(mediavars.luiexpose2))

    @commands.command(
        aliases=["cheatrade"],
        brief="Sends an image",
        description="Sends the image of Cheatrade",
    )
    async def Cheatrade(self, ctx):
        await ctx.send(file=discord.File(mediavars.cheatrade))

    @commands.command(
        aliases=["claramente"],
        brief="Sends an image",
        description="Sends the image of Claramente",
    )
    async def Claramente(self, ctx):
        await ctx.send(file=discord.File(mediavars.claramente))

    @commands.command(
        aliases=["dinklerrebe"],
        brief="Sends an image",
        description="Sends the image of Dinklerrebe",
    )
    async def Dinklerrebe(self, ctx):
        await ctx.send(file=discord.File(mediavars.dinklerrebe))

    @commands.command(
        aliases=["ememp"],
        brief="Sends an image",
        description="Sends the image of Ememp",
    )
    async def Ememp(self, ctx):
        await ctx.send(file=discord.File(mediavars.ememp))

    @commands.command(
        aliases=["mcflurry", "Mcflurry"],
        brief="Sends an image",
        description="Sends the image of McFlurry",
    )
    async def McFlurry(self, ctx):
        await ctx.send(file=discord.File(mediavars.mcflurry))

    @commands.command(
        aliases=["miyazakimp"],
        brief="Sends an image",
        description="Sends the image of Miyazakimp",
    )
    async def Miyazakimp(self, ctx):
        await ctx.send(file=discord.File(mediavars.miyazakimp))

    @commands.command(
        aliases=["neverchancetime", "Neverchancetime"],
        brief="Sends an image",
        description="Sends the image of NeverChanceTime",
    )
    async def NeverChanceTime(self, ctx):
        await ctx.send(file=discord.File(mediavars.neverchancetime))

    @commands.command(
        aliases=["nobitapistol", "Nobitapistol"],
        brief="Sends an image",
        description="Sends the image of NobitaPistol",
    )
    async def NobitaPistol(self, ctx):
        await ctx.send(file=discord.File(mediavars.nobitapistol))

    @commands.command(
        aliases=["pozoaceptacion"],
        brief="Sends an image",
        description="Sends the image of Pozoaceptacion",
    )
    async def Pozoaceptacion(self, ctx):
        await ctx.send(file=discord.File(mediavars.pozoaceptacion))

    @commands.command(
        aliases=["viernesnoche", "Viernesnoche"],
        brief="Sends an image",
        description="Sends the image of ViernesNoche",
    )
    async def ViernesNoche(self, ctx):
        await ctx.send(file=discord.File(mediavars.viernesnoche))

    @commands.command(
        aliases=["bowserakello", "Bowserakello"],
        brief="Sends an image",
        description="Sends the image of BowserAkello",
    )
    async def BowserAkello(self, ctx):
        await ctx.send(file=discord.File(mediavars.bowserakello))

    @commands.command(
        aliases=["muchokanji"],
        brief="Sends an image",
        description="Sends the image of MuchoKanji",
    )
    async def MuchoKanji(self, ctx):
        await ctx.send(file=discord.File(mediavars.muchokanji))

    @commands.command(
        aliases=["frowaifu"],
        brief="Sends an image",
        description="Sends the image of Frowaifu",
    )
    async def Frowaifu(self, ctx):
        await ctx.send(file=discord.File(mediavars.frowaifu))

    @commands.command(
        aliases=["toadship", "ToadShip"],
        brief="Sends a gif",
        description="Sends the gif of Toadship",
    )
    async def Toadship(self, ctx):
        await ctx.send(file=discord.File(mediavars.toadship))

    @commands.command(
        aliases=["pinged"],
        brief="Sends a gif",
        description="Sends the gif of Pinged",
    )
    async def Pinged(self, ctx):
        await ctx.send(file=discord.File(mediavars.pinged))

    @commands.command(
        aliases=["follar"],
        brief="Sends a gif",
        description="Sends the gif of Follar",
    )
    async def Follar(self, ctx):
        await ctx.send(file=discord.File(mediavars.follar))

    @commands.command(
        aliases=["slicerelay", "SliceRelay"],
        brief="Sends an audio",
        description="Sends the audio of Slicerelay",
    )
    async def Slicerelay(self, ctx):
        await ctx.send(file=discord.File(mediavars.slicerelay))

    @commands.command(
        aliases=["amogus"],
        brief="Sends a video",
        description="Sends the video of amogus",
    )
    async def Amogus(self, ctx):
        if ctx.message.reference != None:
            id = ctx.message.reference.message_id
            channel = ctx.channel
            message = await channel.fetch_message(id)
            await message.reply(file=discord.File(mediavars.amogus))
        else:
            await ctx.send(file=discord.File(mediavars.amogus))

    @commands.command(
        aliases=["symjoy"],
        brief="Sends a video",
        description="Sends the video of Symjoy",
    )
    async def Symjoy(self, ctx):
        await ctx.send(file=discord.File(mediavars.symjoy))

    @commands.command(
        aliases=["mp5enjoyer", "MP5enjoyer"],
        brief="Sends a video",
        description="Sends the video of MP5Enjoyer",
    )
    async def MP5Enjoyer(self, ctx):
        await ctx.send(file=discord.File(mediavars.mp5enjoyer))

    @commands.command(
        aliases=["traumas", "trauma", "Trauma"],
        brief="Sends a video",
        description="Sends the video of Traumas",
    )
    async def Traumas(self, ctx):
        await ctx.send(file=discord.File(mediavars.traumas))

    @commands.command(
        aliases=["luifoxfg"],
        brief="Sends a video",
        description="Sends the video of Luifoxfg",
    )
    async def Luifoxfg(self, ctx):
        await ctx.send(file=discord.File(mediavars.luifoxfg))

    @commands.command(
        aliases=["lologro", "Lologro"],
        brief="Sends a video",
        description="Sends the video of LoLogro",
    )
    async def LoLogro(self, ctx):
        await ctx.send(file=discord.File(mediavars.lologro))

    @commands.command(
        aliases=["partyposting", "Partyposting"],
        brief="Sends a video",
        description="Sends the video of PartyPosting",
    )
    async def PartyPosting(self, ctx):
        await ctx.send(file=discord.File(mediavars.partyposting))

    @commands.command(
        aliases=["rajoypensar"],
        brief="Sends a video",
        description="Sends the video of Rajoypensar",
    )
    async def Rajoypensar(self, ctx):
        await ctx.send(file=discord.File(mediavars.rajoypensar))

    @commands.command(
        aliases=["sympinged"],
        brief="Sends a video",
        description="Sends the video of Sympinged",
    )
    async def Sympinged(self, ctx):
        await ctx.send(file=discord.File(mediavars.sympinged))

    @commands.command(
        aliases=["switch"],
        brief="Sends a video",
        description="Sends the video of Switch",
    )
    async def Switch(self, ctx):
        await ctx.send(file=discord.File(mediavars.switch))

    @commands.command(
        aliases=["typo"],
        brief="Sends a video",
        description="Sends the video of Typo",
    )
    async def Typo(self, ctx):
        await ctx.send(file=discord.File(mediavars.typo))


def setup(client):
    client.add_cog(Media(client))
