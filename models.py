from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    vip = "Vip"
    normal = "Normal"
    admin = "Admin"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_game: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_game: Optional[str]
    roles: Optional[List[Role]]