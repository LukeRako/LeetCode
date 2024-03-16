class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # count = {0 : 1}
        # curr_sum = 0
        # total_subs = 0

        # for num in nums:
        #     curr_sum += num
        #     if (curr_sum - goal) in count:
        #         total_subs += count[curr_sum - goal]
        #     count[curr_sum] = count.get(curr_sum, 0) + 1
        
        # return total_subs

        # neetcode solution, makes a lot more sense than previous imo
        def helper(x):
            if x < 0: return 0

            left, res = 0, 0
            current = 0

            for right in range(len(nums)):
                current += nums[right]

                while current > x:
                    current -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        return helper(goal) - helper(goal - 1)
