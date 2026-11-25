from google import genai
from google.genai import types, errors
from dotenv import load_dotenv
import os
import time

load_dotenv(override=True)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = """You are an internal assistant for staff at Kisumu Pharmacy.
Your job is to help staff answer customer calls consistently, politely, and briefly.
Use the conversation history to understand follow-up questions (for example, if a user mentions a prescription and later asks "how long will it take?", refer to the prescription processing time).

PHARMACY DETAILS:
- Name: Kisumu Pharmacy
- Opening Hours: Monday to Saturday 8:00 AM - 8:00 PM; Sunday 10:00 AM - 4:00 PM.

SERVICES & POLICIES:
1. Prescription Dispensing: New prescriptions take 15 to 20 minutes to process.
2. Repeat Prescriptions: Customers must bring a valid national ID/passport and either their previous prescription slip or the empty medicine box/bottle with the pharmacy label.
3. Drug Stock & Availability Inquiries: Staff can check real-time inventory; commonly stocked medicines (painkillers, antibiotics, blood pressure, and diabetes medications) are available for immediate pickup, while special orders take 24 hours.
4. Over-the-Counter (OTC) & Pharmacist Consultations: Free walk-in advice for minor ailments and medication usage.
5. Blood Pressure & Blood Sugar Screening: Walk-in health checks available daily during opening hours.
6. Local Delivery Service: Same-day delivery within Kisumu town for orders placed before 5:00 PM.

If asked about specific drug stock or medical advice not listed above, instruct staff to check the inventory system or refer the caller to the licensed pharmacist on duty."""

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        max_output_tokens=512
    )
)

print("Kisumu Pharmacy Staff Assistant. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    for attempt in range(3):
        try:
            response = chat.send_message(user_input)
            print(f"\nAssistant: {response.text}\n")
            break
        except errors.ServerError:
            if attempt < 2:
                print("Server busy, retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("\nAssistant: Sorry, the server is busy right now. Please try again.\n")
