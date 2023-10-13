class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        
        
        # checked = set(nums)
        # longest = 0

        # for num in nums:
        #     if (num - 1) not in checked:
        #         seqLen = 0
        #         while (num + seqLen) in checked:
        #             seqLen += 1
        #         longest = max(longest, seqLen)
        # return longest
        