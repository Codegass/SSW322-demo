from openai import OpenAI


client = OpenAI(api_key="your-api-key")

completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
