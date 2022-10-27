from replit import db
from database import Database

import schemas

mydb = Database()

def insert(name: schemas.nameInsert):
  data = name.dict()
  name, message = data['name'], data['message']

  db[name] = message
  
  return schemas.nameOut(name=name, message=db[name])

def get(name: schemas.nameRead):
  data = name.dict()
  name = data['name']

  if name in db:
    return schemas.nameOut(name=name, message=db[name])
  else:
    return schemas.errorHandle(code=404, message='Data Not Found')


def get_direct(name: str):
  if name in db:
    return schemas.nameOut(name=name, message=db[name])
  else:
    return schemas.errorHandle(code=404, message='Data Not Found')

def tes():
  print(mydb.get_data())
  return schemas.dataOut(status=200, data=schemas.dataIn(name='fajar ganteng banget'))

def midtrans(data: schemas.getApi):
  data = data.dict()
  print(data)
  
  return schemas.responseApi(status=200)

def tes_sql():
  
  with Database() as mydbs:
    msg = mydbs.tes_sql_query()
  
  return schemas.responseApi(status=200, message=msg)




def input_midtrans(data: schemas.getApi):
  data = data.dict()
  data['tele_id'] = data['order_id'].split('-')[1]

  if mydb.check_order_exist(data['order_id']) == 1:
    return schemas.responseApi(status=202, message='data already in DB')

  status = 200 if mydb.insert_payment(data) == True else 500

  return schemas.responseApi(status=status)


def isOrder_midtrans(tele_id: str):
  status = 200
  msg = mydb.get_pending_order(tele_id)
  return schemas.responseApi(status=status, message=str(msg))
  