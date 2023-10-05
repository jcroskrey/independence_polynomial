import pytest
import networkx as nx
from ind_poly_algorithm import independence_poly

def test_base_case1():
    tree = nx.path_graph(0)
    assert independence_poly(tree, coeffs=True) == 1

def test_base_case2():
    tree = nx.path_graph(1)
    assert independence_poly(tree, coeffs=True) == [1, 1]

def test_base_case3():
    tree = nx.path_graph(2)
    assert independence_poly(tree, coeffs=True) == [2, 1]

def test_4_node_path():
    tree = nx.path_graph(4)
    assert independence_poly(tree, coeffs=True) == [3, 4, 1]

def test_5_node_path():
    tree = nx.path_graph(5)
    assert independence_poly(tree, coeffs=True) == [1, 6, 5, 1] 
