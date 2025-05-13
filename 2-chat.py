import openai

client = openai.OpenAI()

system_message = {
    "role": "system",
    "content": "You're a helpful assistant who answers in minimal words."
}

user_message = {
    "role": "user",
    "content": "What is the third smallest country in the world."
}

messages = [system_message, 
            user_message]

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=messages
)
   
print(completion.choices[0].message.content)    

