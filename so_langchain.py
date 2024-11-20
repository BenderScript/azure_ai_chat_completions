import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


messages = [
    SystemMessage("Extract the event information."),
    HumanMessage("Alice and Bob are going to a science fair on Friday.")
]

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)


llm_with_structure = llm.with_structured_output(schema=CalendarEvent, method="json_schema")
llm_response = llm_with_structure.invoke(messages)
print(llm_response.model_dump_json())  # type: ignore
