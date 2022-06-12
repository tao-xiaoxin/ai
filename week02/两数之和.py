class Solution:
    def twoSum(self,nums,target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return None
                if nums[i]+nums[j] == target:
                    return [i,j]

if __name__=="__main__":
    solution=Solution()
    print(solution.twoSum([2,7,11,15],9))

