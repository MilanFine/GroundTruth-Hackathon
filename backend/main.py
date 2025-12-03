from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import creative
import uvicorn
import os

app = FastAPI(title="Auto-Creative Engine API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(creative.router)

@app.get("/")
async def root():
    return {"message": "Auto-Creative Engine API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
