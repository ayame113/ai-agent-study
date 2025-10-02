import discord
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("botが起動しました")

@client.event
async def on_message(message):
    # 自分に対しては反応しない
    if message.author == client.user:
        return

    # メッセージが送信されたチャンネルに、同じメッセージをオウム返しする
    await message.channel.send(message.content)

client.run(bot_token)
