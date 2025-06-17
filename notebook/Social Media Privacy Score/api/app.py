from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class Post(BaseModel):
    text: str

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("your-hf-model-repo")
model = AutoModelForSequenceClassification.from_pretrained("your-hf-model-repo")

@app.post("/score")
async def score(post: Post):
    inputs = tokenizer(post.text, return_tensors="pt", truncation=True)
    logits = model(**inputs).logits
    score = torch.sigmoid(logits).item() * 100
    return {"risk_score": round(score, 2)}

@app.post("/rewrite")
async def rewrite(post: Post):
    # (Optional) Use a seq2seq model or prompt-based LLM to rewrite
    return {"rewritten": "More privacy-safe version"}
