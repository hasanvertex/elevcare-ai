import pandas as pd
import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

contracts = pd.read_csv(
    "database/contracts.csv"
)

maintenance = pd.read_csv(
    "database/maintenance.csv"
)

prompt = f"""
Contract Data:

{contracts.to_string()}

Maintenance Data:

{maintenance.to_string()}

Create a short management report for elevator maintenance.
"""

response = model.generate_content(
    prompt
)

print(response.text)