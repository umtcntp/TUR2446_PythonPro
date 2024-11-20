import discord
from discord.ext import commands
from bot_token import token
from sifre import sifre_olustur

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def rastgele_sifre(ctx ):
    sifre = sifre_olustur(8)
    await ctx.send(f'İste gizemli sifren {sifre}')


bot.run(token)
