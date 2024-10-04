import os
from groq import Groq
client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)