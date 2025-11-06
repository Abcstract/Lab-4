import sys
import unittest
from typing import *
from dataclasses import dataclass
import math 
import matplotlib.pyplot as plt
import numpy as np
import random
import time

sys.setrecursionlimit(10**6)

from bst import *

TREES_PER_RUN : int = 10000

def example_graph_creation() -> None:
    # Return log-base-2 of 'x' + 5.
    def f_to_graph( x : float ) -> float:
        return math.log2( x ) + 5.0
    
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
    
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    
    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

def random_tree(n: int) -> BinarySearchTree:
    bst: BinarySearchTree = BinarySearchTree(lambda a, b: a < b, None)
    for i in range(n):
        random_value: float = random.random()
        bst = insert(bst, random_value)
    return bst

def graph_average_height() -> None:
    n_max: int = 55
    num_samples: int = 50
    
    n_values: List[int] = []
    avg_heights: List[float] = []
    
    for i in range(num_samples + 1):
        n: int = int((i / num_samples) * n_max)
        n_values.append(n)
        
        if n == 0:
            avg_heights.append(0.0)
        else:
            total_height: int = 0
            for j in range(TREES_PER_RUN):
                tree: BinarySearchTree = random_tree(n)
                h: int = height(tree.tree)
                total_height = total_height + h
            
            avg_height: float = total_height / TREES_PER_RUN
            avg_heights.append(avg_height)
        
        print(f"Completed n={n}")
    
    x_numpy: np.ndarray = np.array(n_values)
    y_numpy: np.ndarray = np.array(avg_heights)
    
    plt.plot(x_numpy, y_numpy, label='Average Height')
    plt.xlabel("N (Tree Size)")
    plt.ylabel("Average Height")
    plt.title("Average BST Height vs Tree Size")
    plt.grid(True)
    plt.legend()
    plt.show()

def graph_insert_time() -> None:
    n_max: int = 55
    num_samples: int = 50
    
    n_values: List[int] = []
    avg_times: List[float] = []
    
    for i in range(num_samples + 1):
        n: int = int((i / num_samples) * n_max)
        n_values.append(n)
        
        if n == 0:
            avg_times.append(0.0)
        else:
            total_time: float = 0.0
            for j in range(TREES_PER_RUN):
                tree: BinarySearchTree = random_tree(n)
                random_value: float = random.random()
                
                start_time: float = time.time()
                tree = insert(tree, random_value)
                end_time: float = time.time()
                
                elapsed: float = end_time - start_time
                total_time = total_time + elapsed
            
            avg_time: float = total_time / TREES_PER_RUN
            avg_times.append(avg_time)
        
        print(f"Completed n={n}")
    
    x_numpy: np.ndarray = np.array(n_values)
    y_numpy: np.ndarray = np.array(avg_times)
    
    plt.plot(x_numpy, y_numpy, label='Average Insert Time')
    plt.xlabel("N (Tree Size)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Average Insert Time vs Tree Size")
    plt.grid(True)
    plt.legend()
    plt.show()

if (__name__ == '__main__'):
    graph_average_height()
    graph_insert_time()