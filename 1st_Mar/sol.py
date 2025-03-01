class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] =0
        n = len(nums)
        res = [x for x in nums if x!= 0]
        z = n-len(res)
        res.extend([0]*z)
        return res