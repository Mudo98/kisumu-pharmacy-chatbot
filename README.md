# Kisumu Pharmacy Staff Assistant (`Kisumubot.py`)

A command-line AI chatbot built with Python and the Google GenAI SDK (`gemini-3.5-flash-lite`) to help staff at **Kisumu Pharmacy** answer customer phone inquiries consistently and accurately.

## Features
- **Consistent Pharmacy Info:** Configured via system prompt with Kisumu Pharmacy's opening hours (**Mon–Sat: 8:00 AM – 8:00 PM**, **Sun: 10:00 AM – 4:00 PM**) and core services.
- **Multi-Turn Conversation Memory:** Remembers context across follow-up questions (e.g., knowing *"How long will it take?"* refers to a prescription mentioned earlier in the chat).
- **Resilient Error Handling:** Includes automatic retry logic for temporary API server spikes.

## Pharmacy Services Covered
1. **Prescription Dispensing:** Processing times (15–20 minutes for new prescriptions).
2. **Repeat Prescriptions:** Required documentation (valid national ID/passport plus previous prescription slip or labeled medicine packaging).
3. **Drug Stock & Availability Inquiries:** Immediate pickup vs. 24-hour special orders.
4. **Over-the-Counter (OTC) & Pharmacist Consultations:** Free walk-in advice.
5. **Blood Pressure & Blood Sugar Screening:** Daily walk-in health checks.
6. **Local Delivery Service:** Same-day delivery within Kisumu town for orders placed before 5:00 PM.

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install google-genai python-dotenv
   ```

3. **Set up your API key**
   Create a `.env` file in the project folder and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

Run the assistant in your terminal:
```bash
python Kisumubot.py
```
Type `exit` to end the session.
