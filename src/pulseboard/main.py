"""FastAPI application entrypoint for PulseBoard."""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pulseboard.config.app_config import config

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


def main() -> None:
    """Run Uvicorn server for development."""
    from uvicorn import run

    run(
        "pulseboard.main:app",
        host="0.0.0.0",
        port=config.WEB_PORT,
        reload=config.DEBUG,
    )


if __name__ == "__main__":
    main()
