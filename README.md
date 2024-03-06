# Quickstart
Source and attribution: https://sparkapps.net/building-a-gemini-pro-chatbot-with-googles-latest-model/<br>
Source and attribution: Heiko Hotz https://github.com/marshmellow77/vertex-gemini/blob/main/chatbot-gemini.py

# Using Gemini Pro via Google's Vertex APIs. 
## Assumptions:
a\ you have gcloud utilities installed (https://cloud.google.com/sdk/docs/install-sdk)<br>
b\ you have a GCP account for authentication.<br>
Note: the content of this repo has been tested on a MacOS Ventura using venv. 

## Instructions:
- Create virtual environment: `python3 -m venv .venv`<br>
- Activate virutal environment: `source .venv/bin/activate`<br>
- Install required packages: `pip3 install -r requirements.txt`<br>

- Set your Google project that allows access to Gemini models: `gcloud config set project cloud-llm-preview1`<br>
  >For more info:  https://developers.google.com/workspace/guides/create-project<br>

- Authenticate with application defaults: `gcloud auth application-default login`<br>
  >For more info: https://cloud.google.com/docs/authentication/provide-credentials-adc#local-user-cred)<br>

- To run the app use `streamlit run chatbot-gemini.py`

![Chatbot](images/chatbot-gemini.png)
