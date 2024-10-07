import discord
from discord.ext import commands

from apikey import *

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix="s!", intents=intents)

@client.event
async def on_ready():
    print('Saturn está ligado! Bom dia mundo!!')

@client.command()
async def ola(ctx):
    await ctx.send('Olá, eu me chamo Saturn! é um prazer te conhecer! fui desenvolvido por @eugabe__')

@client.command()
async def vvif(ctx):
    await ctx.send('Olá, pelo jeito você quer uma informação sobre Valorant! Deixe me te ajudar, valorant é um jogo competivo 5x5!')

@client.command()
async def fala(ctx, arg):
    await ctx.send(arg)

@client.command()
async def info(ctx, *, member: discord.Member):
    await ctx.send(f'{member} entrou em {member.joined_at}')

@client.command()
async def status(ctx:commands.Context):
    await client.change_presence(status=discord.Status.do_not_disturb , activity=discord.Activity(type=discord.ActivityType.listening, name='1993 from Matue') )

client.run(bot_token)
