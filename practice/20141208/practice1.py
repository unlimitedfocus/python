import os

print os.getcwd()
print dir(os)

import glob
print glob.glob('*.py')

import sys
print sys.argv

import re
print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

import urllib2

"""
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:
        print line
"""

html = urllib2.urlopen('http://www.clien.net/cs2/bbs/board.php?bo_table=park')
"""
for line in html:
    print line
"""

from datetime import date
now = date.today()
print now


from timeit import Timer

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

import doctest
doctest.testmod()

"""
import unittest
class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


unittest.main()
"""
