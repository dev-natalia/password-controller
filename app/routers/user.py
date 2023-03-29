from fastapi import APIRouter, Depends

from app.internal.user.models.user import CreateUserModel
from app.internal.user.logic.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root() -> dict:
    """
    Return a dictionary with a message indicating the User Route.
    """
    return {"message": "User Route"}

@router.post("/", tags=["user", "create user"])
def generate_user(data: CreateUserModel, user: User = Depends()):
    """
    Generate a user based on the given data.

    Args:
        data: An instance of CreateUserModel containing the desired data for the user.
        user: An instance of the User class that can be reused across multiple requests.
    """
    user.create_user(data=data)
