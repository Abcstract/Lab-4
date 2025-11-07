import sys
import unittest
from typing import *
from dataclasses import dataclass
import math

sys.setrecursionlimit(10**6)

from bst import *

@dataclass(frozen=True)
class Point2:
    x: float
    y: float

def comes_before(a, b) -> bool:
    return a < b

class BSTTests(unittest.TestCase):
    
    def test_empty_tree(self):
        bst: BinarySearchTree = BinarySearchTree(comes_before, None)
        self.assertTrue(is_empty(bst))
    
    def test_insert_integers(self):
        bst: BinarySearchTree = BinarySearchTree(comes_before, None)
        bst = insert(bst, 5)
        bst = insert(bst, 3)
        bst = insert(bst, 7)
        self.assertFalse(is_empty(bst))
    
    def test_lookup_integers(self):
        bst: BinarySearchTree = BinarySearchTree(comes_before, None)
        bst = insert(bst, 5)
        bst = insert(bst, 3)
        bst = insert(bst, 7)
        self.assertTrue(lookup(bst, 5))
        self.assertTrue(lookup(bst, 3))
        self.assertTrue(lookup(bst, 7))
        self.assertFalse(lookup(bst, 10))
    
    def test_delete_integers(self):
        bst: BinarySearchTree = BinarySearchTree(comes_before, None)
        bst = insert(bst, 5)
        bst = insert(bst, 3)
        bst = insert(bst, 7)
        bst = delete(bst, 3)
        self.assertFalse(lookup(bst, 3))
        self.assertTrue(lookup(bst, 5))
        self.assertTrue(lookup(bst, 7))
    
    def test_string_ordering(self):
        bst: BinarySearchTree = BinarySearchTree(comes_before, None)
        bst = insert(bst, "dog")
        bst = insert(bst, "cat")
        bst = insert(bst, "elephant")
        self.assertTrue(lookup(bst, "dog"))
        self.assertTrue(lookup(bst, "cat"))
        self.assertTrue(lookup(bst, "elephant"))
        self.assertFalse(lookup(bst, "zebra"))
    
    def test_string_delete(self):
        bst: BinarySearchTree = BinarySearchTree(comes_before, None)
        bst = insert(bst, "dog")
        bst = insert(bst, "cat")
        bst = insert(bst, "elephant")
        bst = delete(bst, "cat")
        self.assertFalse(lookup(bst, "cat"))
        self.assertTrue(lookup(bst, "dog"))
    
    def test_point2_euclidean_distance(self):
        def point_comes_before(p1: Point2, p2: Point2) -> bool:
            dist1: float = math.sqrt(p1.x * p1.x + p1.y * p1.y)
            dist2: float = math.sqrt(p2.x * p2.x + p2.y * p2.y)
            return dist1 < dist2
        
        bst: BinarySearchTree = BinarySearchTree(point_comes_before, None)
        p1: Point2 = Point2(1.0, 1.0)
        p2: Point2 = Point2(2.0, 2.0)
        p3: Point2 = Point2(0.5, 0.5)
        
        bst = insert(bst, p1)
        bst = insert(bst, p2)
        bst = insert(bst, p3)
        
        self.assertTrue(lookup(bst, p1))
        self.assertTrue(lookup(bst, p2))
        self.assertTrue(lookup(bst, p3))
    
    def test_point2_delete(self):
        def point_comes_before(p1: Point2, p2: Point2) -> bool:
            dist1: float = math.sqrt(p1.x * p1.x + p1.y * p1.y)
            dist2: float = math.sqrt(p2.x * p2.x + p2.y * p2.y)
            return dist1 < dist2
        
        bst: BinarySearchTree = BinarySearchTree(point_comes_before, None)
        p1: Point2 = Point2(1.0, 1.0)
        p2: Point2 = Point2(2.0, 2.0)
        p3: Point2 = Point2(0.5, 0.5)
        
        bst = insert(bst, p1)
        bst = insert(bst, p2)
        bst = insert(bst, p3)
        bst = delete(bst, p1)
        
        self.assertFalse(lookup(bst, p1))
        self.assertTrue(lookup(bst, p2))


if (__name__ == '__main__'):
    unittest.main()