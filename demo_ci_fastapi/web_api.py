from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
def healthcheck():
    """Base url to check if app is up."""
    return {}


@app.post("/uploadfile")
async def upload_file(data_file: UploadFile):
    """Upload a file."""
    return {"filename": data_file.filename}
