from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

@app.get('/user/{user_id}')
async def get_user(user_id: int = Path(ge=1, le=100, description='Enter User ID')):
    return {"user_id": user_id}

@app.get('/user/{username}/{age}')
async def get_user_info(
    username: Annotated[str,  Path(min_length=5, max_length=20, description='Enter username')],
    age: int = Path(ge=18, le=120, description='Enter age')
):
    return {"username": username, "age": age}