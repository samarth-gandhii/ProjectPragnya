from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router

app = FastAPI(title="AnubhavAI Backend Engine")

# Development CORS policy: allow all origins for browser preflight reliability.
# Do not use this as-is for production deployments.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API endpoints from routes.py
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"status": "AnubhavAI Engine is running."}