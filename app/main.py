from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import person

app = FastAPI()


@app.get("/", tags=["docs"])
def docs_redirect():
    return RedirectResponse(url="/docs")


app.include_router(person.router)
