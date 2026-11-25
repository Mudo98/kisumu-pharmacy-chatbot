import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load GEMINI_API_KEY from your .env file
load_dotenv()

# Initialize the Gemini client
client = genai.Client()

system_prompt = """You are a data extraction assistant for a real estate agent in Nairobi.
Extract property inquiry details from the user's message and return ONLY a valid JSON object.

Rules:
- Do not include markdown formatting (like ```json), explanations, or extra text.
- Use these exact keys: "property_type", "bedrooms", "location", "budget_kes", "rental_or_sale".
- Convert shorthand budgets into full numbers in KES (e.g., "80k" becomes 80000, "15M" becomes 15000000).
- For "rental_or_sale", infer from context (e.g., "per month" = "rental", "buying" = "sale") or use null if unclear.
- If a field is missing from the message, set its value to null.
"""

import time
from google.genai.errors import ServerError

def extract_inquiry(message_text):
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=message_text,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    response_mime_type="application/json"
                )
            )
            return json.loads(response.text)
        except ServerError:
            print(f"Server busy, retrying in 5 seconds... (Attempt {attempt + 1}/5)")
            time.sleep(5)
    raise Exception("Server remained busy after 5 attempts.")
    
    # Parse the JSON string into a Python dictionary
    data = json.loads(response.text)
    return data

# Test cases (including one with missing information)
test_inquiries = [
    "I am looking for a 3-bedroom house in Kileleshwa, budget around 80k per month",
    "Do you have any bedsitters near Westlands under 20k?",
    "Hi, I want to buy a plot or townhouse in Syokimau."
]

# Run the tests and print cleanly
for i, inquiry in enumerate(test_inquiries, start=1):
    print(f"--- Inquiry {i} ---")
    print(f"Original: {inquiry}")
    
    extracted_data = extract_inquiry(inquiry)
    
    print("Extracted Details:")
    for key, value in extracted_data.items():
        print(f"  {key}: {value}")
    print()
