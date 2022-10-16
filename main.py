import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

import schemas
import crud

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

@app.post('/api/read', response_model=schemas.nameOut)
async def read_name(dataIn: schemas.nameRead):
  return crud.get(dataIn)

@app.get('/api/read/{name}', response_model=schemas.nameOut)
async def get_name(name: str):
  return crud.get_direct(name)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port="8080")
