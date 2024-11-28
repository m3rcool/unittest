import math
import unittest

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

print(area(3))

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_area_three(self):
        res = area(3)
        self.assertEqual(res, 28.274333882308138)
    def test_area_hun(self):
        res = area(100)
        self.assertEqual(res, 31415.926535897932)
    def test_per_zero(self):
        res =  perimeter(0)
        self.assertEqual(res, 0)
    def test_per_fifhteen(self):
        res = perimeter(15)
        self.assertEqual(res, 94.24777960769379)
    def test_per_hun(self):
        res = perimeter(100)
        self.assertEqual(res, 628.3185307179587)
