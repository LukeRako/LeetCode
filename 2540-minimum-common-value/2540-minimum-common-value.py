class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        lowest = float('inf')

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                lowest = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return lowest if lowest != float('inf') else -1


        # my solution, meh

        # lowest = float('inf')
        # nums1N = set(nums1)
        # nums2N = set(nums2)

        # for num in nums1N:
        #     if num in nums2N and num < lowest:
        #         lowest = num
        
        # return lowest if lowest != float('inf') else -1