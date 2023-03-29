from typing import Optional
from pydantic import BaseModel


class CreateUserModel(BaseModel):
    id: Optional[str]
    username: str
    password: str
