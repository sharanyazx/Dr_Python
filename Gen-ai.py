#for checking the list of models available in Google Generative AI
import google.generativeai as genai


genai.configure (api_key="Your Api") 

for model in genai.list_models():
    print(model.name)
