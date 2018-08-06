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
    await client.change_presence(game=discord.Game(type=2,name='EvoBot | W.I.P'))

@client.event
async def on_member_join(member):
    if member.server.id == "474988884426752013":
        channel = client.get_channel("475018157405241355")
        await client.send_message(channel, f":white_check_mark: Welcome {member.mention} To **Evolutionary**! Our goal is to support people new to coding languages & help them with whatever they need!")
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
    await client.say ('Messages cleared from chat history.')

@client.command(pass_context=True)
@commands.has_role("Management")
async def rank(ctx,member: discord.Member, rank: str):
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
        return await client.say(f'Successfully ranked user ``{member}`` to **{role}**')
    
@client.command(pass_context=True)
@commands.has_role("Mod")
async def kick(ctx, userName: discord.Member, *, reason: str):
    await client.kick(userName)
    await client.say("Member ``{}`` successfully kicked for **{}** ".format(userName, reason))

@client.command(pass_context=True)
@commands.has_role("Mod")
async def ban(ctx, userName: discord.Member, *, reason: str):
    await client.ban(userName)
    await client.say("Member ``{}`` successfully banned for **{}** ".format(userName, reason))

@client.command(pass_context=True)
@commands.has_role("Mod")
async def mute(ctx, member: discord.Member, *, reason: str):
    mute_role = discord.utils.get(member.server.roles, name='Muted') 
    if mute_role == None:
        await client.create_role(member.server, 'Muted')
    else:
        await client.add_roles(member, mute_role)
        await client.say(f'Member ``{member}`` successfully muted for **{reason}**')

@client.command()
@commands.has_role("Management")
async def unmute(member: discord.Member):
    mute_role = discord.utils.get(member.server.roles, name='Muted')
    await client.remove_roles(member, mute_role)
    await client.say(f"Member ``{member}`` successfully unmuted.")

@client.event
async def on_command_error(error, ctx):
    await client.send_message(ctx.message.channel, f'<:xx:475004317330309120> You do not have access to that command.')
   
    
client.run("NDc1MDEyMTI3OTM0MTE5OTQ3.DkY5XA.u69rTAwBa9lwp-pw9rxigAxDF6M")
