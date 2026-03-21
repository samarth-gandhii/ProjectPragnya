from services.gemini import generate_gemini_quiz
import json

async def generate_quiz(blueprint: str, history: list) -> dict:
    raw_response = await generate_gemini_quiz(blueprint, history)
    
    # Clean up the response in case Gemini wrapped it in markdown
    cleaned_json = raw_response.replace("```json", "").replace("```", "").strip()
    
    try:
        quiz_data = json.loads(cleaned_json)
    except Exception:
        # Fallback if the AI messes up the JSON formatting
        quiz_data = [{"question": "Error generating quiz format.", "options": ["A"], "answer": "A"}]
    
    return {
        "text_explanation": "I've prepared a quick quiz to test your understanding of the topic!",
        "quiz_data": quiz_data,
        "media_type": "Quiz"
    }