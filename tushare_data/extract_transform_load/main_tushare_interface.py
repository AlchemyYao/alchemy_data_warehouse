import basic_get_stock_basic
import basic_get_trade_cal
import basic_get_name_change
import market_get_daily

trade_date = '20210407'
start_date = '20210101'
end_date   = '20210407'
basic_get_stock_basic.get_data_from_tushare()
basic_get_trade_cal.get_data_from_tushare()
basic_get_name_change.get_data_from_tushare()
market_get_daily.get_data_from_tushare(trade_date)
