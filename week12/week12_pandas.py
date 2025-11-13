import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wh = pd.read_csv('wh.csv')
# new_wh = wh.query('Weight < 390')
# print(new_wh.info())
# print(new_wh.describe())

criteria = wh['Weight'].quantile(0.9999)  # 99.99% 이상인 데이터 지점
print(criteria)  # 약 255.9 파운드
print(round(criteria, 1))  # 255.9
new_wh = wh[wh['Weight'] < criteria]
print(new_wh.info())