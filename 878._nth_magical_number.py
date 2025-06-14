import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:

        def find_count(mid):
            lcm_ab = (a*b)//math.gcd(a,b)
            return mid//a + mid//b - mid//lcm_ab


        start, end = 0, 10**16
        while start < end:
            mid = (start + end) //2
            if find_count(mid) < n:
                start = mid +1
            else:
                end = mid
        return start % (10**9 + 7)