import os
import shutil
import tempfile

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from backend.analyzer import analyzer


app = FastAPI(title="Spatia AI Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "app": "Spatia",
        "status": "online"
    }


@app.post("/analyze-room")
async def analyze_room(
    video: UploadFile = File(...),
    budget: int = Form(...)
):

    suffix = os.path.splitext(video.filename or ".mp4")[1]

    temporary_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    )

    try:

        with temporary_file as file:

            shutil.copyfileobj(
                video.file,
                file
            )

        result = analyzer.analyze_video(
            temporary_file.name,
            budget
        )

        return {
            "success": True,
            "analysis": result
        }

    finally:

        if os.path.exists(temporary_file.name):
            os.remove(temporary_file.name)