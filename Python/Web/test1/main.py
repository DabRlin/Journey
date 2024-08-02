from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 用户模型
class User(BaseModel):
    id: int
    name: str
    email: str

# 模拟数据库
users_db = []

@app.get("/users", response_model=List[User])
def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((user for user in users_db if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    user = next((user for user in users_db if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = updated_user.name
    user.email = updated_user.email
    return user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    global users_db
    users_db = [user for user in users_db if user.id != user_id]
    return
