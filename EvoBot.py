import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import time
import random
import sys
import traceback
import json

Client = discord.Client()
client = commands.Bot(command_prefix = "$")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot successfully booted & online.")
    print("My name is " + client.user.name)
    print("My ID is " + client.user.id)
    await client.change_presence(game=discord.Game(type=2,name='$help'))

@bot.event
async def on_member_join(member):
    if member.server.id == "476386834054905857":
        channel = bot.get_channel("476386834054905860")
        embed = discord.Embed(title=f"Welcome {member}!", description=f"to Evolutionary! Enjoy your stay.", color=0x646666)
        await bot.send_message(channel, embed=embed)
        role = discord.utils.get(member.server.roles, name='Members')
        await bot.add_roles(member, role)

@client.command(pass_context=True)
@commands.has_role("Mod")
async def echo(ctx, *, args):
    await client.say(args)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def ping(ctx):
        '''Ping bot'''
        channel = ctx.message.channel
        t1 = time.perf_counter()
        msg = await client.say("Pong!")
        t2 = time.perf_counter()
        await client.edit_message(msg, "Pong! `{}ms`".format(round((t2-t1)*1000)))

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await client.purge_from(ctx.message.channel, limit=int(amount) + 1)
    await client.say ('**✓** | Messages cleared from chat history.')

@client.command(pass_context=True)
@commands.has_role("Management")
async def rank(ctx, member: discord.Member, rank: str):
    if rank == "Developers":
        role = discord.utils.get(member.server.roles, name='Developers')
        await client.add_roles(member, role)
        return await client.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "Support":
        role = discord.utils.get(member.server.roles, name='Support')
        await client.add_roles(member, role)
        return await client.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "Coders":
        role = discord.utils.get(member.server.roles, name='Coders')
        await client.add_roles(member, role)
        return await client.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "Mod":
        role = discord.utils.get(member.server.roles, name='Mod')
        await client.add_roles(member, role)
        return await client.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "Partners":
        role = discord.utils.get(member.server.roles, name='Partners')
        await client.add_roles(member, role)
        return await client.say(f'Successfully ranked user ``{member}`` to **{role}**')
    if rank == "W.I.P":
        role = discord.utils.get(member.server.roles, name='W.I.P')
        await client.add_roles(member, role)
        return await client.say(f'**✓** | Successfully ranked user ``{member}`` to **{role}**')
    
@bot.command(pass_context=True)
async def kick(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title=f"{userName}", description=f"You have been kicked from Evolutionary for {reason}.", color=0x646666)
        await bot.send_message(userName, embed=embed)
        await bot.kick(userName)
        embed = discord.Embed(title="", description=f"User {userName} has been successfully kicked.", color=0x646666)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ban(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title=f"{userName}", description=f"You have been banned from Evolutionary for {reason}.", color=0x646666)
        await bot.send_message(userName, embed=embed)
        await bot.ban(userName)
        embed = discord.Embed(title="", description=f"User {userName} has been successfully banned.", color=0x646666)
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
      
@client.command()
async def contribute():
        embed = discord.Embed(title="By donating, you help to keep the bot run 24/7 and help fund future updates!", description="[**Click here** to grab the donation link!](https://paypal.me/HarryOliver240)", color=0x00ff00)
        await client.say(embed=embed)
        
@client.command()
async def donate():
        embed = discord.Embed(title="By donating, you help to keep the bot run 24/7 and help fund future updates!", description="[**Click here** to grab the donation link!](https://paypal.me/HarryOliver240)", color=0x00ff00)
        await client.say(embed=embed)
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.CheckFailure):
        await client.send_message(ctx.message.channel, f'✘ | You do not have access to that command.')
        return
    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

   
    
client.run("NDc1MDEyMTI3OTM0MTE5OTQ3.DkY5XA.u69rTAwBa9lwp-pw9rxigAxDF6M")
