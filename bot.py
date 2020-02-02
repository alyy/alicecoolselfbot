
token = "" 
prefix = "#"

import discord
from discord.ext import commands

print ("loding")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Aly is so fucking sexy")

try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def r(ctx, nick):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=nick)
                print(f"{user.name} renamed to {nick}")
            except:
                print(f"{user.name} Failed")
        print("Done!")


    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def p(ctx, newname):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=newname + user.name)
                print(f"{user.name} renamed to {newname}{username}")
            except:
                print(f"{user.name} Failed")
        print("Done!")


    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def s(ctx, suffix):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=user.name + suffix)
                print(f"{user.name} renamed to {user.name}{suffix}")
            except:
                print(f"{user.name} Failed")
        print("Done!")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def pf(ctx, newname, suffix):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=newname + user.name + suffix)
                print (f"{user.name} renamed to {newname}{user.name}{suffix}")
            except:
                print (f"{user.name} Failed")
        print ("Done!")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def reset(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=None)
                print(f"{user.name} Nickname been reset")
            except:
                print(f"{user.name} has NOT been Reset")
        print("Done!")


except:
    pass

bot.run(token, bot=False)
