import os

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from settings import SETTINGS

app = FastAPI()
if os.path.exists(SETTINGS.static_folder):
    app.mount("/static", StaticFiles(directory=SETTINGS.static_folder), name="static")
if os.path.exists(SETTINGS.templates_folder):
    templates = Jinja2Templates(directory=SETTINGS.templates_folder)


@app.get("/")
def root(request: Request) -> JSONResponse:
    return JSONResponse({"cookies": request.cookies})
