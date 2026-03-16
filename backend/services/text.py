from services.falcon import generate_falcon_text
from services.gemini import generate_gemini_text

async def generate_text(prompt: str, model_choice: str) -> dict:
    if model_choice == "Falcon 7B" or model_choice == "Falcon":
        response_text = await generate_falcon_text(prompt)
    else:
        response_text = await generate_gemini_text(prompt)
        
    return {
        "text_explanation": response_text,
        "media_type": "Text"
    }