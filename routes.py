from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CodeInput(BaseModel):
    text: str

@router.post("/update-doc")
def update_doc(data: CodeInput):
    print("Received code:", data.text)
    return {"message": "Code received"}

class PasteData(BaseModel):
    text: str
    startLine: int
    endLine: int
    source: str

@router.post("/paste-log")
def log_paste(data: PasteData):
    print(f"\nPaste detected from line {data.startLine} to {data.endLine}:")
    print(f"Copied Code:\n{data.text}")
    print(f"Source: {data.source}")
    return {"message": "Paste logged"}
