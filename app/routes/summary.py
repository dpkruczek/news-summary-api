from auth import validate_api_key
from models import Article
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/summary", dependencies=[Depends(validate_api_key)])

@router.post("/")
def summarize(article: Article):
    if (len(article.article) < 50):
        raise HTTPException(status_code=400, detail="Article too short for summarization")

    # TODO: Call AI summarization model
    summary = "This is a summary"
    
    return summary