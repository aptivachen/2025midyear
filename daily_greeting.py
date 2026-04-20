#!/usr/bin/env python3
import anthropic
from datetime import datetime

def send_daily_greeting():
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=100,
        messages=[
            {"role": "user", "content": "Say 'hi' in a friendly and brief way"}
        ]
    )

    response = message.content[0].text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Daily Greeting: {response}")
    return response

if __name__ == "__main__":
    send_daily_greeting()
