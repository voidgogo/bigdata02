import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

apple = pd.read_csv('APPL_price.csv')
# print(apple.head())
# print(apple.describe())
# print(apple.info())
apple['Date'] = pd.to_datetime(apple['Date'])  # object -> datetime
# print(apple.info())
apple = apple.set_index('Date')  # index를 날짜시간 칼럼으로 대체
# print(apple.head())
# print(apple.tail())

# 시계열 데이터 슬라이싱
# print(apple['2022-06-14':'2022-06-16'])
# print(apple['2022-04':'2022-06'])

print(apple['Close'])
apple_1months = apple.resample('1M').mean()  # 일주일 단위로 행을 묶어 평균값 추출
print(apple_1months['Close'])
# print(apple.info())
# print(apple_7days.describe())