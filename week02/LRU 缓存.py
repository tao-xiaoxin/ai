class LRUcache:
    def __init__(self, cap):
        self.cap = cap  # 缓存容量
        self.cache = {}  # 缓存任务

    def get(self, key):
        '''
        获取键对应的值
        :param key:
        :return:
        '''
        if not key in self.cache.keys():
            return -1
        # 将key变为最近使用, 并返回值
        self.makeRecently(key)
        return self.cache[key]

    def put(self, k, v):
        '''
        将键值对任务添加进缓存
        :param k:
        :param v:
        :return:
        '''
        if k in self.cache.keys():
            self.cache[k] = v
            # 将key变为最近使用, 并返回值
            self.makeRecently(k)
            return 0
        if len(self.cache) >= self.cap:
            # 移除字典第一个
            first = list(self.cache.keys())
            self.cache.pop(first[0])
        self.cache[k] = v

    def makeRecently(self, key):
        value = self.cache.pop(key)
        self.cache[key] = value


# 测试
cache = LRUcache(2)
print(cache.put(1, 1), cache.cache)  # None {1: 1}
print(cache.put(2, 2), cache.cache)  # None {1: 1, 2: 2}
print(cache.get(1), cache.cache)  # 1 {2: 2, 1: 1}
print(cache.put(3, 3), cache.cache)  # None {1: 1, 3: 3}
print(cache.get(2), cache.cache)  # -1 {1: 1, 3: 3}
print(cache.put(4, 4), cache.cache)  # None {3: 3, 4: 4}
print(cache.get(1), cache.cache)  # -1 {3: 3, 4: 4}
print(cache.get(3), cache.cache)  # 3 {4: 4, 3: 3}
print(cache.get(4), cache.cache)  # 4 {3: 3, 4: 4}
