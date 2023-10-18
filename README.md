# Azure AI Chat Completion Script README

## Overview
This script is a Python application that uses the Azure AI API to generate chat completions. It's a simple example designed to translate English text to French, but can be easily modified for other tasks.

## Prerequisites
- Python 3.6 or higher
- `requests` library
- `python-dotenv` library

## Setup
1. Clone the repository.
2. Install the required Python libraries using pip:
    ```
    pip install requests python-dotenv
    ```
3. Create a `azure.env` file in the root directory of the project and add your Azure AI API credentials and settings:
    ```
    OPENAI_API_KEY=<your-api-key>
    OPENAI_API_BASE=<api-base-url>
    OPENAI_API_VERSION=<api-version>
    OPENAI_API_TYPE=<api-type>
    OPENAI_API_MODEL_NAME=<model-name>
    OPENAI_API_DEPLOYMENT_ID=<deployment-id>
    OPENAI_API_EMBEDDING_MODEL_NAME=<embedding-model-name>
    OPENAI_API_TEMPERATURE=<temperature>
    ```

4. `.azure.env` example

   ```
   OPENAI_API_KEY=<your api key>
   OPENAI_API_TYPE=azure
   OPENAI_API_BASE=<your azure ai url base>
   OPENAI_API_DEPLOYMENT_ID=<your deployment id, some people call it deployment name>
   OPENAI_API_VERSION=2023-05-15
   OPENAI_API_REGION=<optional>
   OPENAI_API_MAX_TOKENS=8192
   OPENAI_API_TEMPERATURE=0.1
   OPENAI_API_MODEL_NAME=gpt-4
   ```

## Usage
Run the script using Python:
```
python script.py
```
The script will load the settings from the `.azure.env` file, make a POST request to the Azure AI API with a payload containing your prompt and settings, and print the completion result.



The Azure AI full URL will look like:

```bash
url = openai_api_base + "openai/deployments/" + deployment_name + "/chat/completions?api-version=" + openai_api_version
```

## Customization
You can customize the script by modifying the `payload` dictionary. For example, you can change the `content` field in the `messages` list to use a different prompt, or adjust the `max_tokens` field to generate longer or shorter completions.

## Troubleshooting
If you encounter any errors, check the printed error message and status code for clues about what went wrong. Common issues include incorrect API credentials in the `.env` file and network connectivity problems.

## Contributing
Contributions are welcome! Please read our contributing guidelines before submitting a pull request.

## License
This project is licensed under the terms of the MIT license.