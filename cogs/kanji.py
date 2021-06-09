import discord
from discord.ext import commands
from discord.utils import get
from main import GetJsonElement
import random


class Kanji(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables
    kanjijson = "kanji.json"

    # Events

    # Commands
    @commands.command(
        aliases=["kanjicompetitivo", "kanji"],
        brief="Echos, devs only",
        description="Writes whatever you want in any channel you want, devs only.",
        usage='channel_id message (User Pinging: <@user_id>, roles: "@ role_name")',
    )
    async def KanjiCompetitivo(self, ctx, limit: int = None):
        if limit == None:
            # GetJsonElement()
            pass


def setup(client):
    client.add_cog(Kanji(client))
