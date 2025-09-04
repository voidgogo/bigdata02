import numpy as np

np.random.seed(50)  # 시드 설정

x = np.random.random(5)  # 0 ~ 1 사이의 실수 5개 랜덤 추출
print(x)
y = np.random.randint(1, 10, 5)  # 1 ~ 9 사이의 정수 5개 랜덤 추출
print(y)
z = np.random.normal(0, 1, 5)  # 정규분포
print(z)

# q = np.arange(1, 6)
# choice = np.random.choice(q, 3)
# print(choice)

q = np.array(["가위", "바위", "보"])
choice = np.random.choice(q, 2)
print(choice)