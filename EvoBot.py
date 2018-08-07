import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "$")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot successfully booted & online.")
    print("My name is " + bot.user.name)
    print("My ID is " + bot.user.id)
    await bot.change_presence(game=discord.Game(type=2,name='$help'))

@bot.command()
async def help():
    embed = discord.Embed(title="Help page", description="This would be the help list", color=0x646666)
    await bot.say(embed=embed)

@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome!", description=f"Welcome, {member.mention} to Evolutionary!", color=0x646666)
    await bot.send_message(member, embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title=f"{userName}", description=f"You have been kicked from Evolutionary for {reason}.", color=0x646666)
        await bot.send_message(userName, embed=embed)
        await bot.kick(userName)
        embed = discord.Embed(title="", description=f"User {userName} has successfully been kicked.", color=0x646666)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ban(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.ban_members:
        embed = discord.Embed(title=f"{userName}", description=f"You have been banned from Evolutionary for {reason}.", color=0x646666)
        await bot.send_message(userName, embed=embed)
        await bot.ban(userName)
        embed = discord.Embed(title="", description=f"User {userName} has successfully been banned.", color=0x646666)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def mute(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.kick_members:
        mute_role = discord.utils.get(userName.server.roles, name='Muted') 
    if mute_role == None:
        await bot.create_role(member.server, name='Muted')
    else:
        embed = discord.Embed(title=f"{userName}", description=f"You have been muted on Evolutionary for {reason}.", color=0x646666)
        await bot.send_message(userName, embed=embed)
        await bot.add_roles(userName, mute_role)
        embed = discord.Embed(title="", description=f"User {userName} has successfully been muted.", color=0x646666)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        mute_role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, mute_role)
        embed = discord.Embed(title=f"User {member} has successfully been unmuted.", description="", color=0x646666)
        await bot.say(embed=embed)

@bot.event
async def on_member_join(member):
    if member.server.id == "476386834054905857":
        channel = bot.get_channel("476386834054905860")
        embed = discord.Embed(title=f"Welcome {member}!", description=f"to Evolutionary! Enjoy your stay.", color=0x646666)
        await bot.send_message(channel, embed=embed)
        role = discord.utils.get(member.server.roles, name='Members')
        await bot.add_roles(member, role)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.CheckFailure):
        await client.send_message(ctx.message.channel, f'✘ | You do not have access to that command.')
        return
    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

   
bot.run("NDc1MDEyMTI3OTM0MTE5OTQ3.DkY5XA.u69rTAwBa9lwp-pw9rxigAxDF6M")
