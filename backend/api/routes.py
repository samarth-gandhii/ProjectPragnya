from fastapi import APIRouter
from schemas.models import GenerateRequest # Assuming your Pydantic models are here
from services.text import generate_text
from services.threed import generate_3d
from services.quiz import generate_quiz
from services.video import generate_video
from services.falcon import expand_prompt 

router = APIRouter()

@router.post("/generate")
async def generate_content(request: GenerateRequest):
    
    # ---------------------------------------------------------
    # ROUTE 1: SIMPLE TEXT (Fast, Direct)
    # ---------------------------------------------------------
    if request.context_type == "Text" or not request.context_type:
        return await generate_text(request.prompt, request.model_choice)

    # ---------------------------------------------------------
    # ROUTE 2: COMPLEX MEDIA GENERATION (The Falcon -> Gemini Pipeline)
    # ---------------------------------------------------------
    else:
        # Step 1: Falcon acts as the Prompt Engineer
        detailed_blueprint = await expand_prompt(request.prompt, request.context_type)
        
        # Step 2: Gemini executes the complex blueprint
        if request.context_type == "3D_simulation":
            return await generate_3d(detailed_blueprint)
            
        elif request.context_type == "Quiz":
            return await generate_quiz(detailed_blueprint)
            
        elif request.context_type == "Video":
            return await generate_video(detailed_blueprint)
            
        return {"error": "Invalid context type"}