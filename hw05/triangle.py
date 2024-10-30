"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
import unittest


def classify_triangle( aaa , bbb, ccc):
    """
    Your correct code goes here...  Fix the faulty logic
    below until the code passes all of you test cases.
    This function returns a string with the type of triangle
    from three integer values corresponding to the lengths
    of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if not (isinstance(aaa, int) and isinstance(bbb, int) and isinstance(ccc, int)):
        return 'InvalidInput'
    if bbb > ccc:
        ccc,bbb = bbb,ccc
    if aaa > bbb:
        bbb,aaa = aaa,bbb
        if bbb > ccc:
            ccc,bbb = bbb,ccc
    if aaa <= 0 or bbb <= 0 or ccc <= 0:
        return 'InvalidInput'
    # verify that all 3 inputs are integers  -
    # Python's "isinstance(object,type) returns True if the
    # object is of the specified type
    if aaa > 200 or bbb > 200 or ccc > 200:
        return 'InvalidInput'
    # This information was not in the requirements spec but  is
    # important for correctness the sum of any two sides must be
    # strictly less than the third side
    # of the specified shape is not a triangle
    if aaa + bbb <= ccc:
        return 'NotATriangle'
    # now we know that we have a valid triangle
    what_to_return = "Nothing"
    if aaa == bbb and aaa == ccc:
        what_to_return= 'Equilateral'
    elif ((aaa ** 2) + (bbb ** 2)) == (ccc ** 2):
        what_to_return= 'Right'
    elif bbb not in (aaa, ccc):
        what_to_return= 'Scalene'
    else:
        what_to_return= 'Isoceles'
    return what_to_return







class TestTriangles(unittest.TestCase):
    """This is the test class"""
    # define multiple sets of tests as functions with names that begin
    def test_right_triangle(self):
        """Test for Right Triangle"""
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(4, 3, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 4, 3), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(4, 5, 3), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(8, 15, 17), 'Right')
        self.assertEqual(classify_triangle(9, 41, 40), 'Right')
    def test_scalene(self):
        """Test for Scalene"""
        self.assertEqual(classify_triangle(5,4,2),'Scalene')
        self.assertEqual(classify_triangle(8, 13, 9), 'Scalene')
        self.assertEqual(classify_triangle(4, 2, 3), 'Scalene')
    def test_isosceles(self):
        """Test for Isosceles"""
        self.assertEqual(classify_triangle(3, 3, 5), 'Isoceles')
        self.assertEqual(classify_triangle(3, 5, 3), 'Isoceles')
        self.assertEqual(classify_triangle(5, 3, 3), 'Isoceles')
    def test_equilateral_triangles(self):
        """Test for Equilateral"""
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral', '3,3,3 should be equilateral')
        #self.assertEqual(classifyTriangle(5.5, 5.5, 5.5), 'InvalidInput')
    def test_non_int(self):
        """Makes every parameter is a integer"""
        self.assertEqual(classify_triangle("NOT INTEGER", "NOT NUMBER", "STRING"), 'InvalidInput')
        self.assertEqual(classify_triangle(5.5, 5.5, 5.5), 'InvalidInput')
        self.assertEqual(classify_triangle(None, 2, 2), 'InvalidInput')
        self.assertEqual(classify_triangle(2, None, 2), 'InvalidInput')
        self.assertEqual(classify_triangle(2, 2, None), 'InvalidInput')
        self.assertEqual(classify_triangle(["Art", "History", "Science"], 2, 2), 'InvalidInput')
    def test_zero(self):
        """Makes sure there are no zero values"""
        self.assertEqual(classify_triangle(0, 5, 5), 'InvalidInput')
        self.assertEqual(classify_triangle(5, 0, 5), 'InvalidInput')
        self.assertEqual(classify_triangle(5, 5, 0), 'InvalidInput')
    def test_too_large(self):
        """Makes sure it's not too large"""
        self.assertEqual(classify_triangle(10000, 2, 2), 'InvalidInput')
    def test_not_triangle(self):
        """Makes sure its a triangle"""
        self.assertEqual(classify_triangle(100, 1, 1), 'NotATriangle')
        self.assertEqual(classify_triangle(1, 100, 1), 'NotATriangle')
        self.assertEqual(classify_triangle(1, 1, 100), 'NotATriangle')
    def test_positive(self):
        """Makes sure it's positive"""
        self.assertEqual(classify_triangle(-3, 3, 3), 'InvalidInput')
        self.assertEqual(classify_triangle(3, -3, 3), 'InvalidInput')
        self.assertEqual(classify_triangle(3, 3, -3), 'InvalidInput')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
