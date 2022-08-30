from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def healthcheck():
    """Base url to check if app is up."""
    return {}
