

from fastapi import FastAPI
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
from fastapi.staticfiles import StaticFiles


def include_router(app):
	app.include_router(general_pages_router)

def configure_static(app):  #new
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	return app 


app = start_application()


# @app.get("/") #remove this, It is no longer needed.
# def hello_api():
#     return {"msg":"Hello API"}