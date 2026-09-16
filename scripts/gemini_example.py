"""Minimal example: call the Google AI Studio (Gemini) API using a key from the environment.

Setup:
  1. Copy .env.example to .env
  2. Put your real key in .env as GOOGLE_API_KEY=...
  3. pip install google-generativeai python-dotenv
  4. python scripts/gemini_example.py "your prompt here"
"""

import os
import sys

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise SystemExit("GOOGLE_API_KEY is not set. Add it to your .env file (see .env.example).")

genai.configure(api_key=api_key)

prompt = " ".join(sys.argv[1:]) or "Say hello in one sentence."
model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content(prompt)
print(response.text)
