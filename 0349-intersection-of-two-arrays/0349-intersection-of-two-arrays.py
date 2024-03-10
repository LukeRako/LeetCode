class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set1.intersection(set2))

        # my solution
        ans = []

        for num in nums1:
            if num in nums2:
                ans.append(num)

        return set(ans)