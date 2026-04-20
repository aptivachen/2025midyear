import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    messages=[{"role": "user", "content": "hi"}],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
