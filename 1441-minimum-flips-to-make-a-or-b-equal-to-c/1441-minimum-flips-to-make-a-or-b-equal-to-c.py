class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # check each bit and see if needs to be flipped
        flips = 0

        while a > 0 or b > 0 or c > 0:

            bitA = a & 1
            bitB = b & 1
            bitC = c & 1

            if bitC == 0:
                flips += (bitA + bitB)

            else:
                if bitA == 0 and bitB == 0:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1
            
        return flips
