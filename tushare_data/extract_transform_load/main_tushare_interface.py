import numpy as np
import pandas as pd
import tushare as ts
from sqlalchemy import create_engine,text
import psycopg2
import common
import basic_get_stock_basic
import basic_get_trade_cal
import basic_get_name_change
import market_get_daily

'''
trade_date = '20210407'
start_date = '20210101'
end_date   = '20210408'
basic_get_stock_basic.get_data_from_tushare()
basic_get_trade_cal.get_data_from_tushare()
basic_get_name_change.get_data_from_tushare()
market_get_daily.get_data_from_tushare(trade_date)
market_get_daily.get_data_from_tushare_his(start_date,end_date)
'''
trade_date = '20210412'
start_date = '20210412'
end_date   = '20210412'
def get_basic_data_from_tushare():
    basic_get_stock_basic.get_data_from_tushare()
    basic_get_trade_cal.get_data_from_tushare(start_date,end_date)
    basic_get_name_change.get_data_from_tushare()

def get_his_data_from_tushare(start_date,end_date):
    get_basic_data_from_tushare()
    ts.set_token(common.tushare_token)
    tushare_db = common.tushare_db
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(tushare_db['USER'],tushare_db['PASSWORD'],tushare_db['HOST'],tushare_db['PORT'],tushare_db['NAME']))
    resultproxy = engine.execute(text("select distinct cal_date from tushare.tushare_trade_cal where is_open = '1' and cal_date between :start_date and :end_date order by cal_date desc"),{'start_date':start_date,'end_date':end_date})
    for rowproxy in resultproxy:
        trade_date = rowproxy.items()[0][1]
        market_get_daily.get_data_from_tushare(trade_date)
        print(trade_date,' success!')

def get_daily_data_from_tushare(trade_date):
    get_basic_data_from_tushare()
    ts.set_token(common.tushare_token)
    tushare_db = common.tushare_db
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(tushare_db['USER'],tushare_db['PASSWORD'],tushare_db['HOST'],tushare_db['PORT'],tushare_db['NAME']))
    resultproxy = engine.execute(text("select distinct cal_date from tushare.tushare_trade_cal where is_open = '1' and cal_date = :trade_date order by cal_date desc"),{'trade_date':trade_date})
    for rowproxy in resultproxy:
        trade_date = rowproxy.items()[0][1]
        market_get_daily.get_data_from_tushare(trade_date)

if __name__ == '__main__':
    get_his_data_from_tushare(start_date,end_date)