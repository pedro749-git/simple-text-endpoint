from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextRequest(BaseModel):
    text: str


class TextResponse(BaseModel):
    original: str
    uppercase: str
    char_count: int


@app.post("/text", response_model=TextResponse)
def process_text(body: TextRequest):
    return TextResponse(
        original=body.text,
        uppercase=body.text.upper(),
        char_count=len(body.text),
    )
