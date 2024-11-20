# Structured Output Test
import os
import openai
from dotenv import load_dotenv
from openai import AzureOpenAI, AuthenticationError
from pydantic import BaseModel

load_dotenv()


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    # azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")
)

try:
    completion = client.beta.chat.completions.parse(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
        messages=[
            {"role": "system", "content": "Extract the event information."},
            {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
        ],
        response_format=CalendarEvent,
    )
    event = completion.choices[0].message.parsed
    print(event)
    print(completion.model_dump_json(indent=2))
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
