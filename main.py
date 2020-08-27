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

    return templates.TemplateResponse("home.html",{
        "request" : request
    })

# UPLOAD dan CONVERSION
@app.post("/result")
async def create_upload_file(request : Request , anime1: str = File(...), anime2 : str = File(...)):
    reco = mal_scrap.big_list_recommendation([anime1, anime2])
    arr_reco = []
    for i in reco:

        print(i)
        arr_reco.append([mal_scrap.get_title(i), reco[i][0], reco[i][1]])

    return templates.TemplateResponse("download.html",{
      "request" : request,
      "data" : arr_reco
      })




if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 5001)
