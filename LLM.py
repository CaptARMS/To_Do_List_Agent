import os
from groq import Groq
from datetime import date
import re
client = Groq(
    api_key=os.environ.get("key"),
)

def askLLM(prompt,profession,extra=None):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a"+profession+" who is doing planning his to-do list"+str(extra)
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

def sugg_option(profession):
    options = "\"Add a new task\", \"Delete an existing task\", \"Edit a task\", \"Mark a task as Done\", \"Change the name of the task\""
    prompt_for_options="Output one of the following options"+options+"Only Output exactly one of the above options: Example: Add a new task"
    return askLLM(prompt_for_options,profession)

def sugg_task(profession):
    prompt_for_name="Give a random task with following attributes: Name of the task.Only Output in the following format: \"Name\". Dont return anything else, just return the string \"Name\"." 
    name=askLLM(prompt_for_name,profession)
    prompt_for_deadline="Current Date :"+str(date.today())+"You have to give a deadline for the task: "+name+". Give the average time it would take to complete the task:"+name+"The deadline should not be beyond 1 month from current date. You must output only \"DD=MM-YYYY HH:MM\". Do NOT return anything else"
    extra="You answer only in the following format: %d-%m-%Y %H:%M"
    deadline=askLLM(prompt_for_deadline,profession,extra)
    return name,deadline
# Name=askLLM(prompt_for_options)
# Deadline=askLLM(prompt_for_deadline)
# Deadline.strip().strip('"')
# print(Deadline)
# print(sugg_task('barista'))