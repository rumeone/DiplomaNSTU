from openai import OpenAI

client = OpenAI(
    api_key="sk-mTk0RYw5fkeWo1Y8k_bc1nWMQueTpE86",
    base_url="https://routerai.ru/api/v1"
)

response = client.chat.completions.create(
    model="deepseek/deepseek-v3.2",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
