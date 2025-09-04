import numpy as np

# arr = np.array(["Korean", "English", "Mathmatics"])
# arr = np.array([[1, 2, 3],[4, 5, 9]])
arr = np.array(
    [
        [
            [1.0, 2.0, 3.1],
            [4.2, 5.9, 9.1]
        ],
        [
            [1.1, 0.8, 2.1],
            [6.3, 1.9, 77.1]
        ]
    ]
)
print(arr)
print(arr.shape, arr.dtype, arr.ndim, arr.size)
# 위 3차원 배열에서 1.9만 출력
print(arr[1][1][1])
print(arr[1, 1, 1])
