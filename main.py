import mal_scrap


import uvicorn
import os, shutil
from pydantic import BaseModel, Field
from fastapi import Request, Depends, BackgroundTasks, Form, File, UploadFile, FastAPI as fastapi
from fastapi.templating import Jinja2Templates
# from typing import List
# from starlette.responses import PlainTextResponse, RedirectResponse
# from starlette.responses import FileResponse


app = fastapi()
templates = Jinja2Templates(directory="templates")




@app.get("/")
async def home(request : Request):
    return templates.TemplateResponse("home.php",{
        "request" : request
    })





if __name__ == "__main__":
    uvicorn.run(app, host = "172.0.0.1", port = 5001
