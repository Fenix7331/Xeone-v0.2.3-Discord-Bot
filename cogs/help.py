import discord
import datetime
import os
import random
import asyncio
import contextlib
import json
from discord_components import *
from discord.ext import commands

client = discord.Client

update = "`All bug fixed`"

allembed = discord.Embed(title="Xeone - Utility Commands",
                         description="""
`ping` | `invite` | `mc` | `badges` | `botinfo` | `av` | `banner` | `banner server` | `icon server` | `say` | `roleinfo` | `users` | `guilds` | `boosts`
""",
                         color=0x2f3136)
allembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

modembed = discord.Embed(title="Xeone - Moderation Commands",
                         description="""
`lock` | `unlock` | `hide` | `unhide` | `purge` | `nick` | `purge`
""",
                         color=0x2f3136)
modembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

adminembed = discord.Embed(title="Xeone - Admin Commands",
                           description="""
`fuckban` | `ban` | `getlost` | `fuckoff` | `kick` | `roleall` | `hideall` | `unhideall` | `channelnuke` | `addrole` | `removerole`
""",
                           color=0x2f3136)
adminembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

antinukeembed = discord.Embed(title="Xeone - Security Feature",
                              description="""
\n>>> **Security Status: Enabled <:success:992024105975037992>\nPunishment: Ban <:EC_ban:1008981061000237087>\n\nAll AntiNuke Features Are Mentioned Below!\n```• Anti Ban\n• Anti Kick\n• Anti Unban\n• Anti Bot Add\n• Anti Channel Create\n• Anti Channel Delete\n• Anti Channel Update\n• Anti Role Create\n• Anti Role Delete\n• Anti Everyone Ping```**
""",
                              color=0x2f3136)
antinukeembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

logembed = discord.Embed(title="Xeone - Logging Commands",
                         description="""
`logging-set` | `logging-config` | `logging-delete`
""",
                         color=0x2f3136)
logembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

svembed = discord.Embed(title="Xeone - Server Role Commands",
                        description="""
**__Role Setup Commands__**\n`friend-role-set <role>` | `official-role-set <role>` | `cutie-role-set <role>` | `vip-role-set <role>` | `skid-role-set <role>`\n\n**__Use Below Commands After Setup__**\n`friend <user>` | `official <user>` | `cutie <user>` | `vip <user>` | `skid <user>`\n
""",
                        color=0x2f3136)
svembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

pfpembed = discord.Embed(title="Xeone - Auto PFP Commands",
                         description="""
`start` | `stop`\n\nNote: These Cmds Can Only Be Used By Server Owners!
""",
                         color=0x2f3136)
pfpembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

nsfwembed = discord.Embed(title="Xeone - Auto NSFW Commands",
                          description="""
`nsfw4k` | `boobs` | `pussy` | `lewd` | `lesbian` | `spank` | `cum`
""",
                          color=0x2f3136)
nsfwembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

vcembed = discord.Embed(title="Xeone - Auto Voice Commands",
                        description="""
`vchide` | `vcunhide` | `vcmute` | `vcunmute`
""",
                        color=0x2f3136)
vcembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

autoembed = discord.Embed(title="Xeone - Auto-Role Commands",
                          description="""
`autorole add [role]` | `autorole remove [role]`\n\n**__Other Cmds__**\n`roleall <role>`
""",
                          color=0x2f3136)
autoembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

funembed = discord.Embed(title="Xeone - Fun Commands",
                         description="""
`qr` | `meme` | `truth` | `dare` | `hack [user] | `gay [user]` | `gender [user]`
""",
                         color=0x2f3136)
funembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

webembed = discord.Embed(title="Xeone - Webhook Manager Commands",
                         description="""
`createhook [name]` | `delhook [name]`\n\nNote: These Cmds Can Only Be Used By Server Owners!
""",
                         color=0x2f3136)
webembed.set_footer(text="Made With 🧠 By ! Fenix#7649")

devembed = discord.Embed(title="Xeone - Developer Commands",
                         description="""
`jsk` | `g-leave` | `give badge` | `remove badge` | `guilds-ids` | `guilds-show`
""",
                         color=0x2f3136)
