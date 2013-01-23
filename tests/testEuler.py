import unittest
import euler
import itertools

class testBigRange(unittest.TestCase):
    def testSmallRangeDefaultStep(self):
        expected = list(range(0, 10))
        actual = list(euler.bigRange(0, 10))
        self.assertItemsEqual(expected, actual)

    def testSmallRangeNonDefaultStep(self):
        expected = list(range(2, 10, 3))
        actual = list(euler.bigRange(2, 10, 3))
        self.assertItemsEqual(expected, actual)

    def testBigRangeDefaultStep(self):
        expected = [1000000000000, 1000000000001, 1000000000002]
        actual = list(euler.bigRange(1000000000000, 1000000000003))
        self.assertItemsEqual(expected, actual)

    def testBigRangeNonDefaultStep(self):
        expected = [1000000000000, 1000000000002, 1000000000004, 1000000000006]
        actual = list(euler.bigRange(1000000000000, 1000000000008, 2))
        self.assertItemsEqual(expected, actual)

class testReverseBigRange(unittest.TestCase):
    def testSmallRangeDefaultStep(self):
        expected = list(range(10, 0, -1))
        actual = list(euler.reverseBigRange(10, 0))
        self.assertItemsEqual(expected, actual)

    def testSmallRangeNonDefaultStep(self):
        expected = list(range(10, 2, -3))
        actual = list(euler.reverseBigRange(10, 2, 3))
        self.assertItemsEqual(expected, actual)

    def testBigRangeDefaultStep(self):
        expected = [1000000000003, 1000000000002, 1000000000001]
        actual = list(euler.reverseBigRange(1000000000003, 1000000000000))
        self.assertItemsEqual(expected, actual)

    def testBigRangeNonDefaultStep(self):
        expected = [1000000000006, 1000000000004, 1000000000002]
        actual = list(euler.reverseBigRange(1000000000006, 1000000000001, 2))
        self.assertItemsEqual(expected, actual)

class testFibonacci(unittest.TestCase):
    def testSuccess(self):
        expected = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        actual = itertools.islice(euler.fibonacci(), 10)
        self.assertItemsEqual(expected, actual)

