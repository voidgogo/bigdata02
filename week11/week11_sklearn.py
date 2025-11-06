import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_diabetes

# 나이, 성별, 체질량지수, 평균혈압, TC 총 콜레스테롤(s1)
# LDL 나쁜 콜레스테롤 수치(s2), HDL 좋은 콜레스테롤 수치(s3)
# TCH (s1/s3 = s4), LTG 로그 변환된 중성지방수치 (s5)
# GLU 공복혈당수치 (s6) # target 당뇨병 진행 정도 값
diabetes = load_diabetes()
df_diabetes = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df_diabetes['target'] = diabetes.target  # 당뇨병 진행 정도 값

corr = df_diabetes.corr()  # correlation (상관관계)
# print(corr)

# 당뇨병 데이터셋 상관관계 히트맵
plt.figure(figsize=(12, 10))
sns.heatmap(corr, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.6)
plt.show()
