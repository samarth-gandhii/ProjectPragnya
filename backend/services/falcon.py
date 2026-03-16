from langchain_core.prompts import PromptTemplate
from services.llm_client import falcon_llm

# ---------------------------------------------------------
# 1. TEXT ROUTE (Markdown & Flowcharts)
# ---------------------------------------------------------
async def generate_falcon_text(prompt: str) -> str:
    """Handles standard text explanations locally."""
    template = """You are an AI tutor specializing in Data Science and Data Analytics. 
    Explain the following concept clearly and concisely: {concept}
    
    CRITICAL INSTRUCTIONS:
    - Use Markdown formatting extensively (Headings, bullet points, bolding).
    """
    prompt_template = PromptTemplate(template=template, input_variables=["concept"])
    
    chain = prompt_template | falcon_llm
    
    response = await chain.ainvoke({"concept": prompt})
    return response if isinstance(response, str) else getattr(response, "content", str(response))

# ---------------------------------------------------------
# 2. PIPELINE ROUTE (Prompt Engineering for Gemini)
# ---------------------------------------------------------
async def expand_prompt(prompt: str, context_type: str) -> str:
    """Acts as the Prompt Engineer for Gemini. Expands a short user query into a detailed architectural blueprint."""
    template = """You are an expert prompt engineer and data scientist. The user wants a {context_type} representing this concept: '{prompt}'.
    Write a highly detailed, professional prompt that will be sent to a specialist AI to build this {context_type}.
    Include required visual details, structural instructions, coordinate mapping, and core logic to represent the data science concept accurately.
    Output ONLY the expanded prompt, without introductory text."""
    
    prompt_template = PromptTemplate(template=template, input_variables=["prompt", "context_type"])
    
    chain = prompt_template | falcon_llm
    response = await chain.ainvoke({"prompt": prompt, "context_type": context_type})
    
    return response if isinstance(response, str) else getattr(response, "content", str(response))