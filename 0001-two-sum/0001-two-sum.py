class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dict={}
        for i in range(n):
            if target-nums[i] in dict:
                return [i,dict[target-nums[i]]]
            else:
                dict[nums[i]]=i

