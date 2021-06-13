import discord
from discord.ext import commands
from discord.utils import get
import asyncio


class Media(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables
    facilipeach = "media/images/facilipeach.png"
    facilicheat = "media/images/facilicheat.jpg"
    amañapeach = "media/images/amañapeach.png"
    facilimario = "media/images/facilimario.jpg"
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
    cerrescritorio = "media/images/cerrescritorio.png"
    patrickmp = "media/images/patrickmp.png"
    muchokanji = "media/images/muchokanji.png"
    frowaifu = "media/images/frowaifu.png"
    toadship = "media/gifs/toadship.gif"
    pinged = "media/gifs/pinged.gif"
    slicerelay = "media/audios/slicerelay.mp3"
    amogus = "media/videos/amogus.mp4"
    symjoy = "media/videos/symjoy.mp4"
    switch = "media/videos/switch.mp4"
    typo = "media/videos/typo.mp4"

    # Regular Functions

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("media cog loaded")

    # Commands
    @commands.command(
        aliases=["facilipeach"],
        brief="Sends an image",
        description="Sends the image of Facilipeach",
    )
    async def Facilipeach(self, ctx):
        await ctx.send(file=discord.File(self.facilipeach))

    @commands.command(
        aliases=["facilicheat"],
        brief="Sends an image",
        description="Sends the image of Facilicheat",
    )
    async def Facilicheat(self, ctx):
        await ctx.send(file=discord.File(self.facilicheat))

    @commands.command(
        aliases=["amañapeach"],
        brief="Sends an image",
        description="Sends the image of Amañapeach",
    )
    async def Amañapeach(self, ctx):
        await ctx.send(file=discord.File(self.amañapeach))

    @commands.command(
        aliases=["facilimario"],
        brief="Sends an image",
        description="Sends the image of Facilimario",
    )
    async def Facilimario(self, ctx):
        await ctx.send(file=discord.File(self.facilimario))

    @commands.command(
        aliases=["luiramo"],
        brief="Sends an image",
        description="Sends the image of Luiramo",
    )
    async def Luiramo(self, ctx):
        await ctx.send(file=discord.File(self.luiramo))

    @commands.command(
        aliases=["impercerbero", "imperiocancerbero"],
        brief="Sends an image",
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx):
        await ctx.send(file=discord.File(self.impercerbero))

    @commands.command(
        aliases=["impercerbero"],
        brief="Sends an image",
        description="Sends the image of Impercerbero",
    )
    async def Impercerbero(self, ctx):
        await ctx.send(file=discord.File(self.impercerbero))

    @commands.command(
        aliases=["luistoriador"],
        brief="Sends an image",
        description="Sends the image of Luistoriador",
    )
    async def Luistoriador(self, ctx):
        await ctx.send(file=discord.File(self.luistoriador))

    @commands.command(
        aliases=["filetrelay"],
        brief="Sends an image",
        description="Sends the image of Filetrelay",
    )
    async def Filetrelay(self, ctx):
        await ctx.send(file=discord.File(self.filetrelay))

    @commands.command(
        aliases=["wpcerrebe", "WPcerrebe", "Wpcerrebe", "bienjugadocerrebe"],
        brief="Sends an image",
        description="Sends the image of WPCerrebe",
    )
    async def WPCerrebe(self, ctx):
        await ctx.send(file=discord.File(self.wpcerrebe))

    @commands.command(
        aliases=["bonustars", "bonusstars", "Bonusstars"],
        brief="Sends an image",
        description="Sends the image of Bonustars",
    )
    async def Bonustars(self, ctx):
        await ctx.send(file=discord.File(self.bonustars))

    @commands.command(
        aliases=["hiddenblock", "HiddenBlock"],
        brief="Sends an image",
        description="Sends the image of Hiddenblock",
    )
    async def Hiddenblock(self, ctx):
        await ctx.send(file=discord.File(self.hiddenblock))

    @commands.command(
        aliases=["luipadres"],
        brief="Sends an image",
        description="Sends the image of Luipadres",
    )
    async def Luipadres(self, ctx):
        await ctx.send(file=discord.File(self.luipadres))

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
        await ctx.send(file=discord.File(self.misteryduel))

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
        await ctx.send(file=discord.File(self.ganerrebe))

    @commands.command(
        aliases=["cerrescritorio", "cerresktop"],
        brief="Sends an image",
        description="Sends the image of Cerrescritorio",
    )
    async def Cerrescritorio(self, ctx):
        await ctx.send(file=discord.File(self.cerrescritorio))

    @commands.command(
        aliases=["patrickmp", "patrickMP", "Patrickmp"],
        brief="Sends an image",
        description="Sends the image of PatrickMP",
    )
    async def PatrickMP(self, ctx):
        await ctx.send(file=discord.File(self.patrickmp))

    @commands.command(
        aliases=["muchokanji"],
        brief="Sends an image",
        description="Sends the image of MuchoKanji",
    )
    async def MuchoKanji(self, ctx):
        await ctx.send(file=discord.File(self.muchokanji))

    @commands.command(
        aliases=["frowaifu"],
        brief="Sends an image",
        description="Sends the image of Frowaifu",
    )
    async def Frowaifu(self, ctx):
        await ctx.send(file=discord.File(self.frowaifu))

    @commands.command(
        aliases=["toadship", "ToadShip"],
        brief="Sends a gif",
        description="Sends the gif of Toadship",
    )
    async def Toadship(self, ctx):
        await ctx.send(file=discord.File(self.toadship))

    @commands.command(
        aliases=["pinged"],
        brief="Sends a gif",
        description="Sends the gif of Pinged",
    )
    async def Pinged(self, ctx):
        await ctx.send(file=discord.File(self.pinged))

    @commands.command(
        aliases=["slicerelay", "SliceRelay"],
        brief="Sends an audio",
        description="Sends the audio of Slicerelay",
    )
    async def Slicerelay(self, ctx):
        await ctx.send(file=discord.File(self.slicerelay))

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
            await message.reply(file=discord.File(self.amogus))
        else:
            await ctx.send(file=discord.File(self.amogus))

    @commands.command(
        aliases=["symjoy"],
        brief="Sends a video",
        description="Sends the video of Symjoy",
    )
    async def Symjoy(self, ctx):
        await ctx.send(file=discord.File(self.symjoy))

    @commands.command(
        aliases=["switch"],
        brief="Sends a video",
        description="Sends the video of Switch",
    )
    async def Switch(self, ctx):
        await ctx.send(file=discord.File(self.switch))

    @commands.command(
        aliases=["typo"],
        brief="Sends a video",
        description="Sends the video of Typo",
    )
    async def Typo(self, ctx):
        await ctx.send(file=discord.File(self.typo))


def setup(client):
    client.add_cog(Media(client))
