import asyncio
import discord
import json
from discord.ext import commands


class Autorole(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Bot = bot


    async def update_data(self,newdata:dict):
        with open("autorole.json", "w") as write_mode:
            json.dump(newdata, write_mode , indent=3)


    async def get_data(self,guild:discord.Guild):
        with open("autorole.json" , "r") as read:
            data:dict = json.load(read)

        if str(guild.id) not in list(data.keys()):
            data[guild.id] = []
            return None
        else:
            return data[str(guild.id)]


    async def get_role(self,guild:discord.Guild):
        return await self.get_data(guild=guild)


    async def add_role(self,guild: discord.Guild, role: discord.Role):
        with open("autorole.json", "r") as read_mode:
            data: dict = json.load(read_mode)

        if str(guild.id) in list(data.keys()):
            if role.id in data[str(guild.id)]:
                return False
            else:
                data[str(guild.id)].append(role.id)
                await self.update_data(data)
                return True
        else:
            data[str(guild.id)] = [role.id]
            await self.update_data(data)
            return True


    async def remove_role(self,guild: discord.Guild, role: discord.Role):
        with open("autorole.json", "r") as read_mode:
            data = json.load(read_mode)

        if str(guild.id) in list(data.keys()):
            if role.id in data[str(guild.id)]:
                data[str(guild.id)].remove(role.id)
                await self.update_data(data)
                return True
            else:
                return False
        else:
            data[str(guild.id)] = []
            await self.update_data(data)
            return False


    async def autorole_update(self,member:discord.Member):
        roles = await self.get_role(member.guild)
        if roles == None:
            return False
        else:
            for role in roles:
                await member.add_roles(discord.utils.get(member.guild.roles , id = int(role)))
            return True


    @commands.group(name="autorole", aliases=["autoroles"] , invoke_without_command = True)
    async def autorole(self,ctx):
        embed = discord.Embed(color=0x2f3136, 
                  title="Xeone - Autorole Commands",
                  description=f"`autorole add` | `autorole remove`")
        embed.set_thumbnail(url='')
        await ctx.reply(embed = embed, mention_author = False )

    @autorole.command(name = 'add')
    @commands.has_permissions(administrator = True)
    async def auto_add(self,ctx,role:commands.RoleConverter):
        if role.position > ctx.guild.me.top_role.position:
            await ctx.reply(f"Please Put My Role Above This {role}", mention_author = False)
        elif role.position > ctx.guild.me.top_role.position:
            await ctx.reply(f"You Must Have Above Role From The Role {role} To Add Any Autoroles" , mention_author = False)
        else:
            result = await self.add_role(ctx.guild , role=role)
            
            if  result ==  True and role.permissions.administrator:
                await ctx.reply(f"Added {role.mention} To My Autorole DataBase For This Server" ,mention_author = False)
            elif result == True:
                await ctx.reply(f"Added {role.mention} To My Autorole DataBase For This Server!" ,mention_author = False)
            else:
                await ctx.reply(f"{role.mention} Is Already In Autorole!" , mention_author = False)


    @autorole.command(name = 'remove' )
    @commands.has_permissions(administrator = True)
    async def auto_remopve(self,ctx,role:commands.RoleConverter):
        if await self.remove_role(ctx.guild , role=role) == True:
            await ctx.reply(f"Removed {role} From My Autorole Database" ,mention_author = False)
        else:
            await ctx.reply(f"No Autorole Setupped Please Setup First!" , mention_author = False)


    
    
    @auto_add.error
    async def on_auto_add_error(self,ctx,error):
        if isinstance(error , commands.BadArgument):
            message = await ctx.reply("Please provide valid role <3 !" , mention_author = False)
            await asyncio.sleep(5)
            try:
                await message.delete()
            except:
                ...
        elif isinstance(error ,     commands.MissingPermissions) :
            message = await ctx.reply("You need `Administrator` permission to run this command <3 !" , mention_author = False)
            await asyncio.sleep(5)
            try:
                  await message.delete()
            except:
                    ...
    
    
    
    
    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        await self.autorole_update(member=member)


def setup(bot):
    bot.add_cog(Autorole(bot))
