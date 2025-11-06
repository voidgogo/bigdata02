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

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(df_diabetes['s1'], bins=20)
axes[0, 0].set_title('Diabetes Data : TC Distribution')
axes[0, 0].set_xlabel('TC')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].boxplot([df_diabetes['s1'], df_diabetes['s2'], df_diabetes['s3']])
axes[0, 1].set_title('Diabetes Data : Boxplot')
axes[0, 1].set_xticklabels(['TC', 'LDL', 'HDL'])

axes[1, 0].scatter(df_diabetes['s1'], df_diabetes['target'], color='coral', alpha=0.5)
axes[1, 0].set_title('Diabetes Data : TC vs Progression')
axes[1, 0].set_xlabel('TC')
axes[1, 0].set_ylabel('Progression')

axes[1, 1].scatter(x=df_diabetes['bmi'], y=df_diabetes['target'], color='green', alpha=0.5)
axes[1, 1].set_title('Diabetes Data : BMI vs Progression')
axes[1, 1].set_xlabel('BMI')
axes[1, 1].set_ylabel('Progression')

plt.show()
