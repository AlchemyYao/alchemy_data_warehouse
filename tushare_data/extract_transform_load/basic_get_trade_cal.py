import numpy as np 
import pandas as pd 
import tushare as ts 
from sqlalchemy import create_engine,text
import psycopg2
import common
import uuid

def get_data_from_tushare(start_date,end_date):
    ts.set_token(common.tushare_token)
    tushare_db = common.tushare_db
    pro = ts.pro_api()
    df_data = pro.trade_cal(exchange='', start_date=start_date, end_date=end_date, fields='exchange,cal_date,is_open,pretrade_date')
    df_data['id'] = [str(uuid.uuid1()) for x in range(len(df_data))]
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(tushare_db['USER'],tushare_db['PASSWORD'],tushare_db['HOST'],tushare_db['PORT'],tushare_db['NAME']))
    if not df_data.empty:
        #step1: truncate table 
        engine.execute(text('delete from  tushare.tushare_trade_cal where cal_date between :start_date and :end_date'),{'start_date':start_date,'end_date':end_date})
        #step2: insert into table
        df_data.to_sql(name='tushare_trade_cal',con=engine,schema='tushare',if_exists='append',index=False)

if __name__ == '__main__':
    get_data_from_tushare(start_date,end_date)