class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_key(num):
            count = 0
            for b in bin(num)[2:]:
                if b == '1':
                    count += 1
            return (count, num)
        
        arr.sort(key=get_key)
        return arr
