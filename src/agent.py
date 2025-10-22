from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings, WebSearchTool
from agents.mcp import MCPServerStdio
import asyncio

load_dotenv()


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
          instructions="あなたはフレンドリーな大学生です。",
          mcp_servers=[server],
          # tools=[
          #     WebSearchTool(),
          # ],
      )
      result = await Runner.run(agent, "今日の長野県の天気を教えてください。")
      print(result.final_output)

asyncio.run(main())
