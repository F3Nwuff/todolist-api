from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials, firestore

cred = credentials.Certificate("api-todo-42f3a-firebase-adminsdk-2kgyf-a190b48cda.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = FastAPI()

class TodoItem(BaseModel):
    isCompleted: bool = False
    title: str
    userId: str  

@app.post("/tasks/")
async def create_todo(todo: TodoItem):
    doc_ref = db.collection('tasks').add(todo.dict())
    return {"id": doc_ref[1].id, **todo.dict()}

@app.get("/tasks/")
def read_tasks():
    tasks = db.collection('tasks').stream()
    return {todo.id: todo.to_dict() for todo in tasks}

@app.get("/tasks/user/{userId}")
async def read_user_tasks(userId: str):
    tasks = db.collection('tasks').where('userId', '==', userId).stream()
    return {todo.id: todo.to_dict() for todo in tasks}

@app.get("/tasks/{todo_id}")
def read_todo(todo_id: str):
    todo = db.collection('tasks').document(todo_id).get()
    if not todo.exists:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {todo.id: todo.to_dict()}

@app.put("/tasks/{todo_id}")
async def update_todo(todo_id: str, todo: TodoItem):
    todo_ref = db.collection('tasks').document(todo_id)
    if not todo_ref.get().exists:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_ref.set(todo.dict(), merge=True)
    return {"id": todo_id, "title": todo.title, "completed": todo.completed}

@app.delete("/tasks/{todo_id}")
async def delete_todo(todo_id: str):
    todo_ref = db.collection('tasks').document(todo_id)
    if not todo_ref.get().exists:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_ref.delete()
    return {"message": "Todo deleted"}