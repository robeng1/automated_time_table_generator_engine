#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann

import unittest
from classroom import  Classroom
#import classroom
# TODO: write tests for the section class


class TestSection(unittest.TestCase):
    def setUp(self):
        self.room1 = Classroom("PB001", 120)
        self.room2 = Classroom("A110",100)

    def test_name(self):
        self.assertEqual(self.room1.name,'PB001')
        self.assertEqual(self.room2.name,'A110')
        
    def test_capacity(self):
        self.assertEqual(self.room1.capacity,120)
        self.assertEqual(self.room2.capacity,100)
    
    def test_can_accomodate(self):
        self.assertEqual(self.room1.can_accommodate(120), True)
        self.assertEqual(self.room1.can_accommodate(130), False)
        self.assertEqual(self.room1.can_accommodate(130, 10), True)
    
    def test___eq__(self):
        self.assertEqual((self.room1==self.room2),False)
        self.assertEqual((self.room1 == self.room1),True)
        self.assertEqual((self.room1=='room1'),False)

    def test___ne__(self):
        self.assertEqual((self.room1!=self.room2),True)
        self.assertEqual((self.room1 != self.room1),False)
        self.assertEqual((self.room1 !='room1'),True)
if __name__  ==  '__main__':
    unittest.main()