class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else: 
                frequency[num] = 1

        maxFreq = max(frequency.values())
        maxRet = 0

        for f in frequency.values():
            if f == maxFreq:
                maxRet += f
    
        return maxRet