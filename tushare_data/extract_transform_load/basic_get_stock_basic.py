import numpy as np 
import pandas as pd 
import tushare as ts 
from sqlalchemy import create_engine,text
import psycopg2
import common
import uuid

def get_data_from_tushare():
    ts.set_token(common.tushare_token)
    tushare_db = common.tushare_db
    pro = ts.pro_api()
    df_data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
    df_data['id'] = [str(uuid.uuid1()) for x in range(len(df_data))]
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(tushare_db['USER'],tushare_db['PASSWORD'],tushare_db['HOST'],tushare_db['PORT'],tushare_db['NAME']))
    if not df_data.empty:
        #step1: truncate table 
        engine.execute('truncate table tushare.tushare_stock_basic')
        #step2: insert into table
        df_data.to_sql(name='tushare_stock_basic',con=engine,schema='tushare',if_exists='append',index=False)

if __name__ == '__main__':
    get_data_from_tushare()

 