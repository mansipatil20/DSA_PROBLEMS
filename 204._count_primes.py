class Solution:
    def countPrimes(self, n: int) -> int:
        if n <3:
            return 0

        primes = [True] * (n)
        primes[0] = primes[1]  = False
        for i in range(2,(n//2)+1):
            if primes[i]:
                for digit in range(i*i, n,i):
                    primes[digit] = False
        total_prime = primes.count(True)
        return total_prime