class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window
        product = 1
        l, result = 0, 0
        
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            result += r - l + 1

        return result