from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openai = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# 使用するAIモデル
model = "gpt-5-mini"

# AIのカスタマイズ
instructions = "あなたはフレンドリーな大学生です。"

# AIへ送信する文章
input = "こんにちは"

# AI応答を生成
response = openai.responses.create(
    model=model,
    instructions=instructions,
    input=input,
)

# 結果を表示
print(response.output_text)
