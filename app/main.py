from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import person

app = FastAPI()


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(person.router)
