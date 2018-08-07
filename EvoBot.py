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

@client.event
async def on_member_join(member):
    if member.server.id == "474988884426752013":
        channel = client.get_channel("475018157405241355")
        embed = discord.Embed(title="Welcome!", description="Welcome, {member.mention} to Evolutionary!", color=0x00ff00)
        await client.say(embed=embed)
        role = discord.utils.get(member.server.roles, name='Members')
        await client.add_roles(member, role)

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
    
@client.command(pass_context=True)
@commands.has_role("Mod")
async def kick(ctx, userName: discord.Member, *, reason: str):
    await client.kick(userName)
    await client.say("**✓** | Member ``{}`` successfully kicked for **{}** ".format(userName, reason))

@client.command(pass_context=True)
@commands.has_role("Mod")
async def ban(ctx, userName: discord.Member, *, reason: str):
    await client.ban(userName)
    await client.say("**✓** | Member ``{}`` successfully banned for **{}** ".format(userName, reason))

@client.command(pass_context=True)
@commands.has_role("Mod")
async def mute(ctx, member: discord.Member, *, reason: str):
    mute_role = discord.utils.get(member.server.roles, name='Muted') 
    if mute_role == None:
        await client.create_role(member.server, 'Muted')
    else:
        await client.add_roles(member, mute_role)
        await client.say(f'**✓** | Member ``{member}`` successfully muted for **{reason}**')

@client.command()
@commands.has_role("Mod")
async def unmute(member: discord.Member):
    mute_role = discord.utils.get(member.server.roles, name='Muted')
    await client.remove_roles(member, mute_role)
    await client.say(f"**✓** | Member ``{member}`` successfully unmuted.")
    
@client.command(pass_context=True)
@commands.has_role("Mod")
async def unban(ctx, user):
    user = client.get_user_info(USERID)
    await client.unban(ctx.message.server, user) 
    await client.say(f"**✓** | User ``{user.name}`` successfully unbanned.")
   
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
