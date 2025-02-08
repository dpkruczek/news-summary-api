import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
API_KEY = os.getenv("API_KEY")

# LLM settings
LLM_MODEL = "llama3.2"
MAX_ARTICLE_CHAR_LENGTH = 100000   #llama3.2 context window is 128k tokens
