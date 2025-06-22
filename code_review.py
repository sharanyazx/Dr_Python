import subprocess
import google.generativeai as genai


def analyze_code_quality(file_path):
    result = subprocess.run(["pylint", file_path], stdout=subprocess.PIPE, text=True)
    return result.stdout


def ai_code_suggestions(code):
    # Configure Gemini API
    genai.configure(api_key="you api key")  # Replace with your actual API key

    # Load the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"You are an expert Python code reviewer. Review and suggest improvements for the following code:\n\n{code}"

    response = model.generate_content(prompt)

    return response.text
