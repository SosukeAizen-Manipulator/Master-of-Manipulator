import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def join(ctx):
    
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Bağlandım, {channel.name} kanalına!")
    else:
        await ctx.send("Bir sesli kanala katılmalısınız.")

@bot.command()
async def play(ctx, url: str):
    
    if ctx.voice_client:
        if not ctx.voice_client.is_playing():
            audio_source = discord.FFmpegPCMAudio(url)
            ctx.voice_client.play(audio_source)
            await ctx.send(f"Çalınan ses dosyası: {url}")
        else:
            await ctx.send("Zaten bir ses dosyası çalıyor.")
    else:
        await ctx.send("Önce sesli kanala bağlanmam gerekiyor.")

@bot.command()
async def leave(ctx):
    
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Sesli kanaldan ayrıldım.")
    else:
        await ctx.send("Sesli kanalda değilim.")

bot.run("Token")