devembed.set_footer(text="Made With 🧠 By ! Fenix#7649")


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["h"])
    @commands.bot_has_permissions(embed_links=True)
    async def help(self, ctx):
        await self.selectboxtesting(ctx)

    async def selectboxtesting(self, ctx):
        devemoji = self.bot.get_emoji(1039471757922418729)
        webemoji = self.bot.get_emoji(1039469457220841482)
        funemoji = self.bot.get_emoji(1039466285173588008)
        autoemoji = self.bot.get_emoji(1001171036806586368)
        nsfwemoji = self.bot.get_emoji(1039128432644210769)
        vcemoji = self.bot.get_emoji(1039128137067409428)
        pfpemoji = self.bot.get_emoji(1039125588637667339)
        serverrolesemoji = self.bot.get_emoji(1000725671120752700)
        logemoji = self.bot.get_emoji(1039127839569629256)
        adminemoji = self.bot.get_emoji(1039127668773359696)
        modemoji = self.bot.get_emoji(1039127368083722270)
        antinukeemoji = self.bot.get_emoji(1039126961882136646)
        allemoji = self.bot.get_emoji(1005816928062935111)
        embed = discord.Embed(
            title="Xeone Help Menu",
            description=
            f"""**• Global Prefix: `!`\n• Total Cmd(s): {len(self.bot.commands)} | Guild(s): {len(self.bot.guilds)} | User(s): {len(self.bot.users)}\n• [Get Xeone](https://discordapp.com/oauth2/authorize?client_id=1024259879696859146&scope=bot+applications.commands&permissions=8) | [Support](https://discord.gg/introverts) | [Vote Soon](https://discord.gg/introverts)\n\n<:fenix_dash:1007475039731466320> Main Modules\n<:rep:992046915170619414> <:kdjsjs:1039126961882136646> : Security\n<:rep:992046915170619414> <a:nw_setting:1005816928062935111> : Utility\n<:rep:992046915170619414> <:lgnmod:1039127368083722270> : Moderation\n<:rep:992046915170619414> <:EC_role_icon:1039127668773359696> : Admin\n<:rep:992046915170619414> <a:nw_Users:1001171036806586368> : Autoroles\n<:rep:992046915170619414> <:zzlogging:1039127839569629256> : Logging\n\n<:fenix_dash:1007475039731466320> Other Modules\n<:rep:992046915170619414> <:badge_supporter:1000725671120752700> : Server Roles\n<:rep:992046915170619414> <a:codez_grow_karna:1039125588637667339> : Auto PFP\n<:rep:992046915170619414> <:voice_channel:1039128137067409428> : Voice Commands\n<:rep:992046915170619414> <:xanax_nsfw:1039128432644210769> : NSFW\n<:rep:992046915170619414> <:games:1039466285173588008> : Fun\n<:rep:992046915170619414> <:links:1039469457220841482> : Webhook Manager\n<:rep:992046915170619414> <:Flantic_oki_oki:1039471757922418729> : Developers </>\n\n__Use DropDown To Navigate YourSelf Through The Menu!__**""",
            color=0x2f3136)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(
            text="Made With 🧠 By ! Fenix#7649",
            icon_url=
            "https://cdn.discordapp.com/avatars/1024259879696859146/235c8d3f248e93c13175fe9f5d867a4e.webp?size=1024"
        )
        interaction1 = await ctx.send(
            embed=embed,
            components=[[
                Select(
                    placeholder="Xeone",
                    options=[
                        SelectOption(
                            label="Security",
                            description=" Show's You Security Features",
                            value="1",
                            emoji=antinukeemoji),
                        SelectOption(label="Utility",
                                     description="Show's You Utility Commands",
                                     value="2",
                                     emoji=allemoji),
                        SelectOption(
                            label="Moderation",
                            description="Show's You Moderation Commands",
                            value="3",
                            emoji=modemoji),
                        SelectOption(label="Admin",
                                     description="Show's You Admin Commands",
                                     value="4",
                                     emoji=adminemoji),
                        SelectOption(label="AutoRole",
                                     description="Show's You AutoRole Command",
                                     value="5",
                                     emoji=autoemoji),
                        SelectOption(label="Logging",
                                     description="Show's You Logging Command",
                                     value="6",
                                     emoji=logemoji),
                        SelectOption(
                            label="Server Roles",
                            description="Show's You Server Roles Command",
                            value="7",
                            emoji=serverrolesemoji),
                        SelectOption(
                            label="Auto PFP",
                            description=" Show's You Auto PFP Command",
                            value="8",
                            emoji=pfpemoji),
                        SelectOption(label="Voice Commands",
                                     description="Show's You Voice Command",
                                     value="9",
                                     emoji=vcemoji),
                        SelectOption(label="NSFW",
                                     description="Show's You NSFW Command",
                                     value="10",
                                     emoji=nsfwemoji),
                        SelectOption(label="Fun",
                                     description="Show's You Fun Command",
                                     value="11",
                                     emoji=funemoji),
                        SelectOption(
                            label="Webhook Manager",
                            description="Show's You WebHook Manager Command",
                            value="12",
                            emoji=webemoji),
                        SelectOption(
                            label="Developers </>",
                            description="Show's You Developers Command",
                            value="13",
                            emoji=devemoji),
                    ],
                    custom_id="selectboxtesting")
            ]])
        while True:
            try:
                interaction2 = await self.bot.wait_for(
                    "select_option",
                    check=lambda inter: inter.custom_id == "selectboxtesting",
                    timeout=
                    999999999999999999999999999999999999999999999999999999999999999999999
                )
                res = interaction2.values[0]
                if res == "1":
                    await interaction2.send(embed=antinukeembed)
                if res == "2":
                    await interaction2.send(embed=allembed)
                if res == "3":
                    await interaction2.send(embed=modembed)
                if res == "4":
                    await interaction2.send(embed=adminembed)
                if res == "5":
                    await interaction2.send(embed=autoembed)
                if res == "6":
                    await interaction2.send(embed=logembed)
                if res == "7":
                    await interaction2.send(embed=svembed)
                if res == "8":
                    await interaction2.send(embed=pfpembed)
                if res == "9":
                    await interaction2.send(embed=vcembed)
                if res == "10":
                    await interaction2.send(embed=nsfwembed)
                if res == "11":
                    await interaction2.send(embed=funembed)
                if res == "12":
                    await interaction2.send(embed=webembed)
                if res == "13":
                    await interaction2.send(embed=devembed)
                else:
                    pass
            except discord.errors.HTTPException:
                error = "Error"
                print(error)


def setup(bot):
    bot.add_cog(help(bot))
