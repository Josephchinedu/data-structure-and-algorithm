class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
         
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for multiple_of_i in range(i * i, n, i):
                    isPrime[multiple_of_i] = False
        return sum(isPrime)


if __name__ == '__main__':
    n = 10
    print(Solution().countPrimes(n))