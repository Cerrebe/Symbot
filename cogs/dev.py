import discord
from discord.ext import commands
from discord.utils import get
from discord import DMChannel
from main import devs
from main import client as mainclient


class Dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Variables

    # Regular Functions
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("dev cogloaded")

    # Commands
    @commands.command(
        aliases=["echo"],
        brief="Echos, devs only",
        description="Writes whatever you want in any channel you want, devs only.",
        usage='channel_id message (User Pinging: <@user_id>, roles: "@ role_name")',
        pass_context=True,
    )
    async def Echo(self, ctx, id, *echowords: str):
        if ctx.message.author.id in devs:
            msg = list()
            sendchannel = mainclient.get_channel(int(id))
            for i in range(len(echowords)):
                if echowords[i].startswith("@ "):
                    msg.append(
                        get(
                            sendchannel.guild.roles, name=echowords[i].replace("@ ", "")
                        ).mention
                    )
                else:
                    msg.append(echowords[i])
            await sendchannel.send(" ".join(msg[:]))
        else:
            await ctx.send("Bot developers only :<")

    @commands.command(
        aliases=["dm"],
        brief="DM's a user, devs only",
        descripton="Sends a Direct Message to a user, devs only",
        pass_context=True,
    )
    async def DM(self, ctx, id, *args: str):
        if ctx.message.author.id in devs:
            user = await mainclient.fetch_user(id)
            await user.send(" ".join(args[:]))


def setup(client):
    client.add_cog(Dev(client))
