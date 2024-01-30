# Minimalistic Azure AI Chat Completion 

## Overview
This is a simple Python application that uses the Azure OpenAI AI API to generate chat completions. 

## Prerequisites
- Python 3.11 or higher
- `openai` library
- `python-dotenv` library

## Setup
1. Clone the repository.
2. Install the required Python libraries using pip:
    ```
    pip3 install -r requirements.txt
    ```
3. Create a `.env` file in the root directory of the project and add your Azure AI API credentials and settings:
    ```
   AZURE_OPENAI_API_KEY=your-key
   AZURE_MODEL_NAME=gpt-4
   AZURE_OPENAI_ENDPOINT=your URL endpoint
   AZURE_OPENAI_API_VERSION=<such as 2023-12-01-preview>
   AZURE_OPENAI_DEPLOYMENT=<your deployment name>
    ```

## Usage
Run the script using Python:
```
python main.py
```
The script will load the settings from the `.env` file, make a chat completion request to the Azure OpenAI deployment you specified


If you are working with pure REST the full URL will look like:

```bash
url = openai_api_base + "openai/deployments/" + deployment_name + "/chat/completions?api-version=" + openai_api_version
```

## Customization
You can customize the script by modifying the `messages` dictionary. 
## Troubleshooting
If you encounter any errors, check the printed error message and status code for clues about what went wrong. Common issues include incorrect API credentials in the `.env` file and network connectivity problems.

## Contributing
Contributions are welcome! Please read our contributing guidelines before submitting a pull request.
