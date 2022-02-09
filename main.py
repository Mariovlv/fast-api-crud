from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdate
from typing import List
from uuid import UUID

app = FastAPI(
    title = "My first API",
    version = "0.0.1"
)

db: List[User] = [
        User(
            id = UUID("6f242aa2-9bcb-4e7e-a36d-3f98255794a9"),
            first_name = "Kenia",
            last_name = "Ortiz",
            middle_game = 'IDK',
            gender=Gender.female,
            roles=[Role.vip]
        ),
        User(
            id = UUID("b2ef2a34-4e1d-4247-ab4b-24202edb0b9b"),
            first_name = "Levon",
            last_name = "Zik",
            gender=Gender.male,
            roles=[Role.normal, Role.admin]
        ),
        User(
            id = UUID("24b40b70-9280-4c37-bede-48e906802065"),
            first_name = "Leonardo",
            last_name = "Di Caprio",
            gender=Gender.male,
            roles=[Role.normal]
        )
]

@app.get('/')
async def root():
    return {'Hello':  'World'}

@app.get('/api/v1/users')
async def fetch_users():
        return db
        

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"Succes"}
    
    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} does not exist"
    )

@app.put('/api/v1/users/{user_id}')
async def update_user(user_update: UserUpdate, user_id: UUID):
    for user in db:
        if user.id == user_id:
            # Update data
            if user_update.first_name:
                user.first_name = user_update.first_name
            if user_update.last_name:
                user.last_name = user_update.last_name
            if user_update.middle_game:
                user.middle_game = user_update.middle_game
            if user_update.roles:
                user.roles = user_update.roles
            return {"Succes"}

    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} does not exist"
    )