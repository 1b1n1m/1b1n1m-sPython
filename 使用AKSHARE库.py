import akshare as ak
import pandas as pd

stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol="sz000002", start_date='20201103', end_date='20201116', adjust="hfq")
print(stock_zh_a_daily_hfq_df)
