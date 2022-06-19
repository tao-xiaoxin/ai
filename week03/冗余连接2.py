class UnionFind:
    """并查集
    """

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        self.parent[x_root] = y_root
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def is_circle(edges, n, idx):
            # 判断去除边是否存在环
            uf = UnionFind(n + 1)
            for i in range(n):
                # 去除边
                if i == idx:
                    continue
                if not uf.union(edges[i][0], edges[i][1]):
                    # 存在环
                    return True

            return False

        n = len(edges)
        # 记录入度情况
        indegree = [0 for _ in range(n + 1)]
        for edge in edges:
            indegree[edge[1]] += 1

        # 考虑入度 2 的情况
        # 题目要求重复返回最后出现的答案，
        # 这里直接逆序遍历
        for i in range(n - 1, -1, -1):
            if indegree[edges[i][1]] == 2:
                # 判断去除边是否存在环
                if not is_circle(edges, n, i):
                    return edges[i]

        # 入度 1，存在环，尝试去除某一边
        for i in range(n - 1, -1, -1):
            if indegree[edges[i][1]] == 1:
                # 判断去除边是否存在环
                if not is_circle(edges, n, i):
                    return edges[i]