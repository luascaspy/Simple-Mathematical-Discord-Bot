import discord
import json
import math as mh
from discord.ext import commands

#Bot made by Luascas
#https://github.com/luascaspy

#Connection Settings
with open('config/config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefixo = infos['prefix']

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefixo, intents=intents)


#Initializing client
@client.event
async def on_ready():
    print('Hi, Human. Logged in as {0.user}'.format(client))
    bot_status = ".commands"
    await client.change_presence(activity=discord.Game(bot_status))   

#MathBot Commands
@client.command()
async def mathbot(ctx):
    await ctx.send(f'Hi {ctx.author.mention}, my name is Math! My job is to help you with math. Type .commands')

@client.command()
async def commands(ctx):
    await ctx.send(f'.factorial = Return x factorial as an integer.\n .exp = Return e raised to the power x, where e = 2.718281… is the base of natural logarithms.\n .log = Return the natural logarithm of x (to base 1).\n .log2 = Return the base-2 logarithm of x.\n .log10 = Return the base-10 logarithm of x.\n .cos = Return the cosine of x radians.\n .sine = Return the sine of x radians.\n .asin = Return the arc sine of x, in radians. The result is between -pi/2 and pi/2.\n .tan = Return the tangent of x radians.\n .atan = Return the arc tangent of x, in radians. The result is between -pi/2 and pi/2.\n .const_pi = The mathematical constant π.\n .const_e = The mathematical constant e.\n')

#Operations commands
@client.command()
async def factorial(ctx, num):
    submit_factorial = mh.factorial(int(num))
    await ctx.send(f'The result is {submit_factorial}.')

@client.command()
async def exp(ctx, num):
    submit_exp = mh.exp(int(num))
    await ctx.send(f'The result is {submit_exp}.')

@client.command()
async def log(ctx, num):
    submit_log = mh.log(int(num))
    await ctx.send(f'The result is {submit_log}.')

@client.command()
async def log2(ctx, num):
    submit_log2 = mh.log2(int(num))
    await ctx.send(f'The result is {submit_log2}.')

@client.command()
async def log10(ctx, num):
    submit_log10 = mh.log10(int(num))
    await ctx.send(f'The result is {submit_log10}.') 

@client.command()
async def cos(ctx, num):
    submit_cos = mh.cos(int(num))
    await ctx.send(f'The result is {submit_cos}.')           

@client.command()
async def sine(ctx, num):
    submit_sin = mh.sin(int(num))
    await ctx.send(f'The result is {submit_sin}.')

@client.command()
async def asin(ctx, num):
    submit_asin = mh.asin(int(num))
    await ctx.send(f'The result is {submit_asin}.')

@client.command()
async def tan(ctx, num):
    submit_tan = mh.tan(int(num))
    await ctx.send(f'The result is {submit_tan}.')

@client.command()
async def atan(ctx, num):
    submit_atan = mh.atan(int(num))
    await ctx.send(f'The result is {submit_atan}.')       

@client.command()
async def const_pi(ctx):
    submit_pi = mh.pi
    await ctx.send(f'π = {submit_pi}.')

@client.command()
async def const_e(ctx):
    submit_e = mh.e
    await ctx.send(f'e = {submit_e}.')

client.run(TOKEN)
