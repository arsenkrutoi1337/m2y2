import discord
from discord.ext import commands
import random 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ecology(ctx,eco="создание товара с разу уже из экологичных и переробатываемых материалов,Выключайте компьютер ночью, это поможет сэкономить до 1000 кВт ежемесячно,сортировать мусор"):
    ecology=random.choice(eco)
    await ctx.send(eco)

bot.run("MTEwOTM4NTIwOTkxODUyNTQ3MA.GI7416.LYqHXFy4ChypkzZQbjmfOk_pM1YXo5W9cg9J_8")