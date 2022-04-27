from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routes import person, country

app = FastAPI()


@app.get("/", tags=["docs"])
def docs_redirect():
    return RedirectResponse(url="/docs")


app.include_router(person.router)
app.include_router(country.router)
