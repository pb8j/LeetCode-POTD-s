class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cum_sum = odd = 0 
        even = 1 
        for num in arr:
            cum_sum += num
            if cum_sum % 2 == 1:
                odd += 1 
            else:
                even += 1 

        return odd * even % (pow(10, 9) + 7)