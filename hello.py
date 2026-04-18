import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()  # ANTHROPIC_API_KEY 환경변수 자동 로드

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=512,
    messages=[
        {
            "role": "user",
            "content": "토큰(token)이 뭔지 한 문장으로 설명해줘."
        }
    ]
)

print(message.content[0].text)