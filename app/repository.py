from .database import todos
from .models import Todo
from .utils import generate_uuid


async def todos_list() -> list:
    return todos


async def todo_create(todo: dict) -> Todo:
    new_todo = {
        "id": generate_uuid(),
        "title": todo["title"],
        "description": todo["description"],
    }
    todos.append(new_todo)
    return new_todo


async def todo_read(id: str) -> list:
    print(id)
    print(todos)
    todo = [todo for todo in todos if todo["id"] == id]
    return todo


async def todo_update(id: str, body: Todo) -> Todo:
    todo = [todo for todo in todos if todo["id"] == id]
    todo = todo.update(body)
    return todo


async def todo_delete(id: str) -> list:
    todo = [todo for todo in todos if todo["id"] == id]
    todos.delete(todo)
    return todos
