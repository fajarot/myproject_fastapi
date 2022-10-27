from typing import Union
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

import schemas
import crud

# curl ifconfig.co
# 34.138.154.254
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get('/')
async def root():
  return {"message": "Hello World"}

@app.get('/help')
async def docs():
  return RedirectResponse(url="/docs")

@app.post('/api/write', response_model=schemas.nameOut)
async def post_name(dataIn: schemas.nameInsert):
  return crud.insert(dataIn)

@app.post('/api/read', response_model=Union[schemas.nameOut, schemas.errorHandle])
async def read_name(dataIn: schemas.nameRead):
  return crud.get(dataIn)

@app.get('/api/read/{name}', response_model=Union[schemas.nameOut, schemas.errorHandle])
async def get_name(name: str):
  return crud.get_direct(name)

@app.get('/api/tes', response_model=schemas.dataOut)
async def tes():
  return crud.tes();

@app.post('/api/midtrans', response_model=schemas.responseApi)
async def tes_midtrans(data: schemas.getApi):
  return crud.midtrans(data)

@app.get('/api/v1/tes', response_model=schemas.responseApi)
async def tes_sql():
  return crud.tes_sql()




@app.post('/api/v1/midtrans', response_model=schemas.responseApi)
async def input_data_midtrans(data: schemas.getApi):
  return crud.input_midtrans(data)

@app.get('/api/v1/order/{tele_id}', response_model=schemas.responseApi)
async def check_data(tele_id: str):
  return crud.isOrder_midtrans(tele_id)


if __name__ == "__main__":
  # uvicorn.run(app, host="0.0.0.0", port="8080")

  # dev mode
  uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
