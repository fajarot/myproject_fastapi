import os
import mysql.connector


def create_db_conn(value_date):
    if value_date == 'xyz':
        db = 'db1'
    else:
        db = 'wetrayma_db'
    
    iss_cnxn = mysql.connector.connect(
                      host=os.environ['db_ip'],
                      database=db,
                      user='wetrayma_user',
                      password=os.environ['db_pass'],
                    )
    return iss_cnxn

class Database:
  mydb = create_db_conn('asda')

  table_name = {
  'order_history': 'order_history',
  'order_fail': 'order_fail',
  'order_success': 'order_success'
}

  def __init__(self):
    self.db = Database.mydb
    self.cursor = self.db.cursor()

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.db.close()

  
  def insert_payment(self, data, table):

    for table_name in table:
      sql = '''INSERT INTO '''+table_name+''' 
      (order_id, tele_id, status_code, payment_type, 
      merchant_id, gross_amount, fraud_status, currency, 
      transaction_id, transaction_status, transaction_time) 
      VALUES 
      (%s, 
      (SELECT tele_id FROM user WHERE tele_id = %s), 
      %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
      val = (data['order_id'], data['tele_id'], data['status_code'], data['payment_type'], data['merchant_id'], data['gross_amount'], data['fraud_status'], data['currency'], data['transaction_id'], data['transaction_status'], data['transaction_time'])
      
      self.cursor.execute(sql, val)
  
  
    return self

  
  def get_data(self):
    self.cursor.execute('SELECT * FROM user WHERE user_id=1')

    result = self.cursor.fetchall()

    for x in result:
      result = x

    return result


  def check_order_exist(self, order_id):
    
    query = "SELECT EXISTS (SELECT order_id FROM order_history WHERE order_id = %s) LIMIT 1"

    val = (order_id,)

    self.cursor.execute(query, val)

    result = self.cursor.fetchone()

    return result[0]


  def get_pending_order(self, tele_id):

    query = "SELECT EXISTS (SELECT tele_id FROM order_history WHERE %s IN (SELECT tele_id FROM order_history WHERE transaction_status = 'pending'))"

    val = (tele_id,)

    self.cursor.execute(query, val)

    result = self.cursor.fetchone()

    return result[0]


  def tes_sql_query(self, input):

    # for x in ('GeekTable1', 'GeekTable2'):
    #   query = '''INSERT INTO '''+x+''' (Id, Name, City)
    #               VALUES (%s, %s, %s)'''
    #   val = (data[0], data[1], data[2])
    #   self.cursor.execute(query, val)
    # for x in ('GeekTable1', 'GeekTable2'):
    for data in input:
      query = '''INSERT INTO '''+data[3]+''' (Id, Name, City)
                  VALUES (%s, %s, %s)'''
      val = (data[0], data[1], data[2])
      self.cursor.execute(query, val)

    return self
    

  def comit(self):
    
    self.db.commit()
    
    result = 'Notif Inserted' if self.cursor.rowcount > 0 else 'Something Wrong'
    print("1 record inserted, ID:", self.cursor.rowcount)
    
    return result

