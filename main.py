import discord
import random
from discord.ext import commands

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
async def number(ctx):
    randNum = random.randint(1, 100)
    await ctx.send(f'Rastgele Sayı: {randNum}')

@bot.command()
async def meme(ctx):
    memes = [
        "https://i.pinimg.com/736x/59/6c/c5/596cc56cb5ad8ff7c3307987e1cbeb05.jpg",
        "https://i.pinimg.com/736x/f5/9d/03/f59d039884108523ad4048886bc3fc38.jpg",
        "https://i.pinimg.com/736x/05/11/66/05116661f51e7d47658fbdb4b740f853.jpg",
        "https://i.pinimg.com/736x/4c/16/7c/4c167c29b21e2c90ef51d9a60523cd8d.jpg",
        "https://i.pinimg.com/736x/2d/5d/5f/2d5d5ff1113caeb32375c7aff9abf543.jpg"
            ]
    await ctx.send(random.choice(memes))

@bot.command()
async def guess(ctx, word: str):
    await ctx.send("Kelime: " + word + "(Kolaydı)")

@bot.command()
async def eYeM(ctx):
    sentence = "Erasing You, Erasing Me." # bir oyuna refereans.

    for i in range(10):
        charS = list(sentence)
        eLs = random.randint(3, 4)

        for i in random.sample(range(len(charS)), eLs):
            charS[i] = ""
        await ctx.send("".join(charS))

bot.run("GİZLİ TOKEN BURAYA")
