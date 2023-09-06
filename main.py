from fastapi import FastAPI, status
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root(slack_name: str = "", track: str = ""):
    output = {
        "current_day": datetime.today().strftime("%A"),
        "utc_time": datetime.utcnow(),
        "github_file_url": "https://github.com/ademolab91/stage_1/blob/main/main.py",
        "github_repo_url": "https://github.com/ademolab91/stage_1",
        "status_code": status.HTTP_200_OK,
    }
    output.update({"slack_name": slack_name, "track": track})
    return output
