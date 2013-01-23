# library of functions for Project Euler problems
from math import sqrt, factorial

# a range that works for long values
def bigRange(start, stop, step=1):
    x = start
    while x < stop:
        yield x
        x = x + step

# a fast reverse range that works for long values
def reverseBigRange(start, stop=0, step=1):
    x = start
    while x > stop:
        yield x
        x = x - step

# a Fibonacci sequence generator
def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

# a generator for prime numbers, keeps going until you stop pulling
def generatePrimes(start=2):
    current = start
    if current == 2 or isPrime(current):
        yield current # 2
    current += 1
    yield current # 3
    while 1:
        current += 2 # ignore even numbers
        if isPrime(current):
            yield current

# a prime number sieve using the Eratostenes algorithm
def getPrimesTo(n):
    primes = set(xrange(3, n, 2))
    primes.add(2)
    for p in xrange(3, n / 2, 2):
        if p in primes:
            for multiple in getMultiplesTo(p, n):
                primes.discard(multiple)
    return primes

# a generator for triangle numbers
# 1, +=2, +=3, += 4, etc...
# 1, 3, 6, 10, 15, etc...
def generateTriangleNumbers():
    current = 1
    triangle = 0
    while True:
        triangle += current
        current += 1
        yield triangle

# determines if x is a triangle number
def isTriangle(x):
    n = (sqrt(8 * x + 1) - 1) / 2.0
    return n == int(n)

# a generator for pentagonal numbers
# Pn = (n(3n-1))/2
# 1,5,12,22,35,51,70,...
def generatePentagonalNumbers():
    n = 1
    while True:
        pentagonal = (n * (3 * n - 1)) / 2
        yield pentagonal
        n += 1

# determines if x is a pentagonal number
# Pn = (n(3n-1))/2
def isPentagonal(x):
    n = (sqrt(24 * x + 1) + 1) / 6.0
    return n == int(n)

# a generator for pentagonal numbers
# Hn = n(2n - 1)
# 1,6,15,28,45,...
def generateHexagonalNumbers():
    n = 1
    while True:
        hexagonal = n * (2 * n - 1)
        yield hexagonal
        n += 1

# determines if x is a hexagonal number
def isHexagonal(x):
    n = (sqrt(8 * x + 1) + 1) / 4.0
    return n == int(n)

# generates an iterative sequence starting at start
# n => n/2 (when n is even)
# n => 3n+1 (when n is odd)
def getIterativeSequence(start):
    current = start
    sequence = []
    while current > 1:
        sequence.append(current)
        if isEven(current): current /= 2
        else: current = 3 * current + 1
    sequence.append(current)

    return sequence

# filter for even numbers
def isEven(x):
    return x % 2 == 0

# filter for odd numbers
def isOdd(x):
    return not isEven(x)

# filter for prime numbers
def isPrime(n):
    # shortcuts
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 5 and n % 5 == 0:
        return False

    for x in bigRange(3, sqrt(n) + 1):
        if n % x == 0:
            return False
    return True

# checks if a number (n) is pandigital
def isPandigital(n):
    if n < 0 : return False
    set_n = set(int(x) for x in str(n))
    if len(set_n) != len(str(n)): return False
    c = len(set_n)
    for digit in xrange(1, c + 1):
        if digit not in set_n: return False
    return True

# determines if a number is perfect (equals the sum of its proper divisors)
def isPerfect(n):
    return sum(getProperDivisors(n)) == n

# determines if a number is deficient (sum of proper divisors < number)
def isDeficient(n):
    return sum(getProperDivisors(n)) < n


def isPalindromic(n):
    n_str = str(n)
    return n_str == n_str[::-1]

# determines if a number is abundant (sum of proper divisors > number)
def isAbundant(n):
    return sum(getProperDivisors(n)) > n

# gets factors for a number
# this can be improved via prime factorization
def getFactors(n):
    factors = []
    for x in bigRange(1, (n / 2) + 1):
        if n % x == 0:
            factors.append(x)
    factors.append(n)
    return factors

# gets factors for a number using prime factorization
def getFactorsFast(n):
    factors = {1}
    if n == 1: return factors
    prime_factors = getPrimeFactors(n)
    for prime_factor in prime_factors:
        new_factors = set([])
        if prime_factor not in factors: new_factors.add(prime_factor)
        for factor in factors:
            new_factor = factor * prime_factor
            if new_factor not in factors and new_factor not in new_factors:
                new_factors.add(new_factor)
        factors = factors.union(new_factors)
    return factors

# gets the proper divisors for the specified number
def getProperDivisors(n):
    proper_divisors = getFactorsFast(n)
    proper_divisors.discard(n)
    return proper_divisors

# gets the multiples of n to to
def getMultiplesTo(n, to):
    multiple = n + n
    while multiple < to:
        yield multiple
        multiple += n

# gets the prime factors for a number in a list
# the list will look like 528 => [2, 2, 2, 2, 3, 11]
def getPrimeFactors(n):
    primeFactors = []
    current = n
    while not isPrime(current):
        for prime in generatePrimes():
            if current % prime == 0:
                primeFactors.append(prime)
                current /= prime
                break
    primeFactors.append(current)

    return primeFactors

# gets the prime factors for a number in a dictionary
# where the key is the number and the value is the exponent
# 528 => { 2: 4, 3: 1, 11: 1 }
def getPrimeFactorsDictionary(n):
    primeFactors = {}
    current = n
    while not isPrime(current):
        for prime in generatePrimes():
            if current % prime == 0:
                if prime in primeFactors: primeFactors[prime] += 1
                else: primeFactors[prime] = 1
                current /= prime
                break
    if current in primeFactors: primeFactors[current] += 1
    else: primeFactors[current] = 1

    return primeFactors

# gets the number of factors
# using prime factorization and taking the product
# of 1+each_exponent.
def getFactorCount(n):
    primeFactors = getPrimeFactorsDictionary(n)
    factor_count = 1
    for value in primeFactors.values():
        factor_count *= (value + 1)
    return factor_count

# returns the sum of numbers from 1 to n
# 1+2+...+n
def sumTo(n):
    return (n ** 2 + n) / 2

# returns the sum of the squares from 1 to n
# 1**2+2**2+...+n**2
def sumOfSquaresTo(n):
    return int(n ** 3 / 3.0 + n ** 2 / 2.0 + n / 6.0)

# gets the number of combinations of size k
# from a group of size n
def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
