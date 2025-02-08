from app.config import MAX_ARTICLE_CHAR_LENGTH, LLM_MODEL
import pytest
from fastapi import HTTPException
from app.routes.summary import SummaryService
from app.models import Article

@pytest.fixture
def summary_service():
    return SummaryService(LLM_MODEL)
        
def test_generate_summary_too_short():
    service = SummaryService(LLM_MODEL)
    article = Article(article="Too short")
    
    with pytest.raises(HTTPException) as exc_info:
        service.generate_summary(article)
    
    assert exc_info.value.status_code == 400
    assert "too short" in exc_info.value.detail.lower()

def test_generate_summary_too_long(summary_service):
    long_article = Article(article="x" * (MAX_ARTICLE_CHAR_LENGTH + 1))
    
    with pytest.raises(HTTPException) as exc_info:
        summary_service.generate_summary(long_article)
    
    assert exc_info.value.status_code == 400
    assert "too long" in exc_info.value.detail.lower()
