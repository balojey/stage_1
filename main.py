from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/api")
async def root(slack_name: str = "", track: str = ""):
    output = {
        "current_day": datetime.today().strftime("%A"),
        "utc_time": datetime.utcnow().isoformat().rsplit(".", 1)[0] + "Z",
        "github_file_url": "https://github.com/ademolab91/stage_1/blob/main/main.py",
        "github_repo_url": "https://github.com/ademolab91/stage_1",
        "status_code": status.HTTP_200_OK,
    }
    output.update({"slack_name": slack_name, "track": track})
    return output
