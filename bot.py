import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# 環境変数をロード
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Botの設定
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} がオンラインになりました！")
    
    # ステータスを「〜をプレイ中」に設定
    activity = discord.Game(name="フォートナイト 🎮")
    await bot.change_presence(activity=activity)

# Botを起動
bot.run(TOKEN)
