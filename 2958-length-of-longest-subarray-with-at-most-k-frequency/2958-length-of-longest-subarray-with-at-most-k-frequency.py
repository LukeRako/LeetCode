class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window
        res = 0
        count = defaultdict(int) # default 0 if none exist, increments otherwise

        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res