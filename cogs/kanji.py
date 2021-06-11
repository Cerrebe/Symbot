import discord
from discord.ext import commands
import random
import json


class Kanji(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables
    kanjijson = "kanji.json"
    with open(kanjijson, "r", encoding="utf8") as JsonFile:
        kanjidata = json.load(JsonFile)
    lastKanjiID = None

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
        print("kanji cog loaded")

    # Commands
    @commands.command(
        aliases=["kanjicompetitivo", "kanji"],
        brief="Sends a Kanji",
        description="Sends a kanji, can be limited by heising number",
        usage="limit(optional)",
    )
    async def KanjiCompetitivo(self, ctx, limit: int = 2041):
        limit -= 1
        id = random.randint(0, limit)
        await ctx.send(self.GetKanjiByID(id))
        self.lastKanjiID = id

    @commands.command(
        aliases=["lastkanji", "kanjilast"],
        brief="Sends the last kanji",
        description="Sends the last kanji that has been sent by KanjiCompetitivo",
    )
    async def LastKanji(self, ctx):
        if self.lastKanjiID == None:
            await ctx.send("No kanji was sent recently")
            return
        await ctx.send(self.GetKanjiByID(self.lastKanjiID))

    @commands.command(
        aliases=["lastkanjiname", "kanjilastname", "lastname", "namelast"],
        brief="Sends the keyword of the last kanji",
        description="Sends the keyword of the last kanji that has been sent by KanjiCompetitivo",
    )
    async def LastKanjiName(self, ctx):
        if self.lastKanjiID == None:
            await ctx.send("No kanji was sent recently")
            return
        await ctx.send(self.GetKanjiName(self.GetKanjiByID(self.lastKanjiID)))


def setup(client):
    client.add_cog(Kanji(client))
