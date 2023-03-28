from pydantic import BaseModel, validator

class GeneratePasswordModel(BaseModel):
    """
    A Pydantic model representing the specifications for generating a password.
    """

    number: bool = True
    special_char: bool = False
    upper_case: bool = True
    low_case: bool = True
    length: int = 12

    @validator("length")
    def length_must_be_greater_than_zero(cls, value):
        """
        Validate that the length of the password is greater than zero.
        """
        if value <= 0:
            raise ValueError("Length must be greater than zero")
        return value
