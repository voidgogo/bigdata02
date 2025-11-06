import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes

# 당뇨병 데이터셋 로드

# 나이, 성별, 체질량지수, 평균혈압, TC 총 콜레스테롤(s1)
# LDL 나쁜 콜레스테롤 수치(s2), HDL 좋은 콜레스테롤 수치(s3)
# TCH (s1/s3 = s4), LTG 로그 변환된 중성지방수치 (s5)
# GLU 공복혈당수치 (s6)
diabetes = load_diabetes()
# print(diabetes.feature_names)  # age, sex, bmi, bp .... s6

# print(diabetes)
# print(type(diabetes))
# print(diabetes.info())  # 판다스 데이터 프레임이 아님. 오류
# print(diabetes.target)  # 당뇨병 진행 정도 값
# print(diabetes.data)

df_diabetes = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
# print(df_diabetes.info())
print(df_diabetes.tail())
