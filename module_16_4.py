from pydantic import BaseModel
from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()


class Users(BaseModel):
    id: int = Path(ge=1, le=100, description='Enter User ID')
    username: str = Path(min_length=5, max_length=20, description='Enter username')
    age: int = Path(ge=18, le=120, description='Enter age')

users: list[Users] = []

@app.get("/users", response_model=list[Users])
async def get_all_users():
    return users

@app.post("/user/{username}/{age}")
async def add_user( username: Annotated[str,  Path(min_length=5, max_length=20, description='Enter username')],
                   age:  Annotated[int, Path(ge=18, le=120, description='Enter age')]):
    user_id = (users[-1].id + 1) if users else 1
    user = Users(username=username, age=age, id=user_id)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}", response_model=Users)
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                      username: Annotated[str,  Path(min_length=5, max_length=20, description='Enter username')],
                      age:  Annotated[int, Path(ge=18, le=120, description='Enter age')]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404 ,detail="User was not found")

@app.delete("/user/{user_id}", response_model=Users)
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
