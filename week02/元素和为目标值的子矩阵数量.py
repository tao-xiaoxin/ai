# 元素和为目标值的子矩阵数量
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]],
                              target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        colsm = [[0] * cols for r in range(rows)]
        for c in range(cols):
            cur = 0
            for r in range(rows):
                cur += matrix[r][c]
                colsm[r][c] = cur
        res = 0
        for sr in range(rows):
            for er in range(sr, rows):
                d = collections.defaultdict(int)
                cur = 0
                for c in range(cols):
                    # 注意此处减去的是colsm[sr - 1][c], 因为要把起点行sr统计在内
                    pre = 0 if sr - 1 < 0 else colsm[sr - 1][c]
                    cur += colsm[er][c] - pre
                    if cur == target:
                        # cur本身就是target的特殊情况
                        res += 1
                    res += d[cur - target]
                    d[cur] += 1
        return res
