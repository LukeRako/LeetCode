class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one, zero = 0, 0
        res = 0
        diff = {}

        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
            else:
                one += 1
                
            if one - zero not in diff:
                diff[one-zero] = i

            if one - zero == 0:
                res = zero + one
            else:
                idx = diff[one - zero]
                res = max(res, i - idx)

        return res

            
        