import unittest

def classify_triangle(a,b,c):
    endMessage = ""

    if (str(type(a)) == "<class 'str'>"):
        return "STRING VALUE"
    if (str(type(b)) == "<class 'str'>"):
        return "STRING VALUE"
    if (str(type(c)) == "<class 'str'>"):
        return "STRING VALUE"

    if(a == 0 or b == 0 or c == 0):
        return "ZERO VALUE"

    if (a < 0 or b < 0 or c < 0):
        return "ONLY POSITIVE NUMBERS ACCEPTED"

    if(a == b and b == c):
        endMessage += "equilateral"
    elif(a == b or b == c or a == c):
        endMessage += "isosceles"
    else:
        endMessage += "scalene"

    c = round(c * c, 3)
    a = round(a * a, 3)
    b = round(b * b, 3)

    if(a + b == c  or c  + b == a  or a  + c  == b ):
        endMessage += ", Right Triange"

    return endMessage


class TestStringMethods(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual("equilateral", classify_triangle(3, 3, 3))
        self.assertEqual("equilateral", classify_triangle(5.5, 5.5, 5.5))

    def test_isosceles(self):
        self.assertEqual("isosceles", classify_triangle(3, 3, 5))
        self.assertEqual("isosceles", classify_triangle(3, 5, 3))
        self.assertEqual("isosceles", classify_triangle(5, 3, 3))

    def test_scalene(self):
        self.assertEqual("scalene", classify_triangle(5, 3, 8))
        self.assertEqual("scalene", classify_triangle(3, 4, 9))
        self.assertEqual("scalene", classify_triangle(5, 3, 8))

    def test_scaleneRight(self):
        self.assertEqual("scalene, Right Triange", classify_triangle(3,4,5))
        self.assertEqual("scalene, Right Triange", classify_triangle(3, 5, 4))
        self.assertEqual("scalene, Right Triange", classify_triangle(4, 5, 3))
        self.assertEqual("scalene, Right Triange", classify_triangle(8, 15, 17))
        self.assertEqual("scalene, Right Triange", classify_triangle(9, 41, 40))

    def test_isoscelesRight(self):
        self.assertEqual("isosceles, Right Triange", classify_triangle(2, 2, (2 ** 0.5) * 2))
        self.assertEqual("isosceles, Right Triange", classify_triangle(8, 8, (2 ** 0.5) * 8))

    def test_stringVal(self):
        self.assertEqual(str("STRING VALUE"), str(classify_triangle("B", 2, 8)))
        self.assertEqual(str("STRING VALUE"), str(classify_triangle(5, "B", 8)))
        self.assertEqual(str("STRING VALUE"), str(classify_triangle(3, 2, "C")))

    def test_zeroVal(self):
        self.assertEqual("ZERO VALUE", classify_triangle(0, 4, 5))
        self.assertEqual("ZERO VALUE", classify_triangle(3, 0, 5))
        self.assertEqual("ZERO VALUE", classify_triangle(3, 4, 0))

    def test_Positive(self):
        self.assertEqual("ONLY POSITIVE NUMBERS ACCEPTED", classify_triangle(-3, 4, 5))
        self.assertEqual("ONLY POSITIVE NUMBERS ACCEPTED", classify_triangle(3, -4, 5))
        self.assertEqual("ONLY POSITIVE NUMBERS ACCEPTED", classify_triangle(3, 4, -5))

    def test_wrong(self):
        self.assertNotEqual("isosceles, Right Triange", classify_triangle(2, 2, 8))
        self.assertNotEqual("scalene", classify_triangle(3, 3, 1))



if __name__ == '__main__':
    unittest.main()
