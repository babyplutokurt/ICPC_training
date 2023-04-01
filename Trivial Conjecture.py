from math import sqrt


class Solution:
    def __init__(self):
        pass

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        numbers = [0, 0] + [1] * (n - 2)
        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                # Set all multiples of p to false because they are not prime.
                for multiple in range(p * p, n, p):
                    numbers[multiple] = 0
        return sum(numbers)


a = Solution()
b = 4167792762229302596005813
print(a.countPrimes(b))