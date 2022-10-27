from typing import Optional
from pydantic import BaseModel, Extra, Field, validator


class nameInsert(BaseModel):
  name: str
  message: str

class nameRead(BaseModel):
  name: str

class nameOut(BaseModel):
  name: str
  message: str

class errorHandle(BaseModel):
  code: int
  message: str


class dataIn(BaseModel):
  class Config:
        extra = Extra.forbid

  name: Optional[str] = Field(None, description="name ini adalah")
  tele_id: Optional[str] = Field(None, description="ini user tele id")


class dataOut(BaseModel):
  status: int
  data: Optional[dataIn] = Field(None, description='data ini apa')
  message: Optional[str] = Field(None, description='pesan apa yang mau di sampaikan')

  class Config:
    validate_assignment=True

  @validator('message')
  def set_message(cls, message):
    return message or 'Success'
    



class getApi(BaseModel):
  tele_id: str = None
  order_id: str
  status_code: str
  payment_type: str
  merchant_id: str
  gross_amount: str
  fraud_status: str
  currency: str
  transaction_id: str
  transaction_status: str
  transaction_time: str
  
class responseApi(BaseModel):
  status: int
  message: Optional[str] = None

  # class Config:
  #   validate_assignment=True

  # @validator('message')
  # def set_message(cls, msg, *, values):
  #   msg = 'Success' if values['status'] == 200 else 'Something Wrong'
  #   return msg


  

