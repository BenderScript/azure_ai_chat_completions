import requests

from dotenv import dotenv_values

# Get API key from .env file and store in dict for easy debugging and use
# Alternatively you can use load_dotenv() and then use os.getenv()
dotenv_file = "./.azure.env"
config = dotenv_values(dotenv_path=dotenv_file)

openai_api_key = config["OPENAI_API_KEY"]
openai_api_base = config["OPENAI_API_BASE"]
openai_api_version = config["OPENAI_API_VERSION"]
openai_api_type = config["OPENAI_API_TYPE"]
openai_api_model_name = config["OPENAI_API_MODEL_NAME"]
deployment_name = config["OPENAI_API_DEPLOYMENT_ID"]
model_name = config["OPENAI_API_EMBEDDING_MODEL_NAME"]
temperature = config["OPENAI_API_TEMPERATURE"]

# Debug prints
print(f"openai_api_base: {openai_api_base}")
print(f"openai_api_version: {openai_api_version}")
print(f"openai_api_type: {openai_api_type}")
print(f"deployment_name: {deployment_name}")
print(f"model_name: {model_name}")
print(f"temperature: {temperature}")

# Define the headers. Notice the difference between OpenAI's original API
headers = {
    "api-key": f"{openai_api_key}",
    "Content-Type": "application/json"
}

# Define the payload (your prompt and other settings)
payload = {
    "messages": [{"role": "user", "content": "Translate the following English text to French: 'Hello, World!'"}],
    "max_tokens": 8000,
    "model": f"{openai_api_model_name}",
    "temperature": float(f"{temperature}")
}

# Make the API request
url = openai_api_base + "openai/deployments/" + deployment_name + "/chat/completions?api-version=" + openai_api_version
print(f"url: {url}")
response = requests.post(url, headers=headers, json=payload)

# Parse the response, notice that completions have a "role"
if response.status_code == 200:
    full_response = response.json()
    print(f"Completion: {full_response['choices'][0]['message']}")
else:
    print(f"Error: {response.status_code}, {response.text}")
