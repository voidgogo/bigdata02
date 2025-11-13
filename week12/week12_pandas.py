import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# 특정 기간동안 미국에서 코로나19 바이러스 확진자 수를 지역으로 나눠 정리한 데이터
usc = pd.read_csv('us_corona19.csv')
# print(usc.info())
usc['Date'] = pd.to_datetime(usc['Date'])  # object -> datetime
# print('='*20)
# print(usc.info())
usc = usc.set_index('Date').sort_values('Date')  # 인덱스를 날짜로 변경, 그리고 날짜 기준 오름차순으로 정렬
# print(usc)
# print(usc['2021-09' : '2021-10'])  # 슬라이싱
# print(usc.reset_index().set_index('Province/State').sort_index())
usc = usc.reset_index().set_index('Province/State').sort_index()
# print(usc.index)
print(usc.index.unique(), len(usc.index.unique()))