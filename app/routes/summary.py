from app.routes.auth import validate_api_key
from app.models import Article
from fastapi import APIRouter, Depends, HTTPException
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from app.config import LLM_MODEL, MAX_ARTICLE_CHAR_LENGTH


router = APIRouter(prefix="/summary", dependencies=[Depends(validate_api_key)])

class SummaryService:
    def __init__(self, model: str):
        self.llm = Ollama(
            model=model,
            temperature=0.5,
            callbacks=[StreamingStdOutCallbackHandler()]
        )
    
    def generate_summary(self, article: Article) -> str:
        if (len(article.article) < 50):
            raise HTTPException(status_code=400, detail="Article too short for summarization")
        
        if (len(article.article) > MAX_ARTICLE_CHAR_LENGTH):
            raise HTTPException(status_code=400, detail="Article too long for summarization")
        
        # TODO: Prevent jailbreaking

        instructions = "Please summarize the following article in exactly two sentences. Don't write anything else than the summary, such as 'Here is the summary of the article: '"            
        return self.llm.invoke(instructions + article.article)

# Initialize the service
summary_service = SummaryService(LLM_MODEL)

@router.post("/")
def summarize(article: Article):
    summary = summary_service.generate_summary(article)
    return {"summary": summary}