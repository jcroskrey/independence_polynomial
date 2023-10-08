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
    path = nx.path_graph(4)
    assert independence_poly(path, coeffs=True) == [3, 4, 1]

def test_5_node_path():
    path = nx.path_graph(5)
    assert independence_poly(path, coeffs=True) == [1, 6, 5, 1]

def test_3_leaf_star():
    star = nx.star_graph(3)
    assert independence_poly(star, coeffs=True) == [1, 3, 4, 1]

def test_4_leaf_star():
    star = nx.star_graph(4)
    assert independence_poly(star, coeffs=True) == [1, 4, 6, 5, 1]

def test_custom_labels_star():
    # star with the max node as the center
    star = nx.Graph()
    star.add_edges_from([(5, 1), (5, 2), (5, 3)])
    assert independence_poly(star, coeffs=True) == [1, 3, 4, 1]

def test_reconstructed_tree_isomorphic_to_original():
    star = nx.star_graph(5)
    print(star.edges)
    _, mutated_tree = independence_poly(star, yield_tree=True)
    print(mutated_tree.edges)
    assert nx.isomorphism.tree_isomorphism(star, mutated_tree)

    
    