# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:20:33 2019

@author: maria
"""

import unittest
from functionalities import *

class TestFunctionalities(unittest.TestCase):      
    def test_getdb(self):
        self.assertTrue(getdb("mariana"))
        #self.assertTrue(is_prime(sys.argv[0]))
    def test_findBusinessType(self):
        self

if __name__=="__main__":
    unittest.main()
