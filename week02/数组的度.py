# 数组的度
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        # 统计每个字符出现的次数
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        count = max(dic.values())  # 数组的度
        res = []
        # 找出所有出现次数等于度的值
        for k, v in dic.items():
            if v == count:
                res.append(k)
        mmin = 100000
        for i in res:
            x = len(nums) - nums.index(i) - nums[::-1].index(i)
            if x < mmin:
                mmin = x
        return mmin
