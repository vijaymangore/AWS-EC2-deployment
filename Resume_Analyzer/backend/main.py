from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "api running"}

# Changed from @app.get to @app.post to match your frontend requests.post
@app.post("/analyze")
async def analyze(data: dict):
    text = data.get("text", "")
    
    # Added () to text.split() to properly split the text into a list of words
    words = len(text.split()) 
    
    return {"word_count": words}