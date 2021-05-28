"""
Implementation of Modern Portfolio Theory

"""

import numpy as np
import datetime as dt
from pandas_datareader import data as pdr

# import data

def getData(stocks, start, end ):
    stockData = pdr.get_data_yahoo(stocks, start=start, end=end)
    return stockData
    
    
stocklist = ['CBA', 'BHP', 'TLS']
stocks = [stock+'.AX'  for stock in stocklist]

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365)


print(getData(stocks, start=startDate, end=endDate))


d
