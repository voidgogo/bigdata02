import numpy as np

g = np.array([
    [3, 2, 1],
    [6, 5, 4]
])
print(np.sum(g))
print(np.sum(g, axis=0))  # 열 기준을 축으로 더함
print(np.sum(g, axis=1))  # 행 기준을 축으로 더함

print(np.mean(g))  # 산술평균  21/6
print(np.max(g))
print(np.min(g))
print(np.std(g))  # 표준편차 standard deviation