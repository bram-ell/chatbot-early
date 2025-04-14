from google import generativeai as genai

# Set your Gemini API key
genai.configure(api_key="AIzaSyAger0xg4PGTb33PGwor-4SXntEeYsQJO0")
model = genai.GenerativeModel("gemini-2.0-flash")

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Explain how AI works",
# )

# print(response.text)
