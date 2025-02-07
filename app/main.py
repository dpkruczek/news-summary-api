from fastapi import FastAPI
from app.routes.summary import router as summary_router


app = FastAPI()

app.include_router(summary_router)