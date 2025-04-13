
from fastapi import FastAPI, Request
from pydantic import BaseModel  # Used for request data validation
from google import generativeai as genai  # Google Gemini API

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyDT9PTn9UJ1-bfwVTkpjSBocEhsMyTw82g")

# Initialize the FastAPI application
app = FastAPI()

# Create an instance of the Gemini model (you can change model name if needed)
model = genai.GenerativeModel("gemini-2.0-flash")

# Define a data model for the request body
# When a client sends {"message": "Hello"}, it will match this structure
class Message(BaseModel):
    message: str

# Define a POST route for the chatbot
# Clients will send POST requests to /chat with a JSON message
@app.post("/chat")
async def chat(msg: Message):
    # Use the Gemini model to generate a response based on the input message
    response = model.generate_content(msg.message)
    
    # Return the model's response as a JSON object
    return {"reply": response.text}

