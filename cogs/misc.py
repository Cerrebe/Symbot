import discord
from discord.ext import commands
from discord.utils import get
import asyncio


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables
    mpdocument = "https://docs.google.com/spreadsheets/d/1z-eeH8Q1c3uJliE5v_K_MkNDp30SVGam2cyZvDE56Oo/edit?usp=sharing"

    # Regular Functions

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("misc cog loaded")

    # Commands
    @commands.command(
        aliases=["facilito"],
        brief="Sends ASCII Art",
        description="Sends the ASCII Art of Facilito",
    )
    async def Facilito(self, ctx):
        await ctx.send(
            ".  ━━━━━-╮\n ╰┃ ┣▇━▇\n ┃ ┃  ╰━▅╮ \n ╰┳╯ ╰━━┳╯F A S I L I T O\n  ╰╮ ┳━━╯ E L\n ▕▔▋ ╰╮╭━╮ T U T O R I A L\n ╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n ▏  ▔▔▔▔▔▔▔  O O┃ \n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n ▏╳▕▇▇▕ ▏╳▕▇▇▕\n ╲▂╱╲▂╱ ╲▂╱╲▂╱"
        )

    @commands.command(
        aliases=["symphonia"],
        brief="@Slice Juega Symphonia",
        description="Pings the role @Slice Juega Symphonia",
    )
    async def Symphonia(self, ctx):
        sjs = get(ctx.guild.roles, name="Slice Juega Symphonia")
        await ctx.send(sjs.mention)

    @commands.command(
        aliases=["mpdocument", "MPdocument", "Mpdocument"],
        brief="Sends the document of Mario Party",
        description="Sends a link to the googledocs of Mario Party",
    )
    async def MPDocument(self, ctx):
        ctx.send(self.mpdocument)

    @commands.command(
        aliases=["di"],
        brief="Says something on the current channel",
        description="Says something on the current channel",
        pass_context=True,
    )
    async def Di(self, ctx, *text: str):
        await ctx.send(" ".join(text[:]))

    @commands.command(
        aliases=["dir"],
        brief="Same as Di but with reply",
        description="Says something on the current channel, the message will reply to the same message as the reply of the command message",
        pass_context=True,
    )
    async def Dir(self, ctx, *text: str):
        if ctx.message.reference != None:
            id = ctx.message.reference.message_id
            channel = ctx.channel
            message = await channel.fetch_message(id)
            await message.reply(" ".join(text[:]))

    @commands.command(
        aliases=["timer"],
        brief="Creates a timer",
        description="Creates a real time updating timer",
        pass_context=True,
    )
    async def Timer(self, ctx, number: int):
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


def setup(client):
    client.add_cog(Misc(client))
