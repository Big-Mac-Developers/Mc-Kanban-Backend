import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "summarise this\n"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "I apologize, but you haven't provided any text or information for me to summarize. Could you please provide the text or article that you would like me to summarize? Once you do that, I'll be happy to help you with a concise summary."
                }
            ]
        }
    ]
)
print(message.content)