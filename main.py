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
async def create_upload_file(request : Request , anime1: str = File(...), anime2 : str = File(...), anime3 : str = File(...), anime4 : str = File(...), anime5 : str = File(...), anime6 : str = File(...), anime7 : str = File(...), anime8 : str = File(...), anime9 : str = File(...), anime10 : str = File(...), anime11 : str = File(...), anime12 : str = File(...), anime13 : str = File(...), anime14 : str = File(...), anime15 : str = File(...)):
	arr = [anime1, anime2, anime3, anime4, anime5, anime6, anime7, anime8, anime9, anime10, anime11, anime12, anime13, anime14, anime15]
	arr = list(filter(("-").__ne__, arr))
	print(arr)
	reco = mal_scrap.big_list_recommendation(arr)
	arr_reco  = []
	arr_reco2 = []
	for i in reco:
		print(reco[i][0])

		
		if(i in arr):
			arr_reco2.append([i, reco[i][0], reco[i][1] * reco[i][2], "background:#34495e"])
			arr_reco.append([i, reco[i][0],  reco[i][1],  reco[i][2], "background:#34495e"])
		else:
			arr_reco2.append([i, reco[i][0], reco[i][1] * reco[i][2], ""])
			arr_reco.append([i,  reco[i][0], reco[i][1],  reco[i][2], ""])

	arr_reco  = sorted(arr_reco,  key=lambda l:l[2], reverse=True)
	arr_reco2 = sorted(arr_reco2, key=lambda l:l[2], reverse=True)

	return templates.TemplateResponse("download.html",{
	  "request" : request,
	  "data" : arr_reco,
	  "data2" : arr_reco2
	  })




if __name__ == "__main__":
		uvicorn.run(app, host = "127.0.0.1", port = 5001)
