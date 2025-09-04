import numpy as np

# 조건부 선택과 필터링
h = np.arange(1, 6)

mask = h > 2
print(h[mask])

result = np.where(h > 3, h, 0)  # 3보다 큰 값은 그 값 그대로 3이하의 값은 0으로 처리
print(result)