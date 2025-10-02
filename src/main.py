import discord
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()

client = discord.Client(intents=intents)

openai = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

@client.event
async def on_ready():
    print("botが起動しました")

@client.event
async def on_message(message):
    # 自分が送信したメッセージに対しては反応しない
    if message.author == client.user:
        return
    # 自分にメンションされた時しか反応しない
    if client.user not in message.mentions:
        return
    # AI応答を生成
    response = openai.responses.create(
        model="gpt-5-mini",
        instructions="あなたは親しみのあるdiscord botです。簡潔に応答してください。",
        input=message.content,
    )

    print(response.output_text)

    # メッセージが送信されたチャンネルに、AI応答を送信
    await message.channel.send(response.output_text)

client.run(bot_token)
