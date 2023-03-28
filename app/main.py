from fastapi import FastAPI

from .routers import password


app = FastAPI(
    title="Password Myth",
    description="A FastAPI app for generating passwords based on custom specifications.",
    version="1.0.0",
)

app.include_router(password.router)


@app.get("/", tags=["home"])
async def root():
    """
    Return a greeting message for the home page.
    """
    return {"message": "Hello Password Myth!"}
