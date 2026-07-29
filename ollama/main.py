from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import ollama

app = FastAPI()

@app.get("/ask", response_class=PlainTextResponse)
def ask(question: str = Query(...)):
    response = ollama.generate(
        model="phi3",  
        prompt=question
    )

    return response["response"]