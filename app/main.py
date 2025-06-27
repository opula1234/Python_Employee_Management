"""Main module for FastAPI Development application."""

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Development",
    summary="Best API Development for python easy to learn and " "production ready...",
    version="1",
)


@app.get("/")
def welcome_greet():
    """Return a welcome message for the FastAPI application."""
    return {"message": "Welcome to FastAPI Development..."}


@app.get("/info")
def show_information():
    """Return information about the application."""
    return {"message": "This is the information page"}
