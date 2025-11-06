import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**6)

BinTree: TypeAlias = Union[None, 'Node']

@dataclass(frozen=True)
class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree

#returns whether or not bst is empty
def is_empty(bst: BinarySearchTree) -> bool:
    if bst.tree is None:
        return True
    else:
        return False

#returns bst that has value inserted in it
def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    def insert_helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        if tree is None:
            return Node(value, None, None)
        else:
            if comes_before(value, tree.value):
                new_left: BinTree = insert_helper(tree.left, value, comes_before)
                return Node(tree.value, new_left, tree.right)
            else:
                new_right: BinTree = insert_helper(tree.right, value, comes_before)
                return Node(tree.value, tree.left, new_right)
    
    new_tree: BinTree = insert_helper(bst.tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, new_tree)

#returns whether or not bst contains value
def lookup(bst: BinarySearchTree, value: Any) -> bool:
    def lookup_helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> bool:
        if tree is None:
            return False
        else:
            if comes_before(value, tree.value):
                return lookup_helper(tree.left, value, comes_before)
            elif comes_before(tree.value, value):
                return lookup_helper(tree.right, value, comes_before)
            else:
                return True
    return lookup_helper(bst.tree, value, bst.comes_before)

#returns bst with value removed from it
def delete(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    def find_min(tree: BinTree) -> Any:
        if tree.left is None:
            return tree.value
        else:
            return find_min(tree.left)
    
    def delete_helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        if tree is None:
            return None
        else:
            if comes_before(value, tree.value):
                new_left: BinTree = delete_helper(tree.left, value, comes_before)
                return Node(tree.value, new_left, tree.right)
            elif comes_before(tree.value, value):
                new_right: BinTree = delete_helper(tree.right, value, comes_before)
                return Node(tree.value, tree.left, new_right)
            else:
                if tree.left is None:
                    return tree.right
                elif tree.right is None:
                    return tree.left
                else:
                    min_value: Any = find_min(tree.right)
                    new_right: BinTree = delete_helper(tree.right, min_value, comes_before)
                    return Node(min_value, tree.left, new_right)
    
    new_tree: BinTree = delete_helper(bst.tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, new_tree)

#returns the height of tree
def height(tree: BinTree) -> int:
    if tree is None:
        return 0
    else:
        left_height: int = height(tree.left)
        right_height: int = height(tree.right)
        if left_height > right_height:
            return 1 + left_height
        else:
            return 1 + right_height