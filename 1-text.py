import openai

# Read API KEY
# Not needed if you set the OPENAI_API_KEY environment variable
import os
from dotenv import load_dotenv
load_dotenv()
api_key =  os.environ.get('OPENAI_API_KEY')
# End of Read API KEY

client = openai.OpenAI(api_key=api_key)

question = "What is the second smallest country in the world, in one word?"

response = client.responses.create(
    model="gpt-4o",
    input=question,
    previous_response_id="resp_6818979c889c81928e0311186646a3b50658a9767cc384c9"
)

print(response.id)
print(response.output_text)

