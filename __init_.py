# Install OpenAI SDK "pip3 install openai"

from openai import openAI

# Invoke client API

client = OpenAI(api_key="< INSERT KEY HERE>", base_url="https://apei.deepseek.com")


# Prompts response from API 

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)