import discord 
from discord import app_commands
from discord.ext import commands 


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()


lista_palavroes = [
    
    "merda", "porra", "caralho", "puta", "bosta", "cacete", "caceta",
    "cagado", "cagada", "cuzão", "cuzona", "buceta", "pica", "piroca",
    "rola", "pauduro", "foder", "fodido", "fodida", "foda", "pau",
    "vagabunda", "vagabundo", "idiota", "imbecil", "otário", "otaria",
    "corno", "cornudo", "safado", "safada", "putaria", "babaca",
    
 
    "krl", "krlh", "pqpa", "pqp", "poha", "pnc", "tnc", "vtnc",
    "foda-se", "fdse", "fdp", "fdps", "bct", "bcta", "vgbd", "vgbda",
    "vtmnc", "cuz0", "cuz0n", "cuz0na", "ctz",
    
 
    "preto", "preta", "viado", "veado", "bicha", "nigg", "gay",
    
 
    "m3rda", "p0rr4", "c4r4lh0", "put4", "f0d4", "f0d1d0"
]

@bot.event
async def on_message(message): 
    
    if message.author == bot.user:
        return

    conteudo = message.content.lower()

    
    if any(palavrao in conteudo for palavrao in lista_palavroes):
        await message.channel.send(f"Ei {message.author.mention} boboca, não pode palavrão aqui!")
        await message.delete()



    if "discord.gg/" in conteudo or "https://" in conteudo:
        await message.channel.send(f"Ei {message.author.mention} boboca, não pode links aqui!")
        await message.delete()

    await bot.process_commands(message)

bot.run("YOUR TOKEN")

