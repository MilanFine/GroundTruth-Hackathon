from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from typing import List
import uuid
from services.ai_service import ai_service
from services.image_processor import image_processor

router = APIRouter(prefix="/creative", tags=["creative"])

# In-memory storage for demo purposes
# In production, use a database and object storage (S3)
tasks = {}

@router.post("/generate")
async def generate_creatives(
    logo: UploadFile = File(...),
    product_image: UploadFile = File(...),
    product_description: str = Form(...)
):
    task_id = str(uuid.uuid4())
    
    # Read files
    logo_content = await logo.read()
    product_image_content = await product_image.read()
    
    # 1. Generate copy
    captions = await ai_service.generate_ad_copy(product_description)
    
    # 2. Generate images
    # In a real app, we might pass the processed image to the AI service as a reference
    # processed_img = image_processor.process_assets(logo_content, product_image_content)
    
    images = []
    for i in range(10): # Generate 10 variations as requested
        img_url = await ai_service.generate_image_variation(product_description)
        images.append(img_url)
        
    # Store results
    tasks[task_id] = {
        "captions": captions,
        "images": images
    }
        
    return {
        "status": "success",
        "task_id": task_id,
        "captions": captions,
        "images": images
    }

@router.get("/download/{task_id}")
async def download_results(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
        
    task_data = tasks[task_id]
    zip_buffer = image_processor.create_zip_archive(task_data["images"], task_data["captions"])
    
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename=creative_assets_{task_id}.zip"}
    )
