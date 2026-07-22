from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

tasks = [
    {"id": 1, "title": "Finish Stage 2", "done": False},
    {"id": 2, "title": "Test the API", "done": False},
    {"id": 3, "title": "Push changes to GitHub", "done": True},
]


@app.get("/")
async def root():
    return {"name": "Task API", 
            "version": "1.0", 
            "endpoints": ["/tasks"], 
            }
    

@app.get("/health")
async def health_check():
        return {"status": "healthy"}
    
@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    
    return JSONResponse(
        status_code=404,
        content={"error": f"Task {task_id} not found"},
    )
    