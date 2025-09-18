import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
# print(mpg.isnull().sum())
# print(mpg[mpg['horsepower'].isnull()])

# 결측치 처리 #1
# mpg.dropna(inplace=True)  # mpg = mpg.dropna()
# print(mpg[mpg['horsepower'].isnull()])
# print(mpg.info())

# 결측치 처리 #2
# mpg = mpg.fillna(mpg['horsepower'].mean())
# print(mpg[mpg['horsepower'].isnull()])
# print(mpg.info())

# 결측치 처리 #3
mpg.drop(columns=['horsepower'], inplace=True)
print(mpg.info())