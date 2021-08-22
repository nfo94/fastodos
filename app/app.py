from fastapi import FastAPI
from .models import Todo
from .repository import todos_list, todo_create, todo_read, todo_update, todo_delete

app = FastAPI()


@app.get("/", tags=["ROOT"])
async def post_todo() -> dict:
    return {"message": "Fastodos"}


@app.post("/todos", tags=["CREATE TODO"])
async def post_todo(todo: dict) -> Todo:
    return await todo_create(todo)


@app.get("/todos/{id}", tags=["READ TODO"])
async def get_todo(id: str) -> list:
    return await todo_read(id)


@app.get("/todos", tags=["READ TODOS"])
async def get_todo() -> list:
    return await todos_list()


@app.put("/todos/{id}", tags=["UPDATE TODO"])
async def put_todo(id: str, body: Todo) -> Todo:
    return await todo_update(id, body)


@app.delete("/todos/{id}", tags=["DELETE TODO"])
async def delete_todo(id: str) -> list:
    return await todo_delete(id)
