# news-summary-api

## Getting Started

### Prerequisites

- Python 3.10 or higher.
- Ollama installed.

### Run locally

1. Create a virtual environment by running `python -m venv venv`.
2. Activate the virtual environment by running `source venv/bin/activate`.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Create a `.env` file based on the `.env.example` file.
5. (Optional) Change the model in `app/config.py`.
6. Run the application by running `python -m uvicorn main:app --reload`.

### Run tests

```bash
pytest
```

### API Documentation

The API documentation is available at `http://localhost:8000/docs` after running the application.
