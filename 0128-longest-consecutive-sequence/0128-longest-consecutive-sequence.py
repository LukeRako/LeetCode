class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checked = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in checked:
                seqLen = 0
                while (num + seqLen) in checked:
                    seqLen += 1
                longest = max(longest, seqLen)

        return longest
        