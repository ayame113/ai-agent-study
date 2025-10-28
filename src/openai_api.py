from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openai = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)

# 使用するAIモデル
model = "gpt-4.1-mini"

# AIのカスタマイズ
instructions = "あなたはフレンドリーな大学生です。"

# AIへ送信する文章
input = "今日のニュースを教えて"

# AI応答を生成
response = openai.responses.create(
  model=model,
  instructions=instructions,
  input=input,
  stream=True,
  # tools=[
  #   { "type": "web_search" },
  # ],
  # temperature=0, # 0〜1で調整
  # reasoning={
  #     # 推論のレベルを設定 (low, medium, high)
  #     "effort": "high",
  # },
)

# 結果を表示
# print(response.output_text)
# 結果を表示
for output in response:
  if output.type == "response.output_text.delta":
    # テキスト出力 (1文字ずつ)
    print(output.delta, end="", flush=True)
  elif output.type == "response.output_text.done":
    # テキスト出力(文章ごと)
    print("\n======")
    print(output.type)
    print(output.text)
    print("\n")
  else:
    # その他の出力
    print("\n======")
    print(output.type)
    print(output)
    print("\n")
