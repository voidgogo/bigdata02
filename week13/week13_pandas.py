import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

apple = pd.read_csv('APPL_price.csv')
apple['Date'] = pd.to_datetime(apple['Date'])
apple = apple.set_index('Date')
apple['Daily_Return'] = apple['Close'].pct_change() * 100
apple['Price_Change'] = apple['Close'].diff()
apple['High_Low_Range'] = ((apple['High'] - apple['Low']) / apple['Low']) * 100
apple['MA_20'] = apple['Close'].rolling(window=20).mean()
apple['Volatility'] = apple['Daily_Return'].rolling(window=20).std()
apple = apple.reset_index()
# print(apple[['Date', 'Close', 'Daily_Return', 'MA_20', 'Volatility']].tail(10))
apple['Year'] = apple['Date'].dt.year
yearly_stats = apple.groupby('Year')['Close'].agg([
    ('최고', 'max'),
    ('최저', 'min'),
    ('평균', 'mean'),
    ('개수', 'count'),
])
# print(yearly_stats.tail(9))

apple['Month'] = apple['Date'].dt.month
monthly_stats = apple.groupby('Month')['Close'].mean()
# print(monthly_stats)

# 분기별 수익율 분석
apple['Quarter'] = apple['Date'].dt.quarter
quarterly_return = apple.groupby(['Year', 'Quarter'])['Daily_Return'].sum()
# print(quarterly_return)

# 거래량이 많은 날 분석
# print(apple['Volume'])
apple['Volume_Category'] = pd.cut(apple['Volume'],
                                  bins=[0, 100000000, 300_000_000, 5e8, 10e10],
                                  labels=['Low', 'Medium', 'High', 'Very High']
                                  )
volume_analysis = apple.groupby(['Volume_Category'])['Close'].agg(['count', 'mean'])
print(volume_analysis)

