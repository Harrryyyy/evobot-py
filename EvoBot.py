import discord
from discord.ext import commands
import asyncio
import time
import random

bot = commands.Bot(command_prefix = "!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot successfully booted & online.")
    print("My name is " + bot.user.name)
    print("My ID is " + bot.user.id)
    await bot.change_presence(game=discord.Game(type=2,name='with subjects'))

@bot.event
async def on_member_join(member):
    if member.server.id == "476386834054905857":
        channel = discord.utils.get(member.server.channels, name='welcome-messages')
        embed = discord.Embed(title=f"Welcome {member}!", description=f"to Evolutionary! Enjoy your stay.", color=0x646666)
        await bot.send_message(channel, embed=embed)
        role = discord.utils.get(member.server.roles, name='Members')
        await bot.add_roles(member, role)

@bot.command(pass_context=True)
@commands.has_role("Mod")
async def echo(ctx, *, args):
    await bot.say(args)
    await bot.delete_message(ctx.message)

@bot.command()
async def changesubject():
    subject = ['Minecraft', 'Life', 'Sandwiches', 'Computers', 'Weather', 'Sleep,', 'Sports', 'Music', 'Movies', 'Food', 'TV Shows', 'Hobbies', 'Pet']
    embed = discord.Embed(title="", description=f"Subject successfully changed. New subject is **{subject}**", COLOR=0x646666)
    await bot.say(embed=embed)
    
    
@bot.command()
async def ping():
        t1=time.perf_counter()
        msg=await bot.say(embed=discord.Embed(title='\U0001f3d3 Pinging...',colour=0xFFD700))
        t2=time.perf_counter()
        await bot.edit_message(msg, embed=discord.Embed(title='\U0001f3d3 Pong!',description=f'**{round((t2-t1)*1000)}** milliseconds',colour=discord.Colour.green()))

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await bot.purge_from(ctx.message.channel, limit=int(amount) + 1)
    await bot.say ('Messages cleared from chat history.')

@bot.command(pass_context=True)
@commands.has_role("Management")
async def rank(ctx,member: discord.Member, rank: str):
    if rank == "Developers":
        role = discord.utils.get(member.server.roles, name='Developers')
        await bot.add_roles(member, role)
        return await bot.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "Coders":
        role = discord.utils.get(member.server.roles, name='Coders')
        await bot.add_roles(member, role)
        return await bot.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "Mod":
        role = discord.utils.get(member.server.roles, name='Mod')
        await bot.add_roles(member, role)
        return await bot.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "Partners":
        role = discord.utils.get(member.server.roles, name='Partners')
        await bot.add_roles(member, role)
        return await bot.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "W.I.P":
        role = discord.utils.get(member.server.roles, name='W.I.P')
        await bot.add_roles(member, role)
        return await bot.say(f'Successfully ranked user ``{member}`` to **{role}**')
    
@bot.command(pass_context=True)
async def kick(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title=f"{userName}", description=f"You have been kicked from Evolutionary for {reason}.", color=0x646666)
        await bot.send_message(userName, embed=embed)
        await bot.kick(userName)
        embed = discord.Embed(title="", description=f"User {userName} has successfully been kicked.", color=0x646666)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Mod")
async def ban(ctx, userName: discord.Member, *, reason: str):
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



bot.run("NDgzNjAwMTg0NjE4NTE2NTEw.DmVzcA.ytVRVAGdge938Y0Fe-3YmUxm3JQ")
