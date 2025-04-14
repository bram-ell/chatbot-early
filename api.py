
from fastapi import APIRouter
from model import Message
from gemini_config import model

router = APIRouter()

@router.post("/chat")
async def chat(msg: Message):
    response = model.generate_content(msg.message)
    return {"reply": response.text}


# # Define a POST route for the chatbot
# # Clients will send POST requests to /chat with a JSON message
# @app.post("/chat")
# async def chat(msg: Message):
#     # Use the Gemini model to generate a response based on the input message
#     response = model.generate_content(msg.message)
    
#     # Return the model's response as a JSON object
#     return {"reply": response.text}

