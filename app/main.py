from fastapi import FastAPI

app = FastAPI(title="FastAPI Development",
              summary="Best API Development for python easy to learn and production ready...",
              version="1")


@app.get("/")
def welcome_greet():
    return {"message": "Welcome to FastAPI Development..."}


@app.get("/info")
def show_information():
    return {"message": "This is the information page"}
