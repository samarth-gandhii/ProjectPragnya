from services.gemini import generate_gemini_3d

async def generate_3d(blueprint: str) -> dict:
    # Your gemini function already returns both the text and the code!
    text_explanation, canvas_code = await generate_gemini_3d(blueprint)
    
    return {
        "text_explanation": text_explanation,
        "canvas_code": canvas_code,
        "media_type": "3D_simulation"
    }