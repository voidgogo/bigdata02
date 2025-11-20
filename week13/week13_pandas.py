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
apple['Year'] = apple['Date'].dt.year
yearly_stats = apple.groupby('Year')['Close'].agg([
    ('최고', 'max'),
    ('최저', 'min'),
    ('평균', 'mean'),
    ('개수', 'count'),
])
apple['Month'] = apple['Date'].dt.month
monthly_stats = apple.groupby('Month')['Close'].mean()
# 분기별 수익율 분석
apple['Quarter'] = apple['Date'].dt.quarter
quarterly_return = apple.groupby(['Year', 'Quarter'])['Daily_Return'].sum()
# 거래량이 많은 날 분석
apple['Volume_Category'] = pd.cut(apple['Volume'],
                                  bins=[0, 100000000, 300_000_000, 5e8, 10e10],
                                  labels=['Low', 'Medium', 'High', 'Very High']
                                  )
volume_analysis = apple.groupby(['Volume_Category'])['Close'].agg(['count', 'mean'])
# 최근 2년 데이터
recent_2year = apple[apple['Date'] >= '2020-06-17']
# 가격 100달러 이상
high_price_days =apple[apple['Close'] >= 100]
# 수익율이 양수인 날
positive_return = apple[apple['Daily_Return'] > 0]
# print(f"{len(positive_return) / len(apple) * 100:.2f}")
# 거래량이 상위 5%에 해당하는 날
high_volume_threshold = apple['Volume'].quantile(0.95)
# print(high_volume_threshold)
high_volume_days = apple[apple['Volume'] >= high_volume_threshold]
# print(high_volume_days)

apple_filtered = apple[(apple['Date'] >= '2020-01-01') &
                       (apple['Close'] > 50) &
                       (apple['Volume'] > 2e8)]
print(apple_filtered)