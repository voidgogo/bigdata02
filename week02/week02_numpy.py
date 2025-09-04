import numpy as np

c = np.arange(1, 13)  # 1차원 배열

# r = c.reshape(2, 2, 3)  # 3차원 배열형태로 변환
r = c.reshape(4, 3)  # 2차원 배열형태로 변환
print(c)
print(r)
f = r.flatten()  # 2차원 배열을 1차원 배열로 변환
print(f)

# 전치행렬
t = r.T
print(t)

# 단위행렬
e1 = np.eye(4)
print(e1)