import os
import google.generativeai as genai
import time
genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))
model = genai.GenerativeModel('gemini-pro')

def gpt(prompt, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    time.sleep(0.5)
    return [model.generate_content(prompt).text]
