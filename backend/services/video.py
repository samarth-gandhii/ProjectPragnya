from services.gemini import generate_gemini_video

async def generate_video(blueprint: str) -> dict:
    # Your gemini function already returns both the text and the mock URL!
    text_explanation, video_url = await generate_gemini_video(blueprint)
    
    return {
        "text_explanation": text_explanation,
        "video_url": video_url,
        "media_type": "Video"
    }