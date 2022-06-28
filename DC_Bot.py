import discord
from discord.ext  import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = "m.",intents = intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")
    await bot.change_presence(activity=discord.Game(name="discord.gg/moonfall"),status=discord.Status.online)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,*,reason=None):
    if member is None:
        await ctx.reply("Member")
        return
    await member.ban(reason=reason)
    
    await ctx.reply(f"{member.name} wurde gebannt! UwU")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason=None):
    if member is None:
        await ctx.reply("Member")
        return
    await member.kick(reason=reason)
    
    await ctx.reply(f"{member.name} wurde gekickt! UwU")


@bot.command()
async def ping(ctx):
    await ctx.reply("Pong")

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, id: int = None):
    if id == None:
        await ctx.send('Oopsies but you need an ID!')

    else:
        if len(str(id)) == 18:
            user = await bot.fetch_user(id)

            await ctx.guild.unban(user)
            await ctx.send(f' {id} wurde entbannt! Wilkommen zurück!')

        else:
            await ctx.send(f'Oh! {id} Ich habe die ID nicht gefunden, versuche es erneut!')
    



