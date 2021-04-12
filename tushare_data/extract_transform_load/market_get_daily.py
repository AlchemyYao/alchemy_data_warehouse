import numpy as np 
import pandas as pd 
import tushare as ts 
from sqlalchemy import create_engine,text
import psycopg2
import common
import uuid

def get_data_from_tushare(trade_date):
    ts.set_token(common.tushare_token)
    tushare_db = common.tushare_db
    pro = ts.pro_api()
    df_data = pro.daily(trade_date = trade_date , fields = 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount')
    df_data['id'] = [str(uuid.uuid1()) for x in range(len(df_data))]
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(tushare_db['USER'],tushare_db['PASSWORD'],tushare_db['HOST'],tushare_db['PORT'],tushare_db['NAME']))
    if not df_data.empty:
        #step1: truncate table 
        engine.execute(text('delete from tushare.tushare_daily where trade_date = :trade_date'),{'trade_date':trade_date})
        #step2: insert into table
        df_data.to_sql(name='tushare_daily',con=engine,schema='tushare',if_exists='append',index=False)
if __name__ == '__main__':
    trade_date = '20210407'
    get_data_from_tushare(trade_date)

 