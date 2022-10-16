from pydantic import BaseModel


class nameInsert(BaseModel):
  name: str
  message: str

class nameRead(BaseModel):
  name: str

class nameOut(BaseModel):
  name: str
  message: str