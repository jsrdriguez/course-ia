from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production!"

# This is important for Vercel
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)