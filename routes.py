from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CodeInput(BaseModel):
    text: str

@router.post("/update-doc")
def update_doc(data: CodeInput):
    print("Received code:", data.text)
    return {"message": "Code received"}

# ✅ ADD THIS BELOW
class PasteData(BaseModel):
    text: str
    startLine: int
    endLine: int

@router.post("/paste-log")
def log_paste(data: PasteData):
    print(f"\nPaste detected from line {data.startLine} to {data.endLine}:")
    print(data.text)
    return {"message": "Paste logged"}
