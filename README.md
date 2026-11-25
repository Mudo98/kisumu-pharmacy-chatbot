# Nairobi Real Estate Inquiry Extractor

A Python script that uses Google's Gemini API (`gemini-3.8-flash`) to parse unstructured client messages into clean, structured JSON dictionaries for a Nairobi real estate agency.

## What the Script Extracts & Why Each Field Matters

The script extracts five core fields from incoming customer inquiries, assigning `null` (`None` in Python) when a detail is omitted:

| Field | Example Output | Why It Matters |
| :--- | :--- | :--- |
| **`property_type`** | `"house"`, `"bedsitter"`, `"plot or townhouse"` | Allows agents to immediately filter available inventory by structure category rather than manually reading every inquiry. |
| **`bedrooms`** | `3`, `0`, `null` | Essential for matching family size and layout requirements; automatically normalizes local terms like `"bedsitter"` to `0`. |
| **`location`** | `"Kileleshwa"`, `"Westlands"`, `"Syokimau"` | Enables territory-based routing so leads go directly to the agent covering that specific Nairobi neighborhood or suburb. |
| **`budget_kes`** | `80000`, `20000`, `null` | Converts shorthand text (e.g., `"80k"`, `"15M"`) into pure integers in Kenyan Shillings (KES) so leads can be sorted or filtered numerically in spreadsheets and databases. |
| **`rental_or_sale`** | `"rental"`, `"sale"` | Separates short-term leasing inquiries from long-term property purchase leads, which require different workflows, contracts, and agents. |

## Setup & Usage

1. **Install dependencies:**
   ```bash
   pip install google-genai python-dotenv
   ```

2. **Configure your API key:**
   Create a `.env` file in the root directory and add your Google AI Studio key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Run the script:**
   ```bash
   python day12.py
   ```