class testGeneratePrimes(unittest.TestCase):
    def testDefaultStart(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        actual = itertools.islice(euler.generatePrimes(), 20)
        self.assertItemsEqual(expected, actual)

    def testNonDefaultStart(self):
        expected = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        actual = itertools.islice(euler.generatePrimes(4), 18)
        self.assertItemsEqual(expected, actual)

class testGetPrimesTo(unittest.TestCase):
    def testSuccess(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        actual = euler.getPrimesTo(25)
        self.assertItemsEqual(expected, actual)

class testGenerateTriangleNumbers(unittest.TestCase):
    def testSuccess(self):
        expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        actual = itertools.islice(euler.generateTriangleNumbers(), 10)
        self.assertItemsEqual(expected, actual)

class testIsTriangle(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isTriangle(2))
        self.assertFalse(euler.isTriangle(4))
        self.assertFalse(euler.isTriangle(24))
        self.assertFalse(euler.isTriangle(56))

    def testSuccess(self):
        self.assertTrue(euler.isTriangle(1))
        self.assertTrue(euler.isTriangle(3))
        self.assertTrue(euler.isTriangle(6))
        self.assertTrue(euler.isTriangle(10))
        self.assertTrue(euler.isTriangle(36))

class testGeneratePentagonalNumbers(unittest.TestCase):
    def testSuccess(self):
        expected = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        actual = itertools.islice(euler.generatePentagonalNumbers(), 10)
        self.assertItemsEqual(expected, actual)

class testIsPentagonal(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isPentagonal(2))
        self.assertFalse(euler.isPentagonal(3))
        self.assertFalse(euler.isPentagonal(4))
        self.assertFalse(euler.isPentagonal(21))
        self.assertFalse(euler.isPentagonal(91))
        self.assertFalse(euler.isPentagonal(118))

    def testSuccess(self):
        self.assertTrue(euler.isPentagonal(1))
        self.assertTrue(euler.isPentagonal(5))
        self.assertTrue(euler.isPentagonal(12))
        self.assertTrue(euler.isPentagonal(22))
        self.assertTrue(euler.isPentagonal(92))
        self.assertTrue(euler.isPentagonal(145))

class generateHexagonalNumbers(unittest.TestCase):
    def testFailure(self):
        expected = [1, 6, 15, 28, 45, 66, 91, 120, 153, 190]
        actual = itertools.islice(euler.generateHexagonalNumbers(), 10)
        self.assertItemsEqual(expected, actual)

class testIsHexagonal(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isHexagonal(0))
        self.assertFalse(euler.isHexagonal(2))
        self.assertFalse(euler.isHexagonal(3))
        self.assertFalse(euler.isHexagonal(4))
        self.assertFalse(euler.isHexagonal(7))
        self.assertFalse(euler.isHexagonal(8))
        self.assertFalse(euler.isHexagonal(14))
        self.assertFalse(euler.isHexagonal(92))

    def testSuccess(self):
        self.assertTrue(euler.isHexagonal(1))
        self.assertTrue(euler.isHexagonal(6))
        self.assertTrue(euler.isHexagonal(15))
        self.assertTrue(euler.isHexagonal(28))
        self.assertTrue(euler.isHexagonal(45))
        self.assertTrue(euler.isHexagonal(190))

class testGetIterativeSequence(unittest.TestCase):
    def testStartingOnEven(self):
        expected = [50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        actual = euler.getIterativeSequence(50)
        self.assertItemsEqual(expected, actual)

    def testStartingOnOdd(self):
        expected = [39, 118, 59, 178, 89, 268, 134, 67, 202, 101, 304, 152, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        actual = euler.getIterativeSequence(39)
        self.assertItemsEqual(expected, actual)

    def testStartingOnZero(self):
        expected = [0]
        actual = euler.getIterativeSequence(0)
        self.assertItemsEqual(expected, actual)

    def testStartingNegative(self):
        expected = [-33]
        actual = euler.getIterativeSequence(-33)
        self.assertItemsEqual(expected, actual)

class testIsEven(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isEven(1))
        self.assertFalse(euler.isEven(3))
        self.assertFalse(euler.isEven(5))
        self.assertFalse(euler.isEven(99))
        self.assertFalse(euler.isEven(1344323))

    def testSuccess(self):
        self.assertTrue(euler.isEven(2))
        self.assertTrue(euler.isEven(4))
        self.assertTrue(euler.isEven(998))
        self.assertTrue(euler.isEven(1024))

class testIsOdd(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isOdd(0))
        self.assertFalse(euler.isOdd(2))
        self.assertFalse(euler.isOdd(4))
        self.assertFalse(euler.isOdd(6))
        self.assertFalse(euler.isOdd(346656))
        self.assertFalse(euler.isOdd(3456))

    def testSuccess(self):
        self.assertTrue(euler.isOdd(1))
        self.assertTrue(euler.isOdd(3))
        self.assertTrue(euler.isOdd(5))
        self.assertTrue(euler.isOdd(99))
        self.assertTrue(euler.isOdd(12343))
        self.assertTrue(euler.isOdd(141))
        self.assertTrue(euler.isOdd(3447))

class testIsPrime(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isPrime(0))
        self.assertFalse(euler.isPrime(1))
        self.assertFalse(euler.isPrime(4))
        self.assertFalse(euler.isPrime(9))
        self.assertFalse(euler.isPrime(15))

    def testSuccess(self):
        self.assertTrue(euler.isPrime(2))
        self.assertTrue(euler.isPrime(3))
        self.assertTrue(euler.isPrime(5))
        self.assertTrue(euler.isPrime(7))
        self.assertTrue(euler.isPrime(17))
        self.assertTrue(euler.isPrime(617))

class testIsPandigital(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isPandigital(0))
        self.assertFalse(euler.isPandigital(2))
        self.assertFalse(euler.isPandigital(-1))
        self.assertFalse(euler.isPandigital(11))
        self.assertFalse(euler.isPandigital(13))
        self.assertFalse(euler.isPandigital((3988)))
        self.assertFalse(euler.isPandigital(535))

    def testSuccess(self):
        self.assertTrue(euler.isPandigital(1))
        self.assertTrue(euler.isPandigital(12))
        self.assertTrue(euler.isPandigital(213))
        self.assertTrue(euler.isPandigital(321))
        self.assertTrue(euler.isPandigital(4312))
        self.assertTrue(euler.isPandigital(7456321))
        self.assertTrue(euler.isPandigital(987561243))

class testIsPerfect(unittest.TestCase):
    def testFailure(self):
        self.assertFalse(euler.isPerfect(1))
        self.assertFalse(euler.isPerfect(2))
        self.assertFalse(euler.isPerfect(3))
        self.assertFalse(euler.isPerfect(4))
        self.assertFalse(euler.isPerfect(5))
        self.assertFalse(euler.isPerfect(7))
        self.assertFalse(euler.isPerfect(8))
        self.assertFalse(euler.isPerfect(30))
        self.assertFalse(euler.isPerfect(235))
        self.assertFalse(euler.isPerfect(9888))

    def testSuccess(self):
        self.assertTrue(euler.isPerfect(6))
        self.assertTrue(euler.isPerfect(28))
        self.assertTrue(euler.isPerfect(496))
        self.assertTrue(euler.isPerfect(8128))