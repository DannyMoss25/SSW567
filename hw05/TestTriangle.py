# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(4, 3, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right')
        self.assertEqual(classifyTriangle(9, 41, 40), 'Right')
    def testScalene(self):
        self.assertEqual(classifyTriangle(5,4,2),'Scalene')
        self.assertEqual(classifyTriangle(8, 13, 9), 'Scalene')
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene')
    def testIsosceles(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isoceles')
        self.assertEqual(classifyTriangle(3, 5, 3), 'Isoceles')
        self.assertEqual(classifyTriangle(5, 3, 3), 'Isoceles')
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', '3,3,3 should be equilateral')
        #self.assertEqual(classifyTriangle(5.5, 5.5, 5.5), 'InvalidInput')
    def testNonInt(self):
        self.assertEqual(classifyTriangle("NOT INTEGER", "NOT NUMBER", "STRING"), 'InvalidInput')
        self.assertEqual(classifyTriangle(5.5, 5.5, 5.5), 'InvalidInput')
        self.assertEqual(classifyTriangle(None, 2, 2), 'InvalidInput')
        self.assertEqual(classifyTriangle(2, None, 2), 'InvalidInput')
        self.assertEqual(classifyTriangle(2, 2, None), 'InvalidInput')
        self.assertEqual(classifyTriangle(["Art", "History", "Science"], 2, 2), 'InvalidInput')
    def testZero(self):
        self.assertEqual(classifyTriangle(0, 5, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle(5, 0, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle(5, 5, 0), 'InvalidInput')
    def testTooLarge(self):
        self.assertEqual(classifyTriangle(10000, 2, 2), 'InvalidInput')
    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(100, 1, 1), 'NotATriangle')
        self.assertEqual(classifyTriangle(1, 100, 1), 'NotATriangle')
        self.assertEqual(classifyTriangle(1, 1, 100), 'NotATriangle')
    def testPositive(self):
        self.assertEqual(classifyTriangle(-3, 3, 3), 'InvalidInput')
        self.assertEqual(classifyTriangle(3, -3, 3), 'InvalidInput')
        self.assertEqual(classifyTriangle(3, 3, -3), 'InvalidInput')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

