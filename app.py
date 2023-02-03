from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []

@app.get("/todos")
async def get_all_todos():
  return fake_database

@app.post("/todos")
async def create_todo(request: Request):
    todo = await request.json()
    fake_database.append(todo)
    return todo

@app.patch("/todos/{id}")
async def update_todo_by_id(request: Request, id:int):
    task = await request.json()
    for z in fake_database:
        if z['id'] == id:
            z.update(task)
            return z,200 
    return None,404




