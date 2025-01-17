from fastapi import APIRouter
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    users = db.scalar(select(User).where(user_id == User.id))
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User was not found")
    return users


@router.post('/create')
async def create_user(create: CreateUser, db: Annotated[Session, Depends(get_db)]):
  db.execute(insert(User).values(
    username=create.username,
    firstname=create.firstname,
    lastname=create.lastname,
    age=create.age,
    slug=slugify(create.username)))
  db.commit()
  return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(user_update: UpdateUser, user_id: int, db: Annotated[Session, Depends(get_db)]):
  update_user = db.scalars(select(User).where(user_id == User.id)).first()
  if update_user is None:
    return HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='User was not found'
    )
  db.execute(update(User).where(user_id == User.id).values(
    firstname=user_update.firstname,
    lastname=user_update.lastname,
    age=user_update.age
  ))
  db.commit()
  return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.put('/delete')
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
  delete_user = db.scalars(select(User).where(user_id == User.id)).first()
  if delete_user is None:
    return HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='User was not found'
    )
  db.execute(delete(User).where(user_id == User.id))
  db.commit()
  return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}