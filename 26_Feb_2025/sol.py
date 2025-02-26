class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre, max_pre = 0,0
        cur, res = 0,0

        for num in nums:
            cur += num
            res = max(res , abs(cur - min_pre) , abs(cur - max_pre))
            min_pre = min(cur , min_pre)
            max_pre = max(cur , max_pre)
        return res