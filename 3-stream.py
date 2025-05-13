from openai import OpenAI

client = OpenAI()

stream = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": "Write a short essay about the second smallest country in the world.",
        },
    ],
    stream=True,
)

for event in stream:
    # Check if the event has a 'delta' attribute
    if hasattr(event, 'delta'):
        print(event.delta, end="", flush=True)
        # print(event)