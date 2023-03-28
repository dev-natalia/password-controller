from fastapi import APIRouter, Depends

from app.internal.password.models.generate_password import GeneratePasswordModel
from app.internal.password.logic.generate_password import GeneratePassword

router = APIRouter(
    prefix="/password",
    tags=["password"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root() -> dict:
    """
    Return a dictionary with a message indicating the Password Route.
    """
    return {"message": "Password Route"}

@router.post("/generate", tags=["password", "generate password"])
def generate_password(specifications: GeneratePasswordModel, password_generator: GeneratePassword = Depends()):
    """
    Generate a password based on the given specifications.

    Args:
        specifications: An instance of GeneratePasswordModel containing the desired specifications for the password.
        password_generator: An instance of the GeneratePassword class that can be reused across multiple requests.

    Returns:
        A string representing the generated password.
    """
    return password_generator.generate_password(specifications=specifications)
