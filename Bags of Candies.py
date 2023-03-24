from math import sqrt

Turn = int(input())


def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 1
    numbers = [0, 0] + [1] * (n - 2)
    for p in range(2, int(sqrt(n)) + 1):
        if numbers[p]:
            # Set all multiples of p to false because they are not prime.
            for multiple in range(p * p, n, p):
                numbers[multiple] = 0

    return sum(numbers)


def half_prime(n):
    return countPrimes(n) - countPrimes(int(n // 2))


for i in range(Turn):
    nums = int(input())

    remaining_prime = half_prime(nums)
    # print("remaining_prime: ", remaining_prime)
    '''
    if nums % 3 == 0 and nums - 1 % 5 == 0:
        pair = (nums - remaining_prime - 3) // 2 + remaining_prime + 3
        # print(1)
    elif (nums - remaining_prime - 1) % 2 == 0:
        pair = (nums - remaining_prime - 1) // 2 + remaining_prime + 1
        # print(2)
    else:
        pair = (nums - remaining_prime - 1) // 2 + remaining_prime + 2
    # print(3)
    '''
    if (nums - remaining_prime) % 2 == 1:
        print((remaining_prime + int((nums - remaining_prime) / 2)) + 2)
    print((remaining_prime + int((nums - remaining_prime) / 2)) + 1)

"""
    1 28 39 46 510 7   14 1122 1215 13 1618 17 19 20 21 23  
41 - 6 18 + 6 = 24
    1 24 3
"""
