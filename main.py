import os
import openai
from dotenv import load_dotenv
from openai import AzureOpenAI, AuthenticationError

load_dotenv()


# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
    # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

try:

    completion = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
        messages=[
            {
                "role": "user",
                "content": "How do I output all files in a directory using Python?",
            },
        ],
    )
    print(completion.choices[0].message.content)
except AuthenticationError as e:
    print(e)
    print(e.status_code)
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
    print(e.status_code)
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
except Exception as e:
    print(e)
