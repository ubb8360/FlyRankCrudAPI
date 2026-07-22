from fastapi import FastAPI

app = FastAPI()


@app.get("/tasks")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"], }

@app.get("/health")
async def health_check():
        return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    