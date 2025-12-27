
from fastapi import FastAPI
from fastapi import Response
from fastapi.requests import Request
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse  , RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException

srv = FastAPI(title="litewolf")
templates = Jinja2Templates("templates")

srv.mount("/static", StaticFiles(directory="static"), name="static")

@srv.exception_handler(404)
def not_found(req: Request, exc: HTTPException):
  return templates.TemplateResponse(
        "error.html",
        {"request": req ,"code": 404 , "message": "Page Not Found" }
    )


@srv.get("/favicon.ico")
def favicon():
    return RedirectResponse(url="/static/icons/favicon.svg")


@srv.get("/" , response_class=HTMLResponse)
async def home(req : Request):
  return templates.TemplateResponse(
        "home.html",
        {"request": req }
    )

