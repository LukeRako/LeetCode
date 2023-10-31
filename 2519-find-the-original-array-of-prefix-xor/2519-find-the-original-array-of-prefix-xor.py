class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = pref[0]

        for i in range(1, len(pref)):
            pref[i] ^= arr
            arr ^= pref[i]

        return pref
        