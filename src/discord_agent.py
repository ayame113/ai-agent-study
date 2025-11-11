import discord
from dotenv import load_dotenv
import os
from agents import Agent, Runner, ModelSettings, WebSearchTool
from agents.mcp import MCPServerStdio
import asyncio

import nest_asyncio
nest_asyncio.apply()

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

client = discord.Client(
    intents=discord.Intents.all()
)



async def main():
    async with MCPServerStdio(
        name="天気予報ツール",
        params={
            # 起動コマンドは各自の環境に合わせて切り替え
            "command": "uv",
            "args": [
                "--directory",
                "/Users/r_suzuki/work/ai-agent-study/",
                "run",
                "--with",
                "mcp[cli]",
                "mcp",
                "run",
                "./src/mcp_server.py",
            ],
        },
    ) as server:
        agent = Agent(
            name="Assistant",
            model="gpt-5-mini",
            # model_settings=ModelSettings(temperature=0),
            instructions="あなたは親しみのあるdiscord botです。簡潔に応答してください。",
            mcp_servers=[server],
            # tools=[
            #     WebSearchTool(),
            # ],
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
            result = await Runner.run(agent, message.content)
            print(result.final_output)

            # メッセージが送信されたチャンネルに、AI応答を送信
            await message.channel.send(result.final_output)

        client.run(bot_token)

asyncio.run(main())
