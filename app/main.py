from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
from .extractor import extract_job
from .comparison import run_comparison

app = FastAPI(title="Job Listing Extractor")

class ExtractRequest(BaseModel):
    text: str
    model: str = "gemini-2.5-flash-lite"

class CompareRequest(BaseModel):
    text: str
    
@app.get("/")
async def index():
    ui_path = Path(__file__).parent.parent / "ui" / "index.html"
    return FileResponse(ui_path)

@app.post("/extract")
async def extract(req: ExtractRequest):
    try:
        return extract_job(req.text, req.model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/compare")
async def compare(req: CompareRequest):
    return run_comparison(req.text)