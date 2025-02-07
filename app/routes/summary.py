from app.routes.auth import validate_api_key
from app.models import Article
from fastapi import APIRouter, Depends, HTTPException
from langchain_community.llms import Ollama, OpenAI
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


router = APIRouter(prefix="/summary", dependencies=[Depends(validate_api_key)])

llm = Ollama(
    model="llama3.2", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)
instructions = ("Please summarize the following article in exactly two sentences and nothing else: ")

@router.post("/")
def summarize(article: Article):
    if (len(article.article) < 50):
        raise HTTPException(status_code=400, detail="Article too short for summarization")

    summary = llm.invoke(instructions + article.article)

    return summary