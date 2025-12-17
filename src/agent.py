from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings, WebSearchTool, ItemHelpers
from openai.types.responses import ResponseTextDeltaEvent, ResponseOutputItemAddedEvent, ResponseOutputItemDoneEvent
from openai.types.shared import Reasoning
from agents.mcp import MCPServerStdio
import asyncio

load_dotenv()

# AIへの指示
instructions = "あなたはフレンドリーな大学生です。"
# ユーザーからの入力
input = "今日の長野県の天気を教えてください。"

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
            instructions=instructions,
            mcp_servers=[server],
            # tools=[
            #     WebSearchTool(),
            # ],
        )

        result = Runner.run_streamed(agent, input)

        # 進捗状況を表示
        async for event in result.stream_events():
            if event.type == "raw_response_event":
                if isinstance(event.data, ResponseTextDeltaEvent):
                    print(event.data.delta, end="", flush=True)
                elif isinstance(event.data, ResponseOutputItemDoneEvent):
                    if event.data.item.type == "web_search_call":
                        print(f"\n-- Web search: {event.data.item.action}")
                    else:
                        print(f"-- Output item started: [{event.data.item.type}] {event.data.item}")
                else:
                    print(f"-- Raw response delta: {event.data.type}")
                continue
            elif event.type == "run_item_stream_event":
                if event.item.type == "tool_call_item":
                    print("-- Tool was called")
                elif event.item.type == "tool_call_output_item":
                    print(f"-- Tool output: {event.item.output}")
                elif event.item.type == "message_output_item":
                    print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
            else:
                print(f"-- Event: {event.type}")


        # 最終結果を表示
        print("\n============================")
        print("Final Output:")
        print(result.final_output)


asyncio.run(main())
