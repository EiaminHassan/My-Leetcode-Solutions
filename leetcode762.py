class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        # In LeetCode constraints for this problem, right <= 10^6,
        # so max set bits <= 20. We'll sieve primes up to 32 safely.
        MAX_BITS = 32

        is_prime = [True] * (MAX_BITS + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX_BITS ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_BITS + 1, i):
                    is_prime[j] = False

        ans = 0
        for x in range(left, right + 1):
            # popcount (number of 1 bits)
            cnt = bin(x).count("1")
            if is_prime[cnt]:
                ans += 1

        return ans