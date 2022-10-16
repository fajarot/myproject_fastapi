from replit import db

import schemas

def insert(name: schemas.nameInsert):
  data = name.dict()
  name, message = data['name'], data['message']

  db[name] = message
  
  return schemas.nameOut(name=name, message=db[name])

def get(name: schemas.nameRead):
  data = name.dict()
  name = data['name']

  return schemas.nameOut(name=name, message=db[name])

def get_direct(name: str):
  return schemas.nameOut(name=name, message=db[name])
