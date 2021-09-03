import discord
from discord.channel import VoiceChannel
from discord.ext import commands
from discord import FFmpegPCMAudio
from main import devs
from main import client as mainclient
import youtube_dl
import os


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables
    iMaxDuration = 10
    # Regular Functions

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("voice cog loaded")

    # Commands
    @commands.command(
        aliases=["join"],
        brief="Joins to the vc you're currently in.",
        description="Joins to the voice chat you're currently in. Does nothing if you're not in voice chat.",
        pass_context=True,
    )
    async def Join(self, ctx):
        if ctx.message.author.id in devs:
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
            else:
                print("a")

    @commands.command(
        aliases=["leave"],
        brief="Leaves vc.",
        description="Leaves from the voice chat channel.",
        pass_context=True,
    )
    async def Leave(self, ctx):
        if ctx.message.author.id in devs:
            if ctx.voice.client:
                await ctx.guild.voice_client.disconnect()
            else:
                print("puto")

    @commands.command(
        aliases=["pause"],
        brief="Pauses current audio.",
        description="Pauses currently playing audio.",
        pass_context=True,
    )
    async def Pause(self, ctx):
        if ctx.message.author.id in devs:
            voice = discord.utils.get(mainclient.voice_clients, guild=ctx.guild)
            if voice.is_playing():
                voice.pause()
            else:
                await print("jaja no")

    @commands.command(
        aliases=["resume"],
        brief="Resumes audio.",
        description="Resumes the paused audio.",
        pass_context=True,
    )
    async def Resume(self, ctx):
        if ctx.message.author.id in devs:
            voice = discord.utils.get(mainclient.voice_clients, guild=ctx.guild)
            if voice.is_paused():
                voice.resume()
            else:
                await print("jaja no")

    @commands.command(
        aliases=["stop"],
        brief="Stops audio.",
        description="Stops Playing audio.",
        pass_context=True,
    )
    async def Stop(self, ctx):
        if ctx.message.author.id in devs:
            voice = discord.utils.get(mainclient.voice_clients, guild=ctx.guild)
            voice.stop()

    @commands.command(
        aliases=["play"],
        brief="Plays audio from a video.",
        description="Plays audio from a Youtube Video.",
        pass_context=True,
    )
    async def Play(self, ctx, arg: str):
        if ctx.message.author.id in devs:
            audio = os.path.isfile("audio.mp3")
            try:
                if audio:
                    os.remove("audio.mp3")
            except PermissionError:
                await ctx.send("puto")

            voice = discord.utils.get(mainclient.voice_clients, guild=ctx.guild)
            if not voice.is_connected():
                await VoiceChannel.connect()
            # source = FFmpegPCMAudio(arg)
            # player = voice.play(source)
            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([arg])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "audio.mp3")
            voice.play(discord.FFmpegPCMAudio("audio.mp3"))


def setup(client):
    client.add_cog(Voice(client))
