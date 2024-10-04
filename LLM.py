import os
from groq import Groq
client = Groq(
    api_key=os.environ.get("key"),
)

options = "\"Add a new task\", \"Delete an existing task\", \"Edit a task\", \"Mark a task as Done\", \"Change the name of the task\""
prompt_for_options="Output one of the following options"+options+"Only Output exactly one of the above options: Example: Add a new task"
prompt_for_name="Current Date=04-10-2024.Give a random task with following attributes: Name of the task.Only Output in the following format: \"Name\". Dont return anything else, just return the string \"Name\"." 
prompt_for_deadline="Current Date=04-10-2024. Give a random deadline for a task. The deadline should not be beyond 1 month from current time. Output in the format: DD-MM-YYYY HH:MM  Dont return anything else, just return the string:  \"DD=MM-YYYY HH:MM\""
def askLLM(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a to-do list planning agent."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    reply=chat_completion.choices[0].message.content
    return reply
# Name=askLLM(prompt_for_options)
Deadline=askLLM(prompt_for_deadline)
# Deadline.strip().strip('"')
# print(Deadline)
# print(Name)