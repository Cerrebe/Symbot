import discord
from discord.ext import commands
from discord.utils import get
import asyncio


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events

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
        aliases=["facilipeach"],
        brief="Sends an image",
        description="Sends the image of Facilipeach",
    )
    async def Facilipeach(self, ctx):
        await ctx.send(file=discord.File("images/facilipeach.png"))

    @commands.command(
        aliases=["muchokanji"],
        brief="Sends an image",
        description="Sends the image of MuchoKanji",
    )
    async def MuchoKanji(self, ctx):
        await ctx.send(file=discord.File("images/muchokanji.png"))

    @commands.command(
        aliases=["symphonia"],
        brief="@Slice Juega Symphonia",
        description="Pings the role @Slice Juega Symphonia",
    )
    async def Symphonia(self, ctx):
        sjs = get(ctx.guild.roles, name="Slice Juega Symphonia")
        await ctx.send(sjs.mention)

    @commands.command(
        aliases=["di"],
        brief="Says something on the current channel",
        description="Says something on the current channel",
        pass_context=True,
    )
    async def Di(ctx, *text: str):
        await ctx.send(" ".join(text[:]))

    @commands.command(
        aliases=["timer"],
        brief="Creates a timer",
        description="Creates a real time updating timer",
        pass_context=True,
    )
    async def Timer(ctx, number: int):
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
