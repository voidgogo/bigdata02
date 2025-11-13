import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

usc = pd.read_csv('us_corona19.csv')
usc['Date'] = pd.to_datetime(usc['Date'])
usc = usc.set_index('Date').sort_values('Date')
states = usc['Province/State'].unique()[0:5]
# print(states, len(states))
# print(usc.head(20))
usc = usc[usc['Province/State'].isin(states)]
# print(usc)
# 6개월 단위 그룹으로 5개주(상위) 코로나19 발병 횟수 평균 값
print(usc.groupby([pd.Grouper(freq='6m'), 'Province/State'])['Case'].mean())