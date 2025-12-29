from fastapi import FastAPI
from fastapi import Response
from fastapi.requests import Request
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse  , RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException
from starlette.types import Message

from .logger import logger
from .dash import get_dashboard_data

srv = FastAPI(title="litewolf")
templates = Jinja2Templates("templates")

srv.mount("/static", StaticFiles(directory="static"), name="static")

@srv.exception_handler(404)
def not_found(req: Request, exc: HTTPException):
  return templates.TemplateResponse(
        "error.j2",
        {"request": req ,"code": 404 , "message": "Page Not Found" }
    )


@srv.get("/favicon.ico")
def favicon():
    return RedirectResponse(url="/static/icons/favicon.svg")

@srv.get("/dashboard")
def dash2app():
    return RedirectResponse(url="/app")

@srv.get("/" , response_class=HTMLResponse)
async def home(req : Request):
  return templates.TemplateResponse(
        "home.j2",
        {"request": req }
    )

@srv.get("/auth" , response_class=HTMLResponse)
async def auth(req : Request):
  return templates.TemplateResponse(
        "login.j2",
        {"request": req }
    )

@srv.get("/new-user" , response_class=HTMLResponse)
async def signin(req : Request):
  return templates.TemplateResponse(
        "signin.j2",
        {"request": req }
    )

@srv.get("/app" , response_class=HTMLResponse)
async def app(req : Request):
  data = get_dashboard_data()
  return templates.TemplateResponse(
        "app.j2",
        {"request": req, **data }
    )


@srv.post("/auth/login")
async def login(req: Request):
  form = await req.json()
  logger.debug(f"/auth: {form.get('email')}")
  return { "success": True , "message" : "" }

@srv.post("/auth/signin")
async def signgin(req: Request):
  form = await req.json()
  logger.debug(f"/auth: {form.get('-')}")
  return { "success": True , "message" : "" }

