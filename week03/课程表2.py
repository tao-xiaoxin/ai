class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        res = []
        next_node = defaultdict(list)
        InDegree = defaultdict(int)
        for node in prerequisites:
            next_node[node[1]].append(node[0])
            InDegree[node[0]] += 1
        start = 0
        finish = 0
        while start < numCourses:
            if InDegree[start] == 0:
                for node in next_node[start]:
                    InDegree[node] -= 1
                res.append(start)
                InDegree[start] = -1
                start = 0
                finish += 1
                continue
            if finish == numCourses:
                return res
            start += 1
        return []
