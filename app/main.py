# main.py
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from pathlib import Path
import json

from license_mapper import map_requirements
from ai_client import generate_report  # the function that was built

app = FastAPI(title="Business Licensing AI")
from fastapi.middleware.cors import CORSMiddleware

# Solved CORS Problem using middleware in FastAPI 
# This allows calls from the frontend to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DATA_DIR = Path(__file__).parent / "data"

class BusinessIn(BaseModel):
    name: str | None = "עסק לדוגמה"
    area_sqm: float = 0
    seating: int = 0
    uses_gas: bool = False
    serves_meat: bool = False
    delivers: bool = False

@app.post("/api/generate-report")
def generate_report_endpoint(business: BusinessIn):
    biz = business.dict()
    # mapping requirements according to the logic
    mapped = map_requirements(biz)
    # Gemini model call for customized report 
    report_text = generate_report(biz, mapped)
    return {
        "business": biz,
        "mapped_requirements": mapped,
        "report": report_text
    }

@app.post("/api/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    #saving temporary file in data/raw and than runs the processing
    
    raw_dir = DATA_DIR / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / file.filename
    content = await file.read()
    path.write_bytes(content)
    return {"filename": str(path)}

@app.get("/api/mapped")
def get_mapped():
    mapped_path = DATA_DIR / "mapped_requirements.json"
    if mapped_path.exists():
        return json.loads(mapped_path.read_text(encoding="utf-8"))
    return {"mapped": []}
