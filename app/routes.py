# app/routes.py
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from app.utils import limiter
from app.services import jd

router = APIRouter()

# Data Models...
class JDRequest(BaseModel):
    jd_text: str
    
## API endpoints -->>
# Test API-Health...
@router.get("/")
async def root():
    return JSONResponse(
        status_code=200,
        content={"success": True, "msg": "Hackathon backend is running at `http://localhost:8080/` 🚀!"}
    )

@router.post("/jd-skills")
# @limiter.limit("30/minute")  # 30-req's/min per IP...
async def jd_to_learning_path(payload: JDRequest):
    
    # Sample JD -> "We are hiring a React developer with experience in Node.js, MongoDB, and Docker. Knowledge of Git and CI/CD is a plus."
    extracted_skills = jd.extract_skills_from_jd(payload.jd_text)
    ordered_skills = jd.reorder_skills(extracted_skills)
    learning_path = jd.generate_learning_path(ordered_skills)

    return {
        "success": True,
        "msg": "Learning-Path generated from JD!",
        "jd_text": payload.jd_text,
        "skills_extracted": ordered_skills,
        "learning_path": learning_path,
        "modules_found": len(learning_path),
    }
