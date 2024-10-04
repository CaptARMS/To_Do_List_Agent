import os
from groq import Groq
client = Groq(
    api_key=os.environ.get("key"),
)

prompt="Current Date=04-10-2024.Give a random task with following attributes: Name of the task, Deadline for the task. The deadline of the task cannot be beyond 1 month from the current date and time.Only Output in the following format: Name,Deadline(Date,Time). Dont return anything else, just return the tuple." 

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion[0].message.content.first)
# print(chat_completion.choices[0].message.content)