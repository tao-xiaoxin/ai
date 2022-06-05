import numpy as np


def oneId(matrix):  # 获取1的坐标
    oneid = []
    matrix = matrix
    print(matrix)
    height, width = len(matrix), len(matrix[0])
    for rowid, row in enumerate(matrix):
        for colid, num in enumerate(row):
            if num == 1:
                oneid.append([rowid, colid])
                # print([rowid,colid])
    return oneid


def recTangle(seed):  # 以种子为左上角，搜索最大矩形
    h, w = 1, 1
    p = [seed[0], seed[1]]
    while p[1] + 1 <= len(matrix[0]) - 1 and matrix[p[0], p[1] + 1] == 1:
        w += 1
        p[1] += 1
    q = [seed[0], seed[1]]
    while q[0] + 1 <= len(matrix) - 1 and matrix[q[0] + 1, q[1]] == 1:
        h += 1
        q[0] += 1
    while ((matrix[seed[0]:seed[0] + h, seed[1]:seed[1] + w]) == 0).any():
        if h >= w:
            h -= 1
        if h < w:
            w -= 1
    square = matrix[seed[0]:seed[0] + h, seed[1]:seed[1] + w]
    # print(h, w, '\n', square)
    # print((square == 1).all())
    # print("--" * 30)
    return w * h


matrix = np.random.randint(0, 2, size=(10, 10))
# print([seed for seed in oneId(matrix)])
oneid = oneId(matrix)
maxarea = 0
for seed in oneid:
    area = recTangle(seed)
    if area > maxarea:
        maxarea = area

print(maxarea)
